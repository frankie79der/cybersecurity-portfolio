# Offensive Security | Cybersecurity Portfolio

**Active Directory Security · Network Penetration Testing · Web Application Security · Linux**

## About Me

I am an IT professional with a Computer Science background, transitioning into offensive cybersecurity with a focus on penetration testing and Red Team operations.

I develop my technical skills through hands-on work in self-hosted virtual laboratories, deliberately vulnerable systems, and web security training environments.

My work focuses on understanding not only **how an attack technique is performed**, but also **why it works, what conditions make it possible, and how to verify the result**.

This repository contains my practical investigations, security labs, technical documentation, and application development projects.

---

## Featured Security Projects

### 1. Active Directory — Kerberoasting Investigation

**Focus:** Active Directory enumeration, Kerberos authentication, service accounts, and credential exposure.

A controlled laboratory investigation of the Kerberoasting attack path, starting from a standard domain user account.

**Technical activities:**
- Enumerating domain users and Service Principal Names (SPNs)
- Identifying service accounts
- Requesting Kerberos service tickets with Impacket
- Analyzing TGS-REQ and TGS-REP traffic in Wireshark
- Performing offline password testing
- Validating credentials within the lab environment

**Tools:** Kali Linux, Windows Server, Active Directory, Impacket, Wireshark, Hashcat

**[Explore Active Directory Investigations](Network-Pentesting/Cybersecurity-Incident-Lab)**

### 2. Kerberos — Authentication and Packet Analysis

**Focus:** Understanding Windows authentication through real network traffic.

Captured and investigated Kerberos authentication exchanges between Windows domain clients and a Domain Controller.

**Technical activities:**
- Analyzing AS-REQ and AS-REP exchanges
- Investigating Kerberos pre-authentication
- Analyzing TGS-REQ and TGS-REP exchanges
- Examining service-ticket requests
- Correlating protocol traffic with Windows authentication behavior
- Inspecting authentication events with Wireshark and `klist`

**Tools:** Wireshark, Windows Server, Active Directory, Kerberos, Windows command-line utilities

**[Explore Kerberos and Active Directory Labs](Network-Pentesting/Cybersecurity-Incident-Lab)**

### 3. Network Penetration Testing — Vulnerable Linux Environments

**Focus:** Reconnaissance, vulnerability investigation, exploitation, and Linux enumeration.

Hands-on exercises against intentionally vulnerable systems, including Metasploitable 2.

**Technical activities:**
- TCP port scanning and service identification
- Enumerating exposed network services
- Investigating service versions and potential vulnerabilities
- Testing authentication and service configurations
- Practicing exploitation and reverse-shell concepts
- Exploring Linux post-exploitation and system enumeration
- Processing scan results using Linux command-line tools

**Tools:** Kali Linux, Nmap, Metasploit, Netcat, Bash, Linux CLI

**[Explore Network Exploitation Labs](Network-Pentesting/Exploitation-Labs)**

---

## Web Application Penetration Testing

Practical web security training using **PortSwigger Web Security Academy** and **Burp Suite**.

Areas covered in documented labs include:

- Authentication vulnerabilities
- Access control weaknesses
- JSON Web Token (JWT) security
- SQL Injection
- OS Command Injection
- Path Traversal
- File Upload vulnerabilities

My training includes examining HTTP requests and responses, modifying parameters, investigating application behavior, and reproducing security weaknesses in authorized environments.

The repository distinguishes completed training exercises from topics that are still being developed and reinforced.

**[Explore Web Security Labs](PortSwigger)**

---

## Technical Skills and Tools

| Area | Practical Experience |
|---|---|
| Network Reconnaissance | Nmap, service enumeration, TCP/IP, Linux networking |
| Active Directory | Domain enumeration, Kerberos, LDAP, DNS, SMB, SPNs |
| Offensive Security | Impacket, Metasploit, credential testing, controlled exploitation |
| Web Security | Burp Suite, HTTP analysis, authentication and access control testing |
| Traffic Analysis | Wireshark, Kerberos exchanges, SMB traffic |
| Operating Systems | Kali Linux, Ubuntu Linux, Windows, Windows Server |
| Scripting and Development | Python, Bash, SQLite, Linux text processing |
| Virtualization | VirtualBox, isolated multi-machine lab environments |

These skills reflect practical laboratory experience and ongoing technical development.

---

## Application Development — MiniConnect

Alongside my offensive-security labs, I maintain **MiniConnect**, a Python application project.

The project involves:

- Python application logic
- SQLite database interaction
- HTML templates
- Application structure and troubleshooting
- Technical documentation

Working with application code provides additional context for understanding how software handles input, authentication, and data.

**[Explore MiniConnect](MiniConnect)**

---

## Laboratory Environment

My work is performed in controlled virtual environments built for cybersecurity research and technical training.

The environment includes:

- Kali Linux as an offensive-security workstation
- Windows Server with Active Directory Domain Services
- Windows domain-joined clients
- Linux virtual machines
- Intentionally vulnerable systems
- Isolated virtual networks for testing network services and authentication protocols

These environments allow me to investigate security behavior at the operating-system, application, and network-protocol levels.

---

## Repository Navigation

| Section | Contents |
|---|---|
| [Network Penetration Testing](Network-Pentesting) | Active Directory, network exploitation, vulnerable systems, protocol analysis |
| [Cybersecurity Incident Lab](Network-Pentesting/Cybersecurity-Incident-Lab) | Chronological investigations, including Kerberos and Kerberoasting |
| [Exploitation Labs](Network-Pentesting/Exploitation-Labs) | Service enumeration, vulnerability testing, exploitation exercises |
| [PortSwigger Web Security Labs](PortSwigger) | Web application security training and lab documentation |
| [Linux Terminal Fundamentals](Linux%20Terminal%20X%20Beginners) | Linux commands, system administration basics, command-line practice |
| [MiniConnect](MiniConnect) | Python application development project |

The chronological incident documentation is intentionally preserved as a technical learning record. The featured projects above provide a faster entry point to the most relevant offensive-security work.

---

## Current Direction

My goal is to develop into a capable **penetration tester and Red Team professional**, with particular emphasis on:

- Independent vulnerability discovery and validation
- Active Directory and internal network security assessments
- Web application penetration testing
- Linux exploitation and privilege escalation
- Python and Bash automation
- Technical reporting supported by reproducible evidence

I am continuing to strengthen both my technical foundations and my ability to conduct structured assessments independently.

---

**All security testing documented in this repository is performed in controlled, authorized laboratory environments.**
