# Cybersecurity Portfolio

### Offensive Security · Network Infrastructure · Active Directory · Web Application Testing · Security Research

**From understanding how systems communicate to testing how they can fail.**

A practical, evidence-driven collection of network builds, security investigations, penetration-testing labs, and technical research. Every project is part of a larger effort to understand the technology, reproduce the behavior, verify the outcome, and document what the evidence actually proves.

---

## 👤 Who I Am

My interest in computing started in the late 1990s, when my first experiences with a computer involved typing BASIC code just to make a program run. I did not understand every line back then, but I was fascinated by what computers could do—and, even more, by figuring out *how* they worked.

Over the years, that curiosity developed into hands-on experience with PC hardware, operating-system troubleshooting, software, and web development. I worked with technologies including **PHP, Ruby, Joomla, Drupal, and WordPress**, and began thinking about security while building database-backed applications and learning why vulnerabilities such as SQL injection matter.

I hold a **Bachelor's degree in Computer Science from Italy**. Today, my main focus is **Offensive Security**, particularly internal-network penetration testing, Windows Active Directory, Linux exploitation, and web application security. I enjoy working at the terminal, investigating protocols, writing and testing commands, and understanding *why* an attack succeeds—not just reproducing someone else's instructions.

This repository is a record of that work: **network infrastructure I build, systems I investigate, vulnerabilities I validate, and the evidence I collect**. It is based on self-directed research and controlled, authorized laboratories, not on claims of commercial penetration-testing engagements.

> **What I care about:** technical curiosity, repeatable experiments, accurate findings, and the discipline to distinguish a demonstrated result from an assumption.

---

## 🧭 Explore the Portfolio

**New here?** Choose a topic below. Each link opens a project area with its own labs, documentation, configurations, screenshots, and technical results where available. You do not need to understand cybersecurity to find your way around.

| Explore | What's inside | Why it matters |
|---|---|---|
| **[🌐 Network Infrastructure](./Network-Infrastructure/)** | Cisco Packet Tracer, LAN design, switching, IPv4, routing, VLAN segmentation | Build and understand networks *before* trying to assess their security |
| **[🪟 Active Directory & Red Team](./Red-Team-Active-Directory/)** | Domain services, DNS, LDAP, RPC, SMB, Kerberos, Kerberoasting, privilege validation | Understand identity and attack paths inside Windows networks |
| **[⚔️ Network Penetration Testing](./Network-Pentesting/)** | Reconnaissance, Linux services, credential attacks, Metasploitable 2, exploitation, verification | Turn a discovered weakness into a documented security finding |
| **[🌍 Web Application Security](./Network-Pentesting/Web-Application-Pentesting/)** | Burp Suite, PortSwigger exercises, SQL injection, JWT, access control, Juice Shop, VulnShop | Test the security assumptions behind web applications and APIs |
| **[🔬 Security Research](./Security-Research/)** | PDF prompt injection, AI evaluation experiments, image steganography investigation | Investigate hypotheses without exaggerating the results |
| **[🐧 Linux Terminal & Tooling](./Linux-Terminal-From-Zero/)** | Linux administration, shell commands, permissions, Bash, scripting, troubleshooting | Develop the practical command-line foundation behind every lab |

**Suggested route for a first-time visitor:** Network Infrastructure → Active Directory or Network Penetration Testing → a complete case study → its screenshots and technical conclusions.

---

## ⭐ Selected Work — Start with the Evidence

These examples demonstrate different kinds of technical work. **A network design is not an exploit, and database access is not automatically an operating-system compromise.** Each is valuable for a different reason.

| Case study | What was tested | Demonstrated result |
|---|---|---|
| **Network Infrastructure — Labs 001–005** | Host communication, ARP/ICMP, gateways, routed networks, static routes, VLANs | Built and tested progressively more complex networks, including isolated VLAN broadcast domains |
| **Active Directory — Kerberoasting and privileged access** | DNS/LDAP/RPC discovery, SPNs, Kerberos tickets, password recovery, SMB permissions | Recovered a weak lab service-account credential and verified the associated permissions and administrative access |
| **[Incident 20 — NFS Misconfiguration](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident20-NFS-Misconfiguration/)** | World-accessible NFS root export with `no_root_squash` | Read a protected file using client-root privileges and created a root-owned proof file in the remote `/root` directory |
| **[Incident 21 — MySQL Unauthenticated Root Access](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident-21-MySQL-Unauthenticated-Root-Access/)** | Exposed MySQL service, passwordless login, global privileges, DVWA data, file reads | Logged in as MySQL root without a password; verified grants, recovered a weak lab password, and read `/etc/passwd` via `LOAD_FILE()` |
| **Linux — DistCC and Samba investigations** | Network services, code execution paths, identity and file permissions | Validated remote execution and, in documented lab exercises, privileged execution contexts |
| **Web applications — SQL injection and authentication** | HTTP requests, input handling, database queries, sessions and access control | Reproduced vulnerable workflows and validated their impact in deliberately vulnerable applications |

---

## 🗺️ How the Technical Work Fits Together

```text
             NETWORK INFRASTRUCTURE
      Switching · ARP · IP · Routing · VLANs
                        |
                        v
               SYSTEMS & SERVICES
         Linux · Windows · DNS · SMB · SQL
                        |
                        v
            RECONNAISSANCE & ANALYSIS
         Nmap · Wireshark · LDAP · Burp
                        |
                        v
             SECURITY VALIDATION
       Authentication · Access · Exploitation
                        |
                        v
             EVIDENCE & REPORTING
        Findings · Limits · Cleanup · Fixes
```

Infrastructure provides the context; security testing examines what happens when services, identities, permissions, or applications are configured incorrectly. The repository includes **both sides of that learning process**.

---

# 📚 Complete Technical Index

The sections below are a detailed guide to the topics represented in the portfolio. Expand any area to see the methods, concepts, and specific laboratory work behind it.

<details>
<summary><strong>01 — Network Infrastructure & Cisco Packet Tracer</strong> · Switching, routing, VLANs, and connectivity</summary>

### Building the network, not just scanning it

This track uses Cisco Packet Tracer to build networks from a blank workspace, configure devices, and verify connectivity. The work develops the infrastructure knowledge needed to understand attack surfaces, segmentation, lateral movement, and network troubleshooting.

| Lab | Focus | Core concepts and validation |
|---|---|---|
| **LAB001** | Basic switched LAN | Two PCs, one switch, IPv4 `/24`, ARP address resolution, ICMP echo, packet simulation |
| **LAB002** | Expanded LAN and addressing | Three-PC network, addressing, subnet boundaries, same-network communication, repeatable configuration |
| **LAB003** | Routing between two networks | Two IPv4 `/24` networks, a router, interface addressing, default gateways, end-to-end ping tests |
| **LAB004** | Two routers and static routes | Two routed LANs, a `/30` inter-router link, connected versus static routes, routes in both directions, `show ip route` |
| **LAB005** | VLAN segmentation and network isolation | Cisco 2960 switch, VLAN 10 and VLAN 20, access-port membership, `show vlan brief`, intra-VLAN connectivity and absence of inter-VLAN routing |

**Key networking topics:** Ethernet frames, MAC addresses, Layer 2 switching, ARP, ICMP, IPv4 addressing, CIDR notation, subnets, gateways, Layer 3 forwarding, routing tables, directly connected networks, static routing, Cisco IOS commands, VLANs, access ports, broadcast domains, and topology validation.

**Important distinction:** placing devices in different VLANs creates separate Layer 2 broadcast domains. A failed cross-subnet ping alone does not prove VLAN isolation; addressing, gateways, and routing also affect connectivity. The VLAN work examines those distinctions rather than treating every failed packet as a security control.

**Evidence style:** topology diagrams, device commands, configuration outputs, Simulation Mode behavior, and connectivity tests.

</details>

<details>
<summary><strong>02 — Windows Active Directory & Internal Red Team Labs</strong> · Identity, Kerberos, SMB, privilege paths</summary>

### Investigating a small Windows domain

An isolated Windows domain lab with a domain controller, Windows clients, accounts, service principals, and Kali Linux supports a progression from normal enterprise authentication to authorized offensive tests.

**Directory and infrastructure discovery**

- Windows domains, domain controllers, domain membership, users, groups, organizational units, SIDs and RIDs.
- Domain DNS and service-discovery records, including LDAP SRV lookups.
- LDAP queries, RPC domain enumeration, group membership checks, and service principal names (SPNs).
- Authentication versus authorization: who an account is and what it may actually do.

**Kerberos and Windows network protocols**

- AS-REQ / AS-REP, pre-authentication, TGTs, TGS-REQ / TGS-REP, the KDC, and ticket caches.
- SMB negotiation, session setup, share enumeration, tree connects, and administrative share access.
- NTLM versus Kerberos behavior, network captures in Wireshark, and correlation with Windows commands such as `klist`.

**Offensive scenarios demonstrated in the lab**

- SPN enumeration and Kerberoasting from a domain-user context.
- Offline password testing and validation of recovered lab credentials.
- SMB access checks, administrative share access, and authenticated remote execution in controlled exercises.
- Scoped directory replication / DCSync testing with verified privileges, without equating a single-account extraction with a complete environment compromise.

