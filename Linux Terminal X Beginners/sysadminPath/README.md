# SysadminPath — Understanding Systems from Both Sides

### Linux Administration · System Investigation · Offensive Security Foundations

## Overview

**To understand how to compromise a system, you must first understand how that system works.**

SysadminPath is a growing collection of visual references, command workflows, and practical knowledge developed through hands-on Linux system administration and troubleshooting labs.

The project explores an important connection between **system administration and offensive cybersecurity**: many of the same tools used to maintain and troubleshoot systems are also essential during penetration testing, reconnaissance, and post-exploitation analysis.

The difference is not simply the tools being used, but the **objective, authorization, and context** in which they are applied.

## The Shared Technical Foundation

System administrators investigate processes, services, network connections, file permissions, and system logs to maintain reliable and secure infrastructure.

Penetration testers rely on the same technical knowledge to understand system behavior, identify weaknesses, assess privileges, and evaluate potential attack paths within authorized environments.

For example:

| Linux Tool | System Administration | Offensive Security |
|---|---|---|
| `ps`, `htop` | Monitor running processes | Investigate processes and execution context |
| `systemctl` | Manage system services | Identify active services and their configurations |
| `journalctl` | Troubleshoot system errors | Analyze events and execution traces |
| `ss` | Inspect network connections | Identify listening ports and network activity |
| `ip` | Inspect network interfaces | Understand network exposure and connectivity |
| `chmod`, `chown` | Manage file permissions | Evaluate access controls and privilege boundaries |
| `grep`, `awk` | Search and process logs | Extract relevant security evidence |
| `curl` | Test HTTP services | Inspect web responses and application behavior |

**The commands are tools. Understanding their implications is the real skill.**

## What You'll Find Here

This directory contains visual learning materials covering:

- Linux processes, PID/PPID relationships, and process ownership
- System services and troubleshooting workflows
- Network sockets, listening ports, and connections
- File permissions and access control
- System logs and event investigation
- HTTP service diagnostics
- Practical investigation workflows connecting multiple Linux commands

Each diagram is designed to connect individual commands into a coherent investigation process rather than present isolated command lists.

## Learning Philosophy

My approach is based on a simple progression:

**Understand the system → Investigate its behavior → Identify weaknesses → Validate findings → Document evidence**

Before relying on advanced offensive tools or automated exploitation frameworks, I want to understand the underlying operating system well enough to investigate problems manually.

This project documents that foundation.

## Purpose

SysadminPath is not intended to replace formal system administration training or act as an exhaustive Linux reference.

It is a continuously evolving technical knowledge base supporting my journey toward **Red Team Operations and Penetration Testing**.

All security testing is intended for authorized laboratory environments.

---

*Learn how systems work. Understand how they fail. Know how to investigate both.*
