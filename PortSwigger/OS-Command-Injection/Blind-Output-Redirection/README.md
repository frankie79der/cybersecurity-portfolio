# Blind OS command injection with output redirection

## PortSwigger Web Security Academy

Difficulty:

Practitioner

Status:

Solved


## Lab Description

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing user-controlled input, but the command output is not directly returned in the HTTP response.

To exploit the vulnerability, output redirection is used to write the command result into a file that can later be accessed through the web application.


## Vulnerability Type

Blind OS Command Injection

Technique:

Output Redirection


Unlike standard command injection, the attacker cannot directly see command output.

Instead, the attacker:

1. Executes a command on the server
2. Redirects the output into a writable file
3. Retrieves the generated file through the application


## Vulnerable Functionality

Feature tested:

Feedback submission form


The vulnerable parameter was:

