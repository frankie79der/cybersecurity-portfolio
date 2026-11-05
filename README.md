# Offensive Security | Penetration Testing | Security Research

**Hands-on attack-path validation, technical investigations, and reproducible lab evidence**

I am a Computer Science graduate with a longstanding background in computing, software development, web technologies, operating systems, and troubleshooting. My current focus is **offensive cybersecurity**, particularly **internal penetration testing, Active Directory, Linux service exploitation, web application security, and security research**.

This repository documents practical work conducted in **isolated, authorized lab environments**. I work from initial discovery through enumeration, controlled exploitation, evidence collection, impact verification, cleanup, and technical reporting. The projects below are learning and research work—not claims of commercial penetration-testing engagements.

> **Start here:** The featured case studies provide the clearest demonstrations of technical findings and their impact. The sections that follow are a broader map of the portfolio, including investigative research and foundational engineering labs.

---

## Portfolio at a Glance

| Track | What the work demonstrates | Representative investigations |
| --- | --- | --- |
| **Active Directory & Internal Networks** | Windows identity, Kerberos, LDAP/RPC, SMB, privilege mapping, credential attack paths | Kerberos/SMB traffic, SPN enumeration, Kerberoasting, authenticated access validation, DCSync lab |
| **Linux & Network Penetration Testing** | Network discovery, service enumeration, exploitation, permission boundaries | DistCC RCE, Samba misconfiguration, NFS `no_root_squash`, MySQL root exposure |
| **Web Application Penetration Testing** | HTTP testing, request tampering, application authorization and input validation | Burp Suite, PortSwigger exercises, SQL injection, JWT, file upload and command injection labs |
| **Security Research** | Experimental methods, evidence analysis, explaining limitations | PDF prompt injection and AI evaluation, image steganography investigation |
| **Networking & Protocol Analysis** | Packet interpretation and routing fundamentals | Wireshark TCP/Kerberos/SMB/MySQL; Cisco Packet Tracer switching and routing |
| **Linux, Python & Technical Tooling** | Command-line proficiency, automation and repeatable lab workflows | Bash pipelines, filesystem permissions, Nmap tooling, Python security experiments |

## Featured Case Studies — Verified Impact

### 01. Unauthenticated MySQL Administrative Access — Incident 21

**Scope:** Metasploitable 2, MySQL 5.0.51a, TCP/3306, isolated internal lab.

- Identified the exposed database service using Nmap version detection and the `mysql-info` NSE script.
- Captured TCP connection setup, MySQL server greeting, failed TLS negotiation, and a successful login flow in Wireshark.
- Authenticated remotely as MySQL `root` **without a password**, and verified the matched account `root@%`.
- Confirmed `ALL PRIVILEGES ON *.* WITH GRANT OPTION` rather than assuming privileges from the username.
- Enumerated DVWA tables and retrieved stored password hashes in the lab.
- Identified a raw MD5 hash and validated the weak password using SQL and John the Ripper.
- Demonstrated server-side file disclosure through `LOAD_FILE('/etc/passwd')`; **did not claim an operating-system root shell**.

**Finding:** unauthenticated remote administrative database access, weak application credential storage, and file-read exposure through the database service.

[Read the Incident 21 report](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident-21-MySQL-Unauthenticated-Root-Access/)

### 02. NFS Root Export Misconfiguration — Incident 20

**Scope:** Metasploitable 2, NFS service on TCP/2049.

- Discovered the NFS service and enumerated exports with `showmount`.
- Found an unrestricted root filesystem export (`/ *`).
- Mounted the remote filesystem on Kali and verified read access to remote system files.
- Compared normal-user access denial with successful privileged reading of `/etc/shadow`.
- Examined `/etc/exports`: `rw,sync,no_root_squash,no_subtree_check`.
- Created and verified a **root-owned proof file inside the remote `/root` directory** using the client root identity.
- Removed the test artifact, unmounted NFS, and verified cleanup.

**Finding:** dangerous combination of broadly accessible exports, filesystem-wide exposure, writable access, and `no_root_squash`.

[Read the Incident 20 report](./Network-Pentesting/Cybersecurity-Incident-Lab/Incident20-NFS-Misconfiguration/)

### 03. Active Directory — Kerberoasting and Privileged Access

**Scope:** isolated Windows domain with a domain controller, workstation clients, and Kali Linux.

- Queried domain DNS SRV records, LDAP data, RPC identity information, users, groups, and service principal names.
- Mapped Kerberos AS/TGS traffic and authentication dependencies.
- Enumerated an SPN-bearing service account from a standard domain-user context.
- Requested service tickets and tested weak credentials offline using password-recovery tooling.
- Validated recovered account permissions through SMB enumeration and administrative-access tests.
- In later authorized exercises, examined privileged remote execution and directory replication permissions, including a scoped DCSync test.

**Finding:** service-account credential weaknesses can lead to significant privilege expansion when combined with excessive rights. Individual reports distinguish ticket retrieval, recovered credentials, verified access, and execution outcomes.

[Explore Active Directory investigations](./Red-Team-Active-Directory/)

---

## Investigation Library

### Active Directory & Windows Authentication

Work in this track covers:

- **Domain discovery:** AD-integrated DNS, domain controllers, SRV records, account and group enumeration.
- **Kerberos:** AS-REQ/AS-REP, pre-authentication, TGT versus TGS, service tickets, and ticket-cache inspection.
- **SMB and RPC:** share enumeration, domain identity mapping, RID/SID interpretation, and authentication/authorization checks.
- **Credential and privilege attack paths:** SPNs, Kerberoasting, offline password testing, administrative access validation, and DCSync permission investigation.
- **Packet evidence:** correlating Wireshark captures with commands executed on Kali and Windows hosts.

