# Cybersecurity Portfolio

## About Me

IT professional with a Computer Science background transitioning into cybersecurity, with a strong focus on **offensive security, Active Directory, network penetration testing, web application security, and protocol analysis**.

My approach to cybersecurity is strongly hands-on.

Rather than studying security only at the theoretical level, I build controlled lab environments, reproduce attack paths, analyze authentication protocols, inspect network traffic, test intentionally vulnerable systems, and document the complete process.

This repository documents my progression from Linux and networking fundamentals to increasingly advanced offensive-security topics involving **Active Directory, Kerberos, SMB, exploitation, packet analysis, and web application security**.

---

# Featured Projects

## 🔥 Incident 14 — Active Directory Kerberoasting

A complete Kerberoasting scenario performed inside my controlled Active Directory lab.

The exercise begins with access as a standard domain user and follows the attack path through service-account discovery and Kerberos ticket analysis.

### Topics Covered

- Active Directory enumeration
- Domain user discovery
- Service Principal Name (SPN) enumeration
- Service-account identification
- Kerberos TGS requests
- Impacket `GetUserSPNs`
- TGS-REQ / TGS-REP analysis
- Wireshark packet inspection
- Kerberos ticket extraction
- Offline password testing with Hashcat
- Credential validation inside the lab
- Kerberos time-synchronization requirements

### Technologies

**Kali Linux · Windows Server · Active Directory · Kerberos · Impacket · Wireshark · Hashcat**

---

## 🔐 Incident 12 — Kerberos Authentication Analysis

Captured and analyzed the complete Kerberos authentication process inside a Windows Active Directory environment.

The objective was to connect Kerberos theory with the actual packets exchanged between a Windows domain client and the Domain Controller.

### Authentication Flow Analyzed

1. AS-REQ
2. PREAUTH_REQUIRED
3. AS-REQ with pre-authentication
4. AS-REP
5. Ticket Granting Ticket creation
6. TGS-REQ
7. TGS-REP
8. Service Ticket usage

### Tools Used

- Wireshark
- Windows Server
- Active Directory
- `klist`
- Windows domain utilities

This lab helped connect Windows authentication behavior with packet-level network analysis.

---

## 🏢 Active Directory Security Labs

Several incidents in this portfolio focus on building, understanding, enumerating, and testing a Windows Active Directory environment.

### Topics Covered

- Active Directory Domain Services
- Domain Controllers
- Domain users
- Domain groups
- DNS
- LDAP
- Kerberos
- SMB
- Service Principal Names
- Domain enumeration
- Group membership
- Authentication behavior
- Domain Controller discovery

### Windows Commands Used

- `whoami`
- `whoami /user`
- `whoami /groups`
- `hostname`
- `ipconfig`
- `net user /domain`
- `net group /domain`
- `net group "Domain Admins" /domain`
- `net group "Enterprise Admins" /domain`
- `nltest`
- `klist`
- `setspn`

The objective is not simply to memorize commands, but to understand how Active Directory components interact during authentication, discovery, and offensive-security testing.

---

## 🌐 Incident 11 — Active Directory DNS Investigation

Investigated how DNS operates inside an Active Directory environment and how domain systems locate critical infrastructure.

### Topics Covered

- DNS A records
- DNS SRV records
- Domain Controller discovery
- LDAP service discovery
- Active Directory DNS integration
- DNS relationships with Kerberos and LDAP

Example query used during the investigation:

```bash
dig @192.168.42.40 _ldap._tcp.dc._msdcs.redteamlab.local SRV
```

The lab demonstrates how DNS discovery becomes part of the broader Active Directory enumeration and authentication process.

---

# Cybersecurity Incident Lab

The **Cybersecurity Incident Lab** is a chronological series of hands-on investigations documenting my technical progression.

The incident numbering is intentional.

Instead of creating isolated demonstrations, I preserve the learning path from foundational networking concepts toward increasingly complex Active Directory and offensive-security scenarios.

