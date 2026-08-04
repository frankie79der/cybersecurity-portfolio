# File Upload Vulnerabilities

## Overview

File upload vulnerabilities occur when an application fails to properly validate files submitted by users.

Improper validation can allow attackers to upload malicious files, execute arbitrary code, bypass security controls, or overwrite sensitive application resources.

Successful exploitation often leads to Remote Code Execution (RCE), making file upload vulnerabilities among the most critical issues in web applications.

---

## Topics Covered

This section includes practical exercises covering:

- Web Shell Upload
- File Validation Bypass
- Content-Type Validation
- Extension Blacklist Bypass
- Path Traversal
- Polyglot Files
- Race Conditions

---

## Tools Used

- Burp Suite Proxy
- Burp Repeater
- Burp Intruder

---

## Completed Labs

✅ Remote code execution via web shell upload

✅ Web shell upload via Content-Type restriction bypass

✅ Web shell upload via path traversal

✅ Web shell upload via extension blacklist bypass

✅ Web shell upload via obfuscated file extension

✅ Remote code execution via polyglot web shell upload

✅ Web shell upload via race condition

---

## Selected Write-ups

- Web Shell Upload
- Filter Bypass Techniques
- Path Traversal
- Polyglot Upload
- Race Condition
