# OS command injection, simple case

## PortSwigger Web Security Academy

Difficulty:

Apprentice

Status:

Solved


## Lab Description

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-controlled input and returns the raw command output in the HTTP response.


## Vulnerability Type

OS Command Injection

The application passes user-controlled parameters directly into an operating system command without proper validation or sanitization.


## Vulnerable Functionality

Feature tested:

Product stock checker


The application receives:

- Product ID
- Store ID


and uses these values inside a shell command.


Example vulnerable behavior:

