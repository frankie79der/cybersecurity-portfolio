# Remote Code Execution via Web Shell Upload

## Lab

PortSwigger Web Security Academy

Difficulty: Apprentice

Category: File Upload Vulnerabilities

Vulnerability Type:
- Unrestricted File Upload
- Web Shell Upload
- Remote Code Execution (RCE)


## Vulnerability Overview

The application allows users to upload avatar images without performing any server-side validation.

Because uploaded files are stored inside a web-accessible directory and executed by the PHP interpreter, an attacker can upload a malicious PHP web shell and execute arbitrary server-side code.


## Objective

The objective was to upload a PHP web shell, execute it on the server, and retrieve the contents of the file:

```text
/home/carlos/secret
```

## Methodology

The avatar upload functionality was analyzed using Burp Suite.

A legitimate image upload was first performed to understand where uploaded files were stored and how they were later accessed by the application.

Once the upload workflow was understood, a PHP web shell was uploaded in place of an image.


## Discovery

Uploading a normal avatar revealed that uploaded files were stored inside the following directory:

```text
/files/avatars/
```

The uploaded file could be accessed directly through the browser using a predictable URL.

No validation was performed on the uploaded file type or extension.


## Exploitation

A PHP file containing server-side code was created and uploaded through the avatar upload functionality.

Example payload:

```php
<?php
echo file_get_contents('/home/carlos/secret');
?>
```

After the upload completed successfully, the uploaded file was requested directly:

```http
GET /files/avatars/exploit.php
```

Instead of downloading the file, the server executed the PHP code and returned the contents of Carlos's secret file.


## Impact

An attacker can execute arbitrary PHP code on the server.

Successful exploitation may lead to:

- Remote Code Execution (RCE)
- File disclosure
- Sensitive data theft
- Server compromise
- Full application takeover


## Root Cause

The application performs no server-side validation of uploaded files.

Additionally, uploaded files are stored in a directory where the web server executes PHP code.

Allowing executable files to be uploaded and executed creates a direct path to Remote Code Execution.


## Remediation

Recommended fixes:

- Validate uploaded file types on the server side.
- Verify both MIME type and file contents.
- Store uploaded files outside the web root.
- Disable execution permissions in upload directories.
- Generate random filenames.
- Allow only explicitly approved file extensions.


## Real-World Relevance

File upload vulnerabilities remain one of the most critical web application security issues.

Applications that improperly validate uploaded files can unintentionally provide attackers with remote code execution capabilities.

Modern penetration tests frequently include file upload testing because successful exploitation often results in complete compromise of the target application.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- HTTP Request Analysis
- File Upload Testing
- PHP Web Shell Deployment
- Remote Code Execution
- Server-Side Security Testing


## Lessons Learned

A file upload feature should never trust files provided by users.

Proper validation must occur on the server side, and uploaded files should never be stored in locations where they can be executed by the web server.

Preventing code execution is just as important as validating the uploaded file itself.

## Attack Chain

1. Identify upload functionality
2. Upload malicious PHP file
3. Locate uploaded file
4. Execute uploaded web shell
5. Achieve Remote Code Execution
6. Read sensitive server files