**Tools:** Impacket, `ldapsearch`, `rpcclient`, `smbclient`, `dig`, NetExec, Hashcat, John the Ripper, Wireshark, and native Windows administration commands.

</details>

<details>
<summary><strong>03 — Network Penetration Testing & Linux Service Exploitation</strong> · Discovery through impact validation</summary>

### Understanding what an exposed service really allows

This track documents controlled attacks on deliberately vulnerable systems, principally Metasploitable 2. The objective is not to collect exploits, but to verify prerequisites, exploit behavior, execution identity, permissions, impact, and cleanup.

**Reconnaissance and enumeration**

- Host discovery, TCP SYN scans, version detection, targeted NSE scripts, service banners, and port mapping.
- FTP, SSH, Telnet, DNS, web services, SMB, NFS, MySQL, and other exposed services.
- Command-line result processing, evidence capture, and distinguishing an open port from a demonstrated vulnerability.

**Representative security investigations**

- **vsftpd / FTP:** identifying vulnerable service versions and testing known lab behavior.
- **DistCC:** demonstrating remote command execution, validating a shell context, enumerating SUID programs, and examining a legacy Nmap-based privilege-escalation path.
- **Samba:** anonymous enumeration and investigation of a vulnerable username-map configuration with verified execution results.
- **NFS — Incident 20:** `showmount`, filesystem mounting, comparison of ordinary and root-level file access, `no_root_squash`, root-owned proof file, removal, and unmount verification.
- **MySQL — Incident 21:** Nmap's MySQL scripts, TCP and application handshake, TLS negotiation issue, successful passwordless `root` login, grants, DVWA records, MD5 password analysis, and `LOAD_FILE()`.
- **Related investigations:** credential testing, Metasploit modules, reverse shells, post-exploitation checks, authorized MITM/traffic-observation exercises, and virtual-lab setup where documented.

**Critical distinctions:** service reachability versus authentication; database administrator versus operating-system root; a root-owned file versus a remote root shell; credential recovery versus verified access using that credential.

</details>

<details>
<summary><strong>04 — Web Application Penetration Testing</strong> · Burp, SQL injection, JWT, authentication and APIs</summary>

### Testing applications through their requests and state

This area combines browser-based observation, manual HTTP testing, vulnerable web applications, and structured PortSwigger Web Security Academy practice.

**Web security topics**

- HTTP requests, responses, headers, status codes, cookies, sessions, and the role of proxies.
- Authentication failures, broken access control, insecure direct object references (IDOR), and authorization checks.
- SQL injection in search and login workflows, including laboratory authentication-bypass investigations.
- JWT structure, signatures, signature verification, algorithm handling, and the difference between editing a payload and producing a valid token.
- Path traversal, file upload behavior, OS command injection, and related application input-validation issues.
- API authorization and response interpretation without treating every error message as a confirmed exploit.

**Applications and tooling**

- **PortSwigger Web Security Academy:** topic-specific practical labs and manual request analysis.
- **OWASP Juice Shop:** application/API investigation, SQL injection, authentication and access-control behavior, supported by documented evidence.
- **VulnShop:** a deliberately vulnerable training web application explored through a complete investigation and then documented as a case study.
- **Burp Suite:** Proxy, Repeater, request modification, response comparison, and controlled testing.

The emphasis is on a clear chain: **baseline behavior → test case → response comparison → impact confirmation**.

</details>

<details>
<summary><strong>05 — Independent Security Research</strong> · Experimental methods and evidence interpretation</summary>

### Security questions that do not always end with an exploit

Research projects are deliberately kept separate from conventional penetration-test incidents. They investigate how information, files, and tools behave, and explicitly describe the limits of each result.

**PDF Prompt Injection**

- Prepared clean and modified PDF résumé inputs.
- Extracted and inspected PDF text with `pdftotext` and supporting Python/PDF tooling.
- Tested the inputs in an AI-based evaluation workflow using a local model environment.
- Recorded observed behavior and limitations. **The recorded experiment did not establish a successful bypass or guaranteed manipulation of the evaluator.**

**Image Steganography Investigation**

- Examined image metadata and structure with `exiftool`, `binwalk`, `steghide`, and Python/Pillow.
- Explored least-significant-bit (LSB) extraction and evaluated recovered content.
- Distinguished suspicious artifacts from evidence of an actual hidden message.

These exercises demonstrate investigative discipline: a negative or inconclusive result can still be valuable when the method and evidence are documented correctly.

</details>

<details>
<summary><strong>06 — Linux, Python, Virtual Labs & Technical Foundations</strong> · The practical tools behind the investigations</summary>

### Working directly with systems

**Linux terminal and administration**

- Filesystem navigation, absolute and relative paths, ownership, groups, file permissions, SUID, processes, and services.
- Shell pipelines and redirection, `grep`, `awk`, `find`, `cat`, `head`, `tee`, `chmod`, `ls`, and related tools.
- Text processing, command output capture, repeatable checks, and safe cleanup of test artifacts.
- Linux networking tools, mounted remote filesystems, and troubleshooting command failures.

**Programming and experiments**

- Python for lab utilities, data parsing, security experiments, and small automation tasks.
- Bash scripting and reproducible terminal workflows.
- Web application background in PHP, Ruby, CMS platforms, and database-backed applications.
- Supporting command-line and networking experiments, including small utilities such as MiniConnect where documented.

**Lab engineering**

- VirtualBox-based Windows and Linux test environments, isolated networks, and multiple Kali network interfaces.
- Cisco Packet Tracer infrastructure simulations kept separate from offensive-target virtual machines.
- Git and GitHub Markdown documentation, screenshots, packet captures, findings, and remediation notes.

Foundational exercises are included because reliable penetration testing depends on understanding operating systems and networks—not only on knowing exploitation tools.

</details>

---

## 🧰 Technical Toolbox

| Area | Tools, environments and protocols used |
|---|---|
| **Network engineering** | Cisco Packet Tracer, Cisco IOS, Ethernet, ARP, ICMP, IPv4/CIDR, switching, static routing, VLANs |
| **Reconnaissance** | Nmap, NSE, Linux `ip` tools, `dig`, service enumeration, SearchSploit |
| **Windows / Active Directory** | Kerberos, DNS, LDAP, RPC, SMB, Impacket, NetExec, `rpcclient`, `smbclient`, Windows CLI |
| **Web and databases** | Burp Suite, HTTP, SQL, MySQL/MariaDB, JWT, OWASP Juice Shop, PortSwigger labs |
| **Credential analysis** | John the Ripper, Hashcat, Name-That-Hash, hash-format verification |
| **Network traffic analysis** | Wireshark, TCP three-way handshake, MySQL greeting/login, Kerberos and SMB packet inspection |
| **Linux and development** | Kali Linux, Bash, Python, PHP, Ruby, file permissions, process/service analysis |
| **Lab and reporting** | VirtualBox, GitHub, Markdown, screenshots, network diagrams, evidence-led write-ups |

*Tools listed here have been used in laboratory work; listing them does not imply expert-level mastery or a professional certification.*

---

## 🔎 How I Work

```text
Scope and lab preparation
          ↓
Build or understand the environment
          ↓
Discover hosts, services, or application behavior
          ↓
Form a testable hypothesis
          ↓
Perform a controlled, authorized test
          ↓
Verify the technical result and its limits
          ↓
Collect evidence and explain the impact
          ↓
Remove test artifacts and document remediation
```

Each investigation aims to answer four questions: **What did I test? What actually happened? Why did it happen? What would reduce the risk?**

I prefer to complete the technical learning and testing first. When a case is understood, I repeat the relevant steps to capture clean screenshots, command output, and a final report. This separates exploration from presentation and helps keep the evidence consistent with the claims.

## 📖 How to Read an Individual Project

1. Read the **Overview / Objective** to understand the scope and expected behavior.
2. Check the **Environment / Topology** to identify systems, networks, and prerequisites.
3. Follow the **Method / Commands / Configurations** to understand what was executed or built.
4. Compare the **Evidence** with the findings: a screenshot should support a concrete claim.
5. Read the **Impact, Limitations, Cleanup, and Remediation** before drawing conclusions.

Some investigations demonstrate an exploited misconfiguration. Others are infrastructure builds, protocol studies, or exploratory research. **They are labeled separately on purpose.**

---

## 🎯 Current Direction

I am developing toward **Red Team / Penetration Testing** work, with continued emphasis on:

- Internal Windows and Linux environments, Active Directory, and realistic attack paths.
- Network infrastructure, segmentation, routing, and the protocols that make those environments work.
- Web application and database testing based on reproducible evidence.
- Stronger independent troubleshooting, command-line skills, and professional-quality reporting.

The goal is to combine a long-standing interest in computing with disciplined offensive-security practice: **understand the system, investigate the weakness, prove only what the evidence supports, and communicate it clearly.**

---

<sub>**Scope and ethics:** All offensive demonstrations described here are performed in isolated or explicitly authorized environments, including intentionally vulnerable training applications and virtual machines. Test credentials and results belong to those environments. This portfolio is a record of hands-on technical projects and continued study, not a claim of commercial engagement history.</sub>
