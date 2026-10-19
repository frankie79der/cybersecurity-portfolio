# Lab 001 — Building and Analyzing a Local Area Network (LAN)

**Track:** Network Infrastructure — Fundamentals  
**Tool:** Cisco Packet Tracer (free)  
**Lab file:** `Lab001.pkt`  
**Environment:** Fully simulated; no physical networking equipment required

## 1. Objective

Build a small Ethernet LAN from scratch, configure static IPv4 addressing, verify host-to-host connectivity, and inspect **how the communication actually works** using Packet Tracer's Simulation Mode and the Cisco switch CLI.

By the end of this lab, I practiced:

- Connecting two end hosts to a Layer 2 switch.
- Configuring IPv4 addresses and subnet masks manually.
- Testing reachability with `ping` and inspecting settings with `ipconfig`.
- Discovering IPv4-to-MAC mappings with ARP.
- Comparing **ARP Request (broadcast)** and **ARP Reply (unicast)**.
- Inspecting a Cisco switch's learned MAC Address Table.
- Observing **ICMP Echo Request (Type 8)** and **Echo Reply (Type 0)**.
- Distinguishing an **IP address**, a **MAC address**, and a **physical switch port**.

## 2. Network Topology

```text
  PC0                   Switch0                     PC1
PC-PT                 2960-24TT                   PC-PT
192.168.1.10                                      192.168.1.20
      FastEthernet0 ── Fa0/1   Fa0/2 ── FastEthernet0
                        VLAN 1
             Subnet: 192.168.1.0/24
```

### Devices and connections

| Device | Interface | Connected to | Addressing |
|---|---|---|---|
| PC0 | FastEthernet0 | Switch0 Fa0/1 | 192.168.1.10/24 |
| Switch0 | Fa0/1 and Fa0/2 | PC0 and PC1 | Layer 2 switching; no management IP needed |
| PC1 | FastEthernet0 | Switch0 Fa0/2 | 192.168.1.20/24 |

Both connections use **Copper Straight-Through** Ethernet cables. Green link indicators confirm that the physical Ethernet links are up. An amber switch-port indicator during initialization does not necessarily mean a cabling error.

### IPv4 configuration

| Setting | PC0 | PC1 |
|---|---|---|
| IPv4 address | `192.168.1.10` | `192.168.1.20` |
| Subnet mask | `255.255.255.0` | `255.255.255.0` |
| Default gateway | Not configured | Not configured |
| DNS server | Not configured | Not configured |

**Why no default gateway?** The hosts are on the same IPv4 subnet, so they can exchange traffic directly through the switch. A default gateway is used to route traffic toward **other IP networks**, not just toward the Internet. No router is present or required in this lab. DNS is not needed because the test uses IP addresses rather than hostnames.

## 3. Building the LAN

1. In Packet Tracer's **Logical** workspace, add two **PC-PT** devices and one **2960-24TT** switch.
2. Connect `PC0 FastEthernet0` to `Switch0 FastEthernet0/1` with **Copper Straight-Through**.
3. Connect `PC1 FastEthernet0` to `Switch0 FastEthernet0/2` with the same cable type.
4. Wait for the links to become active.
5. On each PC, open **Desktop > IP Configuration**, select **Static**, and enter the IPv4 settings from the table above.
6. Save the topology as **`Lab001.pkt`**.

### Initial configuration check

On each PC, open **Desktop > Command Prompt**:

```text
ipconfig
```

Before IPv4 configuration, PC0 displayed `0.0.0.0` for its IPv4 address and subnet mask. It also had an IPv6 link-local address (`FE80::...`), so **no configured IPv4 address** did not mean that every form of IP communication was impossible.

After assigning the static addresses, `ipconfig` displayed the expected IPv4 configuration on both hosts.

## 4. Connectivity Test — Ping

From **PC0**, run:

```text
ping 192.168.1.20
```

**Observed result:** four replies, **4 packets sent, 4 received, 0 lost (0% loss)**.

This verifies IPv4 reachability using **ICMP** between PC0 and PC1. A successful ping is useful evidence of connectivity, but it does not by itself explain *how* the devices discovered each other's Ethernet addresses or how the switch forwarded the frames. That is what the following sections investigate.

## 5. ARP — From an IPv4 Address to a MAC Address

A local Ethernet sender needs an appropriate **destination MAC address** to transmit a frame to the next hop. In our same-subnet setup, PC0 needs PC1's MAC address.

On PC0:

```text
arp -a
```

**Before the first ping**, the ARP cache was empty:

```text
No ARP Entries Found
```

**After the ping**, PC0 had learned:

```text
Internet Address    Physical Address    Type
192.168.1.20        0040.0bc8.d0e8     dynamic
```

### ARP Request — broadcast

Packet Tracer showed PC0 sending an ARP Request with:

```text
Ethernet source MAC:       000C.8512.E8E3  (PC0)
Ethernet destination MAC:  FFFF.FFFF.FFFF  (broadcast)
ARP sender IP:             192.168.1.10
ARP target IP:             192.168.1.20
```

The request effectively means: **"Who has 192.168.1.20? Tell 192.168.1.10."**

PC0 knows PC1's IPv4 address but not its MAC, so it cannot yet address a unicast Ethernet frame directly to PC1. Instead, it transmits to the Ethernet broadcast address `FFFF.FFFF.FFFF`.

Switch0 receives the frame on `Fa0/1` and **floods the broadcast** to other active ports in the same VLAN (in this topology, `Fa0/2`). PC1 receives it and sees that the ARP target IP matches its own address.

> **Important:** The sender and target IPv4 addresses shown inside the ARP message are *ARP fields*. An ARP Request is **not** an IPv4 packet carrying ARP inside it.

### ARP Reply — unicast

PC1 responds with its MAC address. The observed frame contained:

```text
Ethernet source MAC:       0040.0BC8.D0E8  (PC1)
Ethernet destination MAC:  000C.8512.E8E3  (PC0)
ARP sender IP:             192.168.1.20
ARP target IP:             192.168.1.10
```

The reply effectively means: **"192.168.1.20 is at 0040.0BC8.D0E8."**

PC1 can reply **unicast** because PC0's MAC was included in the request. PC0 can then cache the IPv4-to-MAC association and send the ICMP packet in a frame addressed to PC1's MAC.

Dynamic ARP cache entries are temporary; they may expire. Earlier communication does not guarantee the entry will remain available forever.

### Packet Tracer command limitation

Attempting to remove the ARP entry with:

```text
arp -d 192.168.1.20
```

produced **`Invalid Command.`** Packet Tracer's PC terminal is a simplified simulation and does not support all Windows commands. To repeat the initial ARP discovery, a practical lab workaround is to **power-cycle the simulated PC** and check `arp -a` again before sending new traffic.

## 6. Switch MAC Address Learning

A Layer 2 switch uses a **MAC Address Table** to associate learned source MAC addresses with switch ports (within the relevant VLAN).

When Switch0 receives a frame on `Fa0/1` with PC0's source MAC, it learns that PC0 is reachable through `Fa0/1`. When it receives PC1's reply on `Fa0/2`, it learns PC1's MAC on that port.

To inspect the real table in the lab, open **Switch0 > CLI** and run:

```text
enable
show mac address-table
```

**Observed entries:**

```text
Vlan    Mac Address       Type       Ports
----    -----------       --------   -----
1       000c.8512.e8e3    DYNAMIC    Fa0/1
1       0040.0bc8.d0e8    DYNAMIC    Fa0/2
```

| Column | Meaning |
|---|---|
| VLAN 1 | Both ports belong to the default VLAN in this lab. |
| Mac Address | Hardware address learned from a frame's **source MAC**. |
| DYNAMIC | Learned from traffic rather than manually configured. |
| Fa0/1 / Fa0/2 | Switch port associated with that MAC. |

**Two different tables — do not confuse them:**

- **ARP Cache (host):** maps an **IPv4 address → MAC address**.
- **MAC Address Table (switch):** maps a **MAC address → switch port**, in a VLAN.

The switch **learns using the source MAC** and makes its forwarding decision using the **destination MAC**. It does not need to know PC0's or PC1's IPv4 addresses to perform normal Layer 2 forwarding. Dynamic MAC entries can age out when no relevant traffic is seen.

## 7. Packet Tracer Simulation — Following the Traffic

1. Switch from **Realtime** to **Simulation**.
2. Set **Edit Filters** so that only **ARP** and **ICMP** are visible.
3. Use **Add Simple PDU** (closed-envelope icon), clicking **PC0** and then **PC1**.
4. Use **Capture/Forward** to advance one event at a time.
5. Click each envelope to open **PDU Information**; examine **OSI Model** and **Inbound/Outbound PDU Details**.

### Sequence observed in the lab

```text
1. PC0 -> Switch0:  ARP Request (broadcast)
2. Switch0 -> PC1: ARP Request forwarded
3. PC1 -> Switch0:  ARP Reply (unicast)
4. Switch0 -> PC0: ARP Reply forwarded
5. PC0 -> Switch0:  ICMP Echo Request (unicast Ethernet frame)
6. Switch0 -> PC1: ICMP Echo Request forwarded
7. PC1 prepares:   ICMP Echo Reply
8. Expected return path: PC1 -> Switch0 -> PC0
```

The screenshots inspected during the session confirmed the request reaching PC1 and PC1 preparing its Echo Reply. **The final return path was not separately documented in the shared Simulation screenshots**, although the earlier CLI `ping` had already confirmed successful end-to-end replies.

### Ethernet header during the ICMP request

After ARP resolution, the observed frame heading toward PC1 contained:

```text
Source MAC:       000C.8512.E8E3  (PC0)
Destination MAC:  0040.0BC8.D0E8  (PC1)
Switch input:     Fa0/1
Switch output:    Fa0/2
```

Unlike the ARP Request, the frame is now **unicast**: PC0 knows the destination MAC and Switch0 knows the destination port.

