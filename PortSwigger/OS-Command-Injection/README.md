# OS Command Injection

## PortSwigger Web Security Academy

Category:

OS Command Injection

Completed Labs:

- OS command injection, simple case
- Blind OS command injection with time delays
- Blind OS command injection with output redirection


## Vulnerability Overview

OS Command Injection occurs when an application executes operating system commands using user-controlled input.

An attacker can manipulate parameters that are passed to the system shell and execute arbitrary commands on the server.


Example vulnerable code:

```php
$command = "ping " . $user_input;

system($command);
