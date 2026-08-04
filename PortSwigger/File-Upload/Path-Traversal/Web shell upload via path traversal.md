# Web Shell Upload via Path Traversal

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: File Upload Vulnerabilities

Vulnerability Type:
- File Upload
- Path Traversal
- Remote Code Execution (RCE)


## Vulnerability Overview

The application allows users to upload files and stores them inside a dedicated upload directory.

Although PHP execution is disabled inside the avatar directory, the application fails to properly validate the uploaded filename.

By exploiting a path traversal vulnerability in the filename parameter, an attacker can store the uploaded file outside the intended directory, bypassing the execution restrictions.


## Objective

The objective was to upload a PHP web shell into an executable directory and retrieve the contents of:

```text
/home/carlos/secret
```

## Methodology

The avatar upload functionality was analyzed using Burp Suite.

A PHP web shell was first uploaded to determine whether executable files were accepted and how the application handled uploaded content.

The upload request was then modified to investigate whether the destination path could be manipulated.


## Discovery

Uploading a PHP file succeeded without restriction.

However, requesting the uploaded file returned its source code instead of executing it.

This indicated that PHP execution was disabled within the upload directory.

Further analysis of the upload request revealed that the filename supplied by the client influenced the destination path on the server.

Using directory traversal sequences inside the filename parameter allowed the uploaded file to escape the restricted upload directory.


## Exploitation

The original filename:

```text
exploit.php
```

was modified to:

```text
../exploit.php
```

The application attempted to sanitize the traversal sequence by removing it.

To bypass this behavior, the forward slash was URL encoded:

```text
..%2fexploit.php
```

The server decoded the filename after validation, allowing the file to be written outside the avatar directory.

Once uploaded, the web shell became accessible through an executable location:

```http
GET /files/exploit.php
```

The PHP code executed successfully, disclosing Carlos's secret.


## Impact

An attacker can bypass directory restrictions and execute arbitrary server-side code.

Successful exploitation may result in:

- Remote Code Execution (RCE)
- File disclosure
- Sensitive data theft
- Server compromise
- Full application takeover


## Root Cause

The application trusts user-controlled filenames when determining the storage location of uploaded files.

Input validation is performed before URL decoding, allowing encoded traversal sequences to bypass security controls.

Restricting script execution in upload directories is ineffective if attackers can write files outside those directories.


## Remediation

Recommended fixes:

- Ignore user-supplied filenames.
- Generate server-side filenames.
- Normalize and validate file paths before saving files.
- Reject path traversal sequences after URL decoding.
- Store uploaded files outside executable directories.
- Disable script execution for uploaded content.


## Real-World Relevance

Path traversal vulnerabilities are not limited to file downloads.

Upload functionality that trusts client-controlled filenames can allow attackers to write files into unintended locations, bypassing otherwise effective security controls.

This technique has been observed in several real-world web applications where upload directories were protected but adjacent directories remained executable.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- File Upload Testing
- Path Traversal Testing
- URL Encoding
- HTTP Request Manipulation
- Remote Code Execution


## Attack Chain

1. Upload PHP web shell
2. Discover PHP execution is disabled
3. Analyze upload request
4. Inject traversal sequence into filename
5. Bypass filename sanitization using URL encoding
6. Store file outside restricted directory
7. Execute uploaded web shell
8. Retrieve sensitive server files


## Lessons Learned

Securing upload directories alone is not sufficient.

Applications must validate both the uploaded file and its destination path.

User-controlled filenames should never determine where files are stored, and all path normalization should occur before security checks are applied.