## 8. ICMP — Understanding the Ping

At **PC1**, Packet Tracer's **OSI Model** displayed:

| Field | Incoming request | Outgoing reply |
|---|---|---|
| Source IPv4 | `192.168.1.10` | `192.168.1.20` |
| Destination IPv4 | `192.168.1.20` | `192.168.1.10` |
| ICMP Type | **8 — Echo Request** | **0 — Echo Reply** |
| Ethernet source MAC | PC0 MAC | PC1 MAC |
| Ethernet destination MAC | PC1 MAC | PC0 MAC |

ICMP operates at the **Network layer (Layer 3)** alongside IPv4. The ICMP *Type* field is **not a TCP or UDP port number**.

### How these protocols cooperate

- **ARP:** resolves the next hop's IPv4 address to an Ethernet MAC address on the local network.
- **Ethernet:** carries frames on the LAN using source and destination MAC addresses.
- **Switching:** forwards Ethernet frames according to the switch's MAC Address Table.
- **IPv4:** supplies source and destination IP addresses for the packet.
- **ICMP:** carries the Echo Request and Echo Reply used by `ping`.

In short: **ARP discovers, Ethernet carries, the switch forwards, and ICMP tests reachability.**

## 9. Troubleshooting Notes

| Symptom | What to check |
|---|---|
| Link stays down | Cable type, selected ports, device power, interface status. |
| IPv4 address is `0.0.0.0` | Set a valid static IPv4 address in Desktop > IP Configuration. |
| Ping fails | Check both IPs, subnet masks, physical links, and ARP learning. |
| No ARP Request appears | ARP entry may already be cached; check `arp -a` and restart the simulated PC if necessary. |
| No useful Simulation events | Check ARP/ICMP filters and create a new Simple PDU. |
| `arp -d` returns `Invalid Command` | Packet Tracer PC command support is limited; this is not a cabling failure. |
| MAC table is empty | Generate frames, then rerun `show mac address-table`; dynamic entries may age out. |

## 10. Screenshot Evidence

Screenshots were captured during the hands-on session. Add them to a `screenshots/` directory using **your actual filenames**, then link them here or in the matching sections above.

Recommended evidence order:

1. **Topology:** PC0 — Switch0 — PC1, with green links.
2. **Initial PC0 `ipconfig`:** IPv4 address `0.0.0.0` before configuration.
3. **Static IPv4 configuration:** PC0 and PC1 settings.
4. **Successful ping and ARP cache:** `ping 192.168.1.20` and `arp -a`.
5. **ARP Request at Switch0:** destination MAC `FFFF.FFFF.FFFF`.
6. **ARP Request / Reply at PC1:** incoming broadcast, outgoing unicast.
7. **ARP Reply at Switch0:** `Fa0/2` inbound, `Fa0/1` outbound.
8. **Switch CLI:** `show mac address-table` output.
9. **ICMP request at Switch0:** unicast MAC addresses.
10. **ICMP at PC1:** Type 8 received, Type 0 prepared.

Suggested repository structure:

```text
Lab001/
├── README.md
├── Lab001.pkt
└── screenshots/
    └── (your captured PNG/JPG files)
```

## 11. Quick Review — Read Before Your Next Lab

**Q: Is a green Ethernet link enough to guarantee IPv4 connectivity?**  
No. Physical link status and correct Layer 3 addressing are separate requirements.

**Q: Why is there no default gateway in this topology?**  
Both hosts are in the same subnet; neither needs routing to another network to communicate.

**Q: Why is the first ARP Request a broadcast?**  
PC0 knows the target IPv4 address but does not yet know its destination MAC.

**Q: How does PC1 know it should respond?**  
The target IPv4 address in the ARP Request matches PC1's own IPv4 address.

**Q: Why is the ARP Reply unicast?**  
The request already provides PC0's MAC address to PC1.

**Q: What does the switch learn from incoming frames?**  
Their **source MAC addresses** and the **ports** where those frames arrived.

**Q: How is the switch's MAC table different from a PC's ARP cache?**  
ARP cache = IP-to-MAC; switch MAC table = MAC-to-port (per VLAN).

**Q: What are ICMP Types 8 and 0?**  
Echo Request and Echo Reply, respectively.

### Essential commands

```text
# Packet Tracer PC Command Prompt
ipconfig
ping 192.168.1.20
arp -a

# Cisco 2960 CLI
 enable
 show mac address-table
```

## 12. Outcome and Next Steps

**Verified:** devices connected, static IPv4 configured, four successful ping replies, dynamic ARP entry observed, ARP Request and Reply inspected, dynamic MAC table entries confirmed in the switch CLI, and ICMP Type 8 / Type 0 observed at PC1.

**Next:** finish capturing the ICMP Echo Reply returning to PC0, then repeat the packet flow from memory and extend the topology to explore switching behavior and troubleshooting.

---

*Educational networking lab completed in a simulated environment with Cisco Packet Tracer. The commands, addressing, MAC values, and observations above reflect this particular lab and are not claims of production infrastructure experience.*