Current structure includes:

```text
Cybersecurity-Incident-Lab
│
├── Incident-1
├── Incident-2
├── Incident-3
├── Incident-4
├── Incident-5
├── Incident-6
├── Incident-7
├── Incident-8
├── Incident-9
├── Incident-10 — Active Directory
├── Incident-11 — DNS Investigation
├── Incident-12 — Kerberos
├── Incident-13 — Active Directory
├── Incident-14 — Kerberoasting
└── Special Incident
```

The incidents document combinations of:

- Lab objectives
- Network configuration
- Investigation methodology
- Commands used
- Security tools
- Screenshots
- Packet captures
- Findings
- Technical explanations
- Troubleshooting
- Lessons learned

---

# Network Penetration Testing

The `Network-Pentesting` section contains the majority of my infrastructure and offensive-security work.

```text
Network-Pentesting
│
├── Cybersecurity-Incident-Lab
│
├── Exploitation-Labs
│   ├── Credential-Attacks
│   ├── Metasploit-Reverse-Shell
│   ├── Metasploitable2-Blind-Assessment
│   ├── Post-Exploitation
│   ├── Vulnerability-Assessment
│   └── Metasploitable2-vsftpd
│
├── MITM-Lab
│
└── Virtual-Lab-Environment
```

Topics explored include:

- Network enumeration
- Host discovery
- Service enumeration
- Vulnerability assessment
- Authentication
- Credential attacks
- Exploitation
- Reverse shells
- Post-exploitation
- Man-in-the-Middle concepts
- Vulnerable services
- Active Directory
- Kerberos
- SMB
- Network traffic analysis

---

# Exploitation Labs

The `Exploitation-Labs` section contains controlled exercises performed against intentionally vulnerable systems.

## Areas Covered

- Credential attacks
- Vulnerability assessment
- Service enumeration
- Metasploit exploitation
- Reverse shells
- Post-exploitation
- Metasploitable 2
- FTP / vsftpd analysis
- Blind assessment methodology

## Tools Used

- Kali Linux
- Nmap
- Metasploit
- Linux command-line tools
- Wireshark

The goal of these labs is to understand the complete process from **discovery to exploitation**, rather than simply executing individual tools.

---

# Active Directory Lab Environment

My Windows security work is performed inside a personally controlled virtual environment.

The lab includes a Windows Server Domain Controller, Windows domain clients, and Kali Linux.

```text
                     Active Directory Lab

                          DC1
                    Windows Server
                    192.168.42.40

                   Active Directory
                         DNS
                       Kerberos
                        LDAP

                          │
                          │
                  redteamlab.local
                          │
              ┌───────────┼───────────┐
              │           │           │
           BOB-PC      ALICE-PC      KALI
          Windows 10   Windows 10   Linux
                                  192.168.42.20

                                   │
                                   │
                          Offensive Security
                             Workstation
```

The lab is used to study how offensive-security techniques interact with actual Windows domain services.

---

# Kerberos

Kerberos is one of the major areas documented in the Active Directory labs.

The authentication process analyzed includes:

```text
User
 │
 │ AS-REQ
 ▼
Domain Controller / KDC
 │
 │ AS-REP
 │ + TGT
 ▼
User
 │
 │ TGS-REQ
 ▼
Domain Controller / KDC
 │
 │ TGS-REP
 │ + Service Ticket
 ▼
User
 │
 │ Service Ticket
 ▼
Target Service
```

Hands-on work includes:

- Ticket Granting Tickets
- Service Tickets
- Kerberos pre-authentication
- AS-REQ
- AS-REP
- TGS-REQ
- TGS-REP
- SPNs
- Kerberoasting
- Wireshark analysis
- `klist`
- Impacket
- Hashcat

The goal is to understand both the attack technique and the authentication mechanism behind it.

---

# SMB & Network Traffic Analysis

Wireshark is used throughout the portfolio to analyze network activity at the protocol level.

