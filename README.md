# Cybersecurity Portfolio

## About Me

IT professional with a Computer Science background currently transitioning into cybersecurity, with a strong focus on offensive security, Active Directory, network analysis, and web application security.

My approach is strongly hands-on.

Rather than studying security only at the theoretical level, I build controlled lab environments, reproduce attack paths, analyze authentication protocols, capture network traffic, test vulnerable applications, and document the entire process.

This GitHub portfolio documents that progression.

---

## Featured Technical Areas

### Active Directory & Windows Security

Hands-on work with a multi-VM Active Directory environment including:

- Windows Server Domain Controller
- Windows domain clients
- Active Directory Domain Services
- DNS
- LDAP
- Kerberos
- SMB
- Domain users and groups
- Service Principal Names (SPNs)
- Domain enumeration
- Authentication analysis

I use Kali Linux as the offensive-security workstation for enumeration and attack simulation inside the lab.

---

### Kerberos & Kerberoasting

Practical Active Directory authentication analysis including:

- AS-REQ / AS-REP
- Kerberos pre-authentication
- Ticket Granting Tickets (TGT)
- TGS-REQ / TGS-REP
- Service Tickets
- SPN discovery
- Kerberoasting
- Offline password testing

Tools used include:

- Wireshark
- Impacket
- Hashcat
- Windows native tools such as `klist`, `setspn`, `whoami`, `net user`, `net group`, and `nltest`

Several documented labs follow the full attack and authentication flow from domain-user access through SPN discovery, service-ticket requests, packet analysis, and controlled offline credential testing.

---

### SMB & Network Traffic Analysis

Hands-on packet analysis using Wireshark, including:

- TCP connection establishment
- SMB2 Negotiate
- Session Setup
- Tree Connect
- File Create
- Read / Write operations
- Authentication behavior
- TCP/445 analysis

The goal is not only to use security tools, but to understand what is happening on the network while the tools are running.

---

### Web Application Security

Hands-on training using Burp Suite and PortSwigger Web Security Academy.

Topics studied and practiced include:

- SQL Injection
- Authentication vulnerabilities
- Access Control vulnerabilities
- JWT security
- Path Traversal
- File Upload vulnerabilities
- OS Command Injection
- Cross-Site Scripting (XSS)
- API Security
- Server-Side vulnerabilities

---

### Linux & Offensive Security

Practical Linux and Kali Linux work covering:

- Linux command-line fundamentals
- Filesystem navigation
- System information and processes
- Network inspection
- Service enumeration
- Security tooling
- Vulnerable service analysis

Training environments include intentionally vulnerable systems such as Metasploitable.

Tools used include:

- Kali Linux
- Nmap
- Metasploit
- Burp Suite
- Wireshark
- Impacket
- Hashcat
- Python
- Linux CLI tools

---

## Selected Projects

### Active Directory Offensive Security Lab

Built and maintained a multi-system Active Directory lab for studying domain architecture, authentication, enumeration, and offensive-security techniques.

Key areas include:

- Domain Controller discovery
- DNS SRV queries
- Active Directory enumeration
- User and group discovery
- SPN enumeration
- Kerberos authentication
- SMB authentication
- Packet-level analysis

---

### Kerberos Traffic Analysis

Captured and analyzed complete Kerberos authentication sequences using Wireshark.

Documented:

- AS-REQ
- PREAUTH_REQUIRED
- AS-REQ with pre-authentication
- AS-REP
- TGS-REQ
- TGS-REP

This project connects Windows authentication behavior with the actual packets exchanged between domain clients and the Domain Controller.

---

### Kerberoasting Lab

Created a controlled Active Directory Kerberoasting scenario.

The lab includes:

1. Starting with standard domain-user credentials
2. Enumerating Service Principal Names
3. Identifying a service account
4. Requesting a Kerberos service ticket
5. Capturing the TGS exchange
6. Extracting Kerberos material for offline analysis
7. Performing controlled password testing
8. Documenting the complete attack path

---

### SMB Packet Analysis

Captured and analyzed SMB authentication and file-access traffic.

Topics include:

- TCP/445
- SMB negotiation
- Session authentication
- Share access
- File operations
- Packet sequencing

---

### PortSwigger Web Security Labs

Practical web application security exercises using Burp Suite and PortSwigger Web Security Academy.

| Module | Status |
|---|---|
| Access Control | ✅ Completed |
| Authentication | ✅ Completed |
| JWT | ✅ Completed |
| Path Traversal | ✅ Completed |
| File Upload | ✅ Completed |
| OS Command Injection | ✅ Completed |
| SQL Injection | 🚧 In Progress |

---

## Tools & Technologies

**Offensive Security**

Kali Linux · Burp Suite · Impacket · Metasploit · Hashcat · Nmap

**Network Analysis**

Wireshark · TCP/IP · DNS · SMB · Kerberos · LDAP

**Active Directory**

AD DS · Domain Controllers · DNS · Kerberos · SPNs · Domain Users & Groups · SMB

**Web Security**

Burp Suite · PortSwigger Web Security Academy · SQL Injection · Authentication Testing · Access Control Testing

**Systems**

Windows · Windows Server · Linux · VirtualBox

**Scripting**

Python · Bash / Linux CLI

---

## How I Work

My objective is to understand security mechanisms at multiple levels:

**Tool → Protocol → System → Attack Path**

For example, when studying Kerberos I do not stop at running a tool.

I also analyze:

- what request the tool sends
- which system receives it
- which protocol is being used
- what authentication ticket is created
- what can be observed in Wireshark
- why the attack technique works
- what assumptions and prerequisites are required

This portfolio therefore contains both practical exercises and technical explanations.

---

## Portfolio Structure

Many repositories are organized chronologically.

This is intentional.

They document the progression from fundamentals toward increasingly complex offensive-security topics, including:

**Linux → Networking → Web Security → Vulnerable Systems → Active Directory → Kerberos → SMB → Packet Analysis → Kerberoasting**

Selected repositories represent the strongest projects, while the remaining material documents the broader learning path.

---

## Lab Ethics

All security testing documented in this portfolio was performed in:

- Personally controlled environments
- Intentionally vulnerable systems
- Training platforms
- Authorized cybersecurity laboratories

No techniques documented here were performed against systems without authorization.

---

## Current Focus

Current areas of continued development:

- Active Directory offensive security
- Kerberos attack techniques
- Windows authentication
- Network protocol analysis
- Web application penetration testing
- Offensive-security methodology
- Python security automation
