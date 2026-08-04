# Remote Code Execution via Polyglot Web Shell Upload

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: File Upload Vulnerabilities

Vulnerability Type:
- File Upload
- Polyglot File
- Content Validation Bypass
- Remote Code Execution (RCE)


## Vulnerability Overview

The application attempts to protect its file upload functionality by validating the contents of uploaded files to ensure they are legitimate images.

However, the validation only checks whether the file contains valid image data and does not prevent additional server-side code from being embedded inside the file.

By creating a polyglot file containing both valid image data and PHP code, an attacker can bypass content validation and achieve Remote Code Execution.


## Objective

The objective was to upload a PHP web shell disguised as a valid image file and execute server-side code to retrieve:

```text
/home/carlos/secret
```

## Methodology

The avatar upload functionality was analyzed using Burp Suite.

Previous bypass techniques such as changing extensions or modifying content types were tested but blocked by the application's image validation mechanism.

The focus was then shifted toward understanding how the application validated uploaded files.


## Discovery

The application successfully rejected normal PHP uploads and verified that uploaded files were valid images.

However, image formats often support additional metadata fields.

This allowed PHP code to be embedded inside image metadata while preserving the file's valid image structure.

The resulting file became a polyglot:

```
Valid JPG Image
        +
Embedded PHP Code
```

The file could satisfy image validation while still containing executable server-side instructions.


## Exploitation

A PHP payload was embedded into the metadata of a valid JPG image.

Example payload:

```php
<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>
```

The modified image was saved with a PHP extension:

```text
polyglot.php
```

The file was uploaded successfully because the application recognized the content as a valid image.

When the uploaded file was requested:

```http
GET /files/avatars/polyglot.php
```

the server processed the embedded PHP code and returned the contents of Carlos's secret file.


## Impact

An attacker can bypass file content validation and execute arbitrary server-side code.

Potential consequences include:

- Remote Code Execution
- Sensitive data exposure
- Server compromise
- Application takeover


## Root Cause

The application relies only on checking whether the uploaded file contains valid image data.

However, file format validation does not guarantee that the file is safe.

Certain formats allow metadata or additional content that can contain executable code.

Furthermore, uploaded files are stored in a location where the server executes PHP.


## Remediation

Recommended fixes:

- Never allow uploaded files to be executed by the web server.
- Store uploaded files outside the web root.
- Re-encode images server-side instead of trusting uploaded files.
- Remove unnecessary metadata from uploaded images.
- Use strict allowlists for file types.
- Validate both content and storage location.


## Real-World Relevance

Polyglot files demonstrate why file validation is a complex security problem.

Attackers often combine multiple techniques to bypass upload restrictions, including valid file structures, metadata abuse, and server-side execution flaws.

Checking only the file signature or MIME type is not sufficient protection against malicious uploads.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- File Upload Testing
- Image Metadata Analysis
- Polyglot File Creation
- Content Validation Bypass
- Remote Code Execution


## Attack Chain

1. Identify upload functionality
2. Test standard PHP upload
3. Discover content validation
4. Create valid image with embedded PHP payload
5. Upload polyglot file
6. Access uploaded file
7. Execute server-side code
8. Retrieve sensitive information


## Lessons Learned

A file that appears to be a legitimate image can still contain executable code.

Secure upload handling requires more than checking file extensions or file signatures. Applications must control where uploaded files are stored and ensure that uploaded content can never be executed.
