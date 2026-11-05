# Offensive Security & Penetration Testing Portfolio

**Hands-on security assessments | Active Directory | Linux & network services | Web application security**

I have a background in computer science and software development, including work with web technologies and troubleshooting across different operating systems. I am now concentrating on **offensive security, penetration testing, and Red Team fundamentals**, with an emphasis on understanding how vulnerabilities work, validating their impact, and documenting reproducible evidence.

This repository is a collection of **authorized, isolated lab assessments**, technical investigations, and supporting study projects. Reports distinguish demonstrated results from potential impact; a successful database login, for example, is not presented as proof of operating-system compromise.

## Featured Security Assessments

| Project | What I investigated | Demonstrated result |
| --- | --- | --- |
| **[Incident 21 — MySQL Unauthenticated Root Access](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident-21-MySQL-Unauthenticated-Root-Access/)** | MySQL service discovery, TCP/MySQL traffic, authentication, SQL privilege review, DVWA data exposure, offline hash analysis | Remote MySQL root login without a password; administrative database privileges; access to DVWA user hashes; Linux `/etc/passwd` read through `LOAD_FILE()` |
| **[Incident 20 — NFS Misconfiguration](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident20-NFS-Misconfiguration/)** | NFS export enumeration, filesystem mounting, `no_root_squash` validation, protected file access and write testing | Read access to protected files and creation of a root-owned file in the remote `/root` directory; test artifact removed and share unmounted |
| **[Active Directory Assessments](./Red-Team-Active-Directory/)** | DNS/LDAP/RPC/SMB enumeration, Kerberos ticket analysis, SPN discovery and Kerberoasting | Recovered a weak lab service-account password from a requested service ticket and validated subsequent access in the isolated domain |

> **Navigation note:** The Incident 20/21 links above use the project folder names adopted in the lab reports. If either directory was uploaded under a different name or location, update that single link to match GitHub's exact path (including capitalization).

## Areas of Practice

### Active Directory & Windows Authentication

- Domain service discovery, user/group enumeration, LDAP and RPC queries, SPNs and Kerberos authentication flows.
- Kerberoasting and offline credential analysis in a controlled Windows domain.
- SMB share enumeration, permission validation and packet-level analysis with Wireshark.
- Documentation of identity, privilege boundaries and verified post-authentication access.

**Explore:** [Red Team Active Directory](./Red-Team-Active-Directory/)

### Network & Linux Penetration Testing

- Host discovery, TCP port scanning, service fingerprinting and protocol enumeration using Nmap.
- Configuration-driven service exposure: NFS exports and MySQL authentication/authorization failures.
- Controlled Linux service exploitation, privilege verification, evidence collection and cleanup.
- Linking the observed configuration to a specific security impact rather than treating an open port as a vulnerability.

**Explore:** [Network Penetration Testing](./Network-Pentesting/)

### Web Application Security

- HTTP request inspection and modification with Burp Suite and PortSwigger Web Security Academy labs.
- Authentication, access control, SQL injection, JWT behavior and other application security fundamentals.
- Independent application and database investigations with commands, results and technical explanations.

**Explore:** [Network Penetration Testing](./Network-Pentesting/)

### Security Research, Linux & Networking Foundations

- Local research experiments involving document security and hidden data, with method and limitations documented.
- Linux command-line practice, shell pipelines, permissions and system investigation.
- Cisco Packet Tracer projects covering ARP, ICMP, subnetting and basic routing.

**Explore:** [Security Research](./Security-Research/) · [Linux Terminal](./Linux-Terminal-From-Zero/) · [Networking](./Networking/)

## Tools & Technologies

| Category | Hands-on tools and technologies |
| --- | --- |
| Reconnaissance & exploitation | Kali Linux, Nmap, Metasploit, Impacket, NetExec, Netcat, SearchSploit |
| Windows / AD | Active Directory, DNS, LDAP, Kerberos, SMB, RPC, Windows command-line tools |
| Traffic analysis | Wireshark, TCP/IP, packet capture and protocol interpretation |
| Web & databases | Burp Suite, PortSwigger labs, MySQL/MariaDB, SQL, HTTP |
| Credential analysis | John the Ripper, Hashcat, name-that-hash |
| Development & labs | Python, Bash, Git, Markdown, VirtualBox, Cisco Packet Tracer |

These are tools used during projects or training, **not claims of professional mastery in every item**.

## How Projects Are Documented

Most hands-on assessments follow a repeatable workflow:

```text
Scope & Lab Setup
       ↓
Discovery & Enumeration
       ↓
Hypothesis & Controlled Validation
       ↓
Evidence & Impact Assessment
       ↓
Cleanup & Remediation Recommendations
```

Reports aim to include the test environment, exact commands and relevant options, terminal or packet-capture evidence, interpretation, limitations, and practical mitigation recommendations. All penetration testing is performed against systems I own or am explicitly authorized to test.

## Current Direction

I am developing deeper practical competence in **internal penetration testing, Active Directory attack paths, Linux service security and web application testing**. My goal is to translate a longstanding computing background into well-evidenced offensive security work, while continuing to improve technical depth and reporting quality.

---

*This portfolio is an ongoing record of independently executed lab work. Findings and outcomes are specific to intentionally vulnerable training environments, not production engagements.*