SMB analysis includes traffic over TCP port 445 and the sequence of operations involved in accessing Windows network resources.

Typical SMB flow:

```text
TCP Three-Way Handshake
        │
        ▼
SMB2 Negotiate
        │
        ▼
Session Setup
        │
        ▼
Tree Connect
        │
        ▼
Create / Open
        │
        ▼
Read / Write
        │
        ▼
Close
```

Topics investigated include:

- TCP connections
- SMB negotiation
- Authentication
- Session establishment
- Share access
- File creation
- File reading
- File writing
- Connection termination

---

# Protocol Analysis

One of my main learning objectives is understanding what happens on the network while security tools and operating systems communicate.

Protocols analyzed throughout the labs include:

- TCP/IP
- DNS
- HTTP
- HTTPS
- SMB
- SMB2
- Kerberos
- LDAP

Wireshark is used to connect security concepts with actual network traffic.

---

# Web Application Security

The `PortSwigger` section documents hands-on web application security training using **Burp Suite** and the **PortSwigger Web Security Academy**.

```text
PortSwigger
│
├── Access-Control
├── Authentication
├── File-Upload
├── JWT
├── OS-Command-Injection
├── Path-Traversal
└── SQL-Injection
```

## Training Progress

| Module | Status |
|---|---|
| Access Control | ✅ Completed |
| Authentication | ✅ Completed |
| JWT | ✅ Completed |
| Path Traversal | ✅ Completed |
| File Upload | ✅ Completed |
| OS Command Injection | ✅ Completed |
| SQL Injection | 🚧 In Progress |

Additional areas of study include:

- Cross-Site Scripting
- API Security
- Server-Side vulnerabilities
- Authentication weaknesses
- Authorization vulnerabilities

## Tools

- Burp Suite
- PortSwigger Web Security Academy
- Browser Developer Tools
- Kali Linux

The focus is on understanding how web vulnerabilities work, how requests and responses can be manipulated, and how application behavior changes during security testing.

---

# Linux Fundamentals

The `Linux Terminal X Beginners` section documents my Linux command-line progression from the fundamentals onward.

Topics include:

- Filesystem navigation
- Files and directories
- User identity
- System information
- Processes
- Memory
- Permissions
- Networking
- Command-line utilities
- Linux administration fundamentals

Linux skills developed here are applied throughout the offensive-security labs using Kali Linux.

---

# MiniConnect

`MiniConnect` is a Python application project included in the portfolio.

```text
MiniConnect
│
├── screenshots
├── templates
├── README.md
├── app.py
├── init_db.py
└── miniconnect.db
```

The project demonstrates experience beyond security tooling, including:

- Python
- Application structure
- Database interaction
- SQLite
- Templates
- Application logic
- Troubleshooting
- Technical documentation

---

# Tools & Technologies

## Offensive Security

- Kali Linux
- Nmap
- Burp Suite
- Impacket
- Metasploit
- Hashcat

## Active Directory

- Windows Server
- Active Directory Domain Services
- Domain Controllers
- Kerberos
- LDAP
- DNS
- SMB
- Service Principal Names
- Domain users
- Domain groups

## Network Analysis

- Wireshark
- TCP/IP
- DNS
- HTTP / HTTPS
- SMB
- Kerberos
- LDAP

## Web Application Security

- Burp Suite
- PortSwigger Web Security Academy
- SQL Injection
- Authentication Testing
- Access Control Testing
- JWT
- Path Traversal
- File Upload vulnerabilities
- OS Command Injection

## Systems

- Windows
- Windows Server
- Kali Linux
- Linux
- VirtualBox

## Development

- Python
- Bash
- Linux CLI
- SQLite

---

# How I Approach Cybersecurity

My objective is not simply to learn how to execute security tools.

I want to understand the complete chain behind them.

```text
Tool
  │
  ▼
Command
  │
  ▼
Protocol
  │
  ▼
Authentication
  │
  ▼
Operating System / Service
  │
  ▼
Network Traffic
  │
  ▼
Attack Path
```

For example, when studying Kerberoasting, the objective is not simply to execute `GetUserSPNs`.

The complete investigation involves understanding:

- Why a Service Principal Name exists
- How service accounts interact with Kerberos
- Why a domain user can request certain service tickets
- How the Domain Controller processes the request
- What happens during TGS-REQ and TGS-REP
- What can be observed in Wireshark
- Why offline password analysis becomes possible
- What prerequisites the technique requires
- How DNS, LDAP, Kerberos, Active Directory, users, and services interact

This methodology is applied throughout the portfolio.

---

# Learning Progression

This repository intentionally preserves the chronological progression of my cybersecurity studies and hands-on work.

```text
Linux Fundamentals
        │
        ▼
Networking
        │
        ▼
Network Enumeration
        │
        ▼
Vulnerability Assessment
        │
        ▼
Web Application Security
        │
        ▼
Vulnerable Systems
        │
        ▼
Exploitation
        │
        ▼
Windows / Active Directory
        │
        ▼
DNS
        │
        ▼
Kerberos
        │
        ▼
SMB
        │
        ▼
Wireshark Packet Analysis
        │
        ▼
Kerberoasting
```

Older labs remain in the repository because they document the progression that led to the more advanced projects.

The objective is to show not only what I know today, but how that knowledge was built through practical work.

---

# Current Focus

My current areas of continued development include:

- Active Directory offensive security
- Windows authentication
- Kerberos attack techniques
- Service-account security
- Network protocol analysis
- Web application penetration testing
- Offensive-security methodology
- Python security automation

---

# Repository Structure

```text
Cybersecurity-Portfolio
│
├── Linux Terminal X Beginners
│   ├── screenshots
│   └── README.md
│
├── MiniConnect
│   ├── screenshots
│   ├── templates
│   ├── README.md
│   ├── app.py
│   ├── init_db.py
│   └── miniconnect.db
│
├── Network-Pentesting
│   │
│   ├── Cybersecurity-Incident-Lab
│   │   ├── Incident-1
│   │   ├── Incident-2
│   │   ├── Incident-3
│   │   ├── Incident-4
│   │   ├── Incident-5
│   │   ├── Incident-6
│   │   ├── Incident-7
│   │   ├── Incident-8
│   │   ├── Incident-9
│   │   ├── Incident-10 — Active Directory
│   │   ├── Incident-11 — DNS Investigation
│   │   ├── Incident-12 — Kerberos
│   │   ├── Incident-13 — Active Directory
│   │   ├── Incident-14 — Kerberoasting
│   │   └── Special Incident
│   │
│   ├── Exploitation-Labs
│   │   ├── Credential-Attacks
│   │   ├── Metasploit-Reverse-Shell
│   │   ├── Metasploitable2-Blind-Assessment
│   │   ├── Post-Exploitation
│   │   ├── Vulnerability-Assessment
│   │   └── Metasploitable2-vsftpd
│   │
│   ├── MITM-Lab
│   └── Virtual-Lab-Environment
│
└── PortSwigger
    ├── Access-Control
    ├── Authentication
    ├── File-Upload
    ├── JWT
    ├── OS-Command-Injection
    ├── Path-Traversal
    └── SQL-Injection
```

---

# Lab Ethics

All security testing documented in this repository was performed exclusively in:

- Personally controlled lab environments
- Intentionally vulnerable virtual machines
- Authorized cybersecurity training platforms
- Systems specifically configured for security testing

No testing documented in this portfolio was performed against systems without authorization.

---

# Objective

My goal is to transition my existing IT and Computer Science background into professional cybersecurity work, with particular interest in **offensive security and penetration testing**.

This portfolio is intended to demonstrate practical ability rather than simply list technologies on a résumé.

Every major topic documented here represents something I have **configured, tested, analyzed, captured, investigated, or documented in a controlled environment**.
