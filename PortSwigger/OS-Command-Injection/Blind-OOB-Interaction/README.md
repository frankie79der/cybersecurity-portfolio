# Blind OS command injection with out-of-band interaction

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
- The command execution has no visible effect on the application

To detect successful exploitation, an out-of-band interaction is triggered with an external server.


## Vulnerability Type

Blind OS Command Injection

Technique:

Out-of-Band (OOB) Interaction


Out-of-band exploitation is used when:

- The application does not return command output
- There is no visible response difference
- The attacker needs an external interaction as proof of execution


## Vulnerable Functionality

Feature tested:

Feedback submission form


The vulnerable parameter was:

