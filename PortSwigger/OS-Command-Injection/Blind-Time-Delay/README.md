# Blind OS command injection with time delays

## PortSwigger Web Security Academy

Difficulty:

Practitioner

Status:

Solved


## Lab Description

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing user-controlled input, but the output of the command is not returned in the HTTP response.

The goal is to prove command execution by creating a measurable time delay.


## Vulnerability Type

Blind OS Command Injection

Unlike classic command injection, the attacker cannot directly see the command output.

Instead, exploitation relies on observable side effects:

- Time delays
- External network interactions
- File system changes


## Vulnerable Functionality

Feature tested:

Feedback submission form


The application processes user input from the feedback request and includes it inside a system command.


The vulnerable parameter was:

