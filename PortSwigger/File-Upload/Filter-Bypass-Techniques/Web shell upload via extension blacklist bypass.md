# Web Shell Upload via Extension Blacklist Bypass

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: File Upload Vulnerabilities

Vulnerability Type:
- File Upload
- Extension Blacklist Bypass
- Web Server Misconfiguration
- Remote Code Execution (RCE)


## Vulnerability Overview

The application attempts to prevent malicious uploads by blocking files with the `.php` extension.

However, the blacklist only filters specific file extensions and fails to consider how the underlying web server interprets uploaded files.

By uploading a malicious `.htaccess` file, an attacker can instruct Apache to execute files with a custom extension as PHP code, bypassing the blacklist entirely.


## Objective

The objective was to bypass the application's extension blacklist, upload a malicious web shell, execute arbitrary PHP code, and retrieve the contents of:

```text
/home/carlos/secret
```

## Methodology

The avatar upload functionality was analyzed using Burp Suite.

An initial attempt to upload a PHP web shell was rejected because the `.php` extension was blacklisted.

The upload request and server response were then examined to identify the web server technology and determine whether alternative execution paths were available.


## Discovery

The server response identified the application as running on **Apache**.

Because Apache supports per-directory configuration through `.htaccess` files, it was possible to upload a custom configuration file that modified how uploaded files were interpreted.

The following directive was used:

```apache
AddType application/x-httpd-php .l33t
```

This instructed Apache to execute files with the `.l33t` extension as PHP scripts.


## Exploitation

The attack was performed in two stages.

First, a malicious `.htaccess` file containing the custom `AddType` directive was uploaded.

Next, the PHP web shell was renamed from:

```text
exploit.php
```

to:

```text
exploit.l33t
```

Because the blacklist only blocked the `.php` extension, the upload succeeded.

When the uploaded file was requested through the browser:

```http
GET /files/avatars/exploit.l33t
```

Apache executed the file as PHP, allowing arbitrary server-side code execution and disclosure of Carlos's secret.


## Impact

An attacker can bypass file extension restrictions and achieve Remote Code Execution.

Successful exploitation may result in:

- Execution of arbitrary server-side code
- Disclosure of sensitive files
- Complete application compromise
- Full server takeover


## Root Cause

The application relies on an extension blacklist instead of enforcing a strict allowlist.

Additionally, Apache is configured to honor uploaded `.htaccess` files, allowing attackers to redefine how uploaded files are processed.

Filtering file extensions alone is insufficient when server configuration can also influence code execution.


## Remediation

Recommended fixes:

- Use an allowlist of permitted file types.
- Prevent users from uploading `.htaccess` files.
- Disable `AllowOverride` where possible.
- Store uploaded files outside the web root.
- Disable script execution inside upload directories.
- Validate uploaded file contents rather than relying solely on file extensions.


## Real-World Relevance

Blacklists are a common but ineffective defense against malicious file uploads.

Attackers frequently exploit alternative file extensions, server configuration files, or interpreter mappings to bypass extension-based filters.

This lab demonstrates why secure file upload validation must consider both application logic and web server configuration.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- File Upload Testing
- Apache Configuration Analysis
- .htaccess Abuse
- Extension Blacklist Bypass
- Remote Code Execution


## Attack Chain

1. Upload blocked PHP web shell
2. Identify Apache web server
3. Upload malicious `.htaccess`
4. Map a custom extension to the PHP interpreter
5. Upload web shell using the new extension
6. Execute arbitrary PHP code
7. Retrieve sensitive server files


## Lessons Learned

Blocking dangerous file extensions is not sufficient to secure file upload functionality.

Applications must combine strict server-side validation with secure web server configuration to prevent attackers from introducing new executable file types through configuration files such as `.htaccess`.