[Browse the Active Directory track](./Red-Team-Active-Directory/)

### Linux and Network Service Exploitation

Service-level investigations include:

- **DistCC:** remote code execution, reverse-shell validation, local enumeration, and SUID privilege-escalation testing in the intentionally vulnerable lab.
- **Samba:** anonymous service enumeration, vulnerable configuration identification, exploitation testing, and verification of the resulting execution context.
- **NFS:** exported filesystem discovery, mount behavior, permissions and `no_root_squash` abuse (Incident 20).
- **MySQL:** server handshake analysis, unauthenticated root access, database privilege mapping, credentials, and file-read testing (Incident 21).
- **Supporting enumeration:** FTP, SSH, Telnet, web services, and other identified attack-surface components, documented where tested.

[Browse Network Penetration Testing](./Network-Pentesting/)

### Web Application Penetration Testing

My web security practice includes **manual request inspection and modification**, with particular attention to the distinction between a suspicious response and a verified vulnerability.

- Authentication and access-control tests, including IDOR-style authorization failures.
- SQL injection and database interaction in authorized training environments.
- JWT structure, signatures, verification, and algorithm-related weaknesses.
- Path traversal, unsafe file upload behavior, and command injection exercises.
- Burp Suite Proxy, Repeater, and selected PortSwigger Web Security Academy labs.
- Application-oriented investigations such as the VulnShop training environment, where present in the repository.

[Browse Network and Web Pentesting](./Network-Pentesting/)

### Independent Security Research

These are **experimental investigations**, not necessarily exploitation demonstrations:

**PDF Prompt Injection** — Investigated whether adversarial content embedded in a PDF résumé could alter an AI-based evaluation workflow; compared clean and manipulated inputs and documented observations and limitations.

**Image Steganography Investigation** — Inspected metadata, file structure, and least-significant-bit techniques to examine whether information had been hidden in an image. Distinguished observed evidence from speculation.

These projects emphasize reproducibility, disciplined interpretation, and knowing when evidence does *not* support a conclusion.

[Browse Security Research](./Security-Research/)

### Networking and Packet Analysis

I maintain separate networking exercises to build protocol understanding from first principles:

| Lab area | Investigated concepts |
| --- | --- |
| Switching and local addressing | Ethernet, MAC addresses, ARP, ICMP, same-subnet communication |
| Subnets and default gateways | IPv4 networks, local versus remote traffic, forwarding decisions |
| Inter-network routing | Two routed subnets, router interfaces and gateways |
| Multi-router routing | Point-to-point links, connected routes and static routes |
| Packet-level investigations | TCP handshake, Kerberos, SMB, MySQL greetings and SQL protocol exchanges |

[Browse Networking Labs](./Networking/)

### Linux Terminal and Automation

The Linux work documents practical operations that underpin the security investigations: navigating filesystems, ownership and permissions, processes, shell redirection, pipes, `grep`, `awk`, `find`, service investigation, text processing, and repeatable CLI workflows. Python experiments support selected analysis and automation tasks.

[Browse Linux Terminal Studies](./Linux-Terminal-From-Zero/)

---

## Tools and Protocols in the Lab

| Practice area | Tools and technologies |
| --- | --- |
| Network reconnaissance | Nmap, Linux `ip` utilities, DNS tools, SearchSploit |
| Active Directory | Impacket, LDAP tools, `rpcclient`, `smbclient`, NetExec, native Windows commands |
| Exploitation and validation | Metasploit, Netcat, Linux privilege/permission analysis |
| Web and database testing | Burp Suite, MySQL/MariaDB client, SQL, PortSwigger labs |
| Credential research | John the Ripper, Hashcat, name-that-hash |
| Network forensics | Wireshark, TCP/IP, DNS, Kerberos, SMB, MySQL protocol analysis |
| Programming and environments | Bash, Python, VirtualBox, Cisco Packet Tracer, Git, Markdown |

*Listing a tool means that I have worked with it in a lab; it does not imply expert proficiency or professional certification.*

## Assessment Methodology

```text
  LAB SCOPE & AUTHORIZATION
              |
              v
     DISCOVERY / SCANNING
              |
              v
   ENUMERATION / HYPOTHESIS
              |
              v
      CONTROLLED VALIDATION
              |
              v
  EVIDENCE / PRIVILEGE CHECKS
              |
              v
     IMPACT AND LIMITATIONS
              |
              v
    CLEANUP / REMEDIATION
              |
              v
       TECHNICAL REPORT
```

I distinguish **connection** from **authentication**, **authentication** from **authorization**, and **database-level control** from **operating-system compromise**. Reports aim to record commands, observations, screenshots or packet captures, limits of the evidence, and potential remediation. Training exercises are completed first for understanding, then repeated as needed to gather clear publication-ready evidence.

## Background and Current Focus

My technical background began with early home computing and progressed through computer troubleshooting, operating systems, and web development using technologies including PHP, Ruby, and content-management systems. I hold a **Bachelor's degree in Computer Science** obtained in Italy.

I am currently deepening my practical skills in **Red Team and penetration-testing techniques**, with an emphasis on terminal-based investigation, independent problem solving, networking, and explaining *why* a finding works rather than just executing a tool.

**Current priority:** rigorous internal-network assessments, Active Directory attack paths, Linux services, and web application exploitation within authorized scopes.

---

### Responsible Use and Evidence Standards

All attack techniques in this repository are demonstrated against systems I own or am expressly authorized to test, including deliberately vulnerable machines and isolated virtual networks. Credentials, users, hosts, and attack outcomes are specific to those environments. Where an exercise ends at data access, the report does not imply remote code execution or system administrator access without separate proof.

**Repository:** [cybersecurity-portfolio](https://github.com/frankie79der/cybersecurity-portfolio)
