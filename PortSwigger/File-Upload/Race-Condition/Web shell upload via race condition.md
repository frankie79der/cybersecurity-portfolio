# Web Shell Upload via Race Condition

## Lab

PortSwigger Web Security Academy

Difficulty: Expert

Category: File Upload Vulnerabilities

Vulnerability Type:
- Race Condition
- Time Of Check To Time Of Use (TOCTOU)
- File Upload
- Remote Code Execution (RCE)


## Vulnerability Overview

The application performs strong validation on uploaded files.

However, the validation process introduces a race condition because uploaded files are temporarily stored in a web-accessible directory before security checks are completed.

During this short time window, an attacker can access and execute the uploaded file before it is deleted.


## Objective

The objective was to exploit a race condition in the upload process, execute a PHP web shell before validation removed it, and retrieve:

```text
/home/carlos/secret
```

## Methodology

The upload workflow was analyzed using Burp Suite and Turbo Intruder.

Unlike previous upload vulnerabilities, the application correctly rejected malicious files after validation.

The focus was therefore shifted from bypassing validation to exploiting the timing of the validation process.


## Discovery

The upload process followed this sequence:

```
1. Upload file
2. Move file to upload directory
3. Validate file type
4. Delete file if invalid
```

The problem was that the file became available inside the web-accessible directory before validation completed.

During this small time interval, the malicious file could be requested and executed.


## Exploitation

A PHP web shell was prepared:

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

A normal upload request was captured using Burp.

Turbo Intruder was used to send multiple requests simultaneously:

- One request uploaded the malicious PHP file.
- Multiple GET requests attempted to access the file immediately after upload.

The race condition was exploited by reaching the file before the validation process deleted it.

One of the GET requests successfully executed the PHP payload and returned Carlos's secret.


## Impact

A successful race condition attack allows an attacker to bypass file validation controls and execute arbitrary server-side code.

Potential consequences include:

- Remote Code Execution
- Sensitive information disclosure
- Server compromise
- Complete application takeover


## Root Cause

The application temporarily stores uploaded files in an executable, publicly accessible directory before validation is completed.

Security checks occur after the file has already become available to users.

This creates a Time Of Check To Time Of Use (TOCTOU) vulnerability.


## Remediation

Recommended fixes:

- Perform validation before moving files into publicly accessible directories.
- Store uploaded files in temporary non-public locations.
- Rename and move files only after successful validation.
- Disable script execution in upload directories.
- Use atomic file operations where possible.
- Avoid exposing temporary processing states to users.


## Real-World Relevance

Race conditions are difficult vulnerabilities because the application logic may appear secure when analyzed step-by-step.

However, attackers can exploit timing differences between operations to access resources during unsafe intermediate states.

TOCTOU vulnerabilities are especially relevant in file processing systems, upload handlers, and applications performing asynchronous validation.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- Turbo Intruder
- Race Condition Testing
- File Upload Analysis
- TOCTOU Vulnerabilities
- Remote Code Execution


## Attack Chain

1. Analyze upload validation workflow
2. Identify temporary file exposure
3. Prepare malicious web shell
4. Synchronize upload and access requests
5. Exploit validation timing gap
6. Execute PHP code
7. Retrieve sensitive information


## Lessons Learned

Security controls must protect the entire lifecycle of an operation, not only individual steps.

A file that is eventually deleted can still be dangerous if attackers can access it during an unsafe intermediate state.

Race conditions require analyzing not only what the application does, but also when each operation happens.
