# Blind OS command injection with out-of-band data exfiltration

## PortSwigger Web Security Academy

Difficulty:

Practitioner

Status:

Solved


## Lab Description

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing user-controlled input.

However:

- The command runs asynchronously
- The output is not returned in the HTTP response
- Output redirection is not possible
- No direct communication channel exists between the server and attacker

The vulnerability is exploited using an out-of-band technique to exfiltrate command output through DNS queries.


## Vulnerability Type

Blind OS Command Injection

Technique:

Out-of-Band Data Exfiltration


This technique extends standard OOB exploitation by not only proving command execution, but also extracting command output.


## Vulnerable Functionality

Feature tested:

Feedback submission form


The vulnerable parameter was:
