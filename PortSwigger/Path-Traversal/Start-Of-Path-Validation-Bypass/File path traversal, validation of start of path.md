# File path traversal, validation of start of path

**Difficulty:** 🟡 Practitioner

## Objective

Exploit a Path Traversal vulnerability to retrieve the contents of the `/etc/passwd` file by bypassing path validation.

---

## Vulnerability

The application validates only that the supplied file path starts with the expected directory (`/var/www/images/`).

However, after passing this initial check, the operating system resolves any traversal sequences (`../`), allowing access to files located outside the intended directory.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Replace the `filename` parameter with a path that begins with the expected directory and then traverses outside of it.
4. Send the modified request.
5. Observe that the application returns the contents of the target file.

---

## Payload

```http
GET /image?filename=/var/www/images/../../../etc/passwd HTTP/1.1
```

---

## Result

The server returned the contents of:

```text
/etc/passwd
```

demonstrating that validating only the beginning of a file path is not sufficient to prevent Path Traversal attacks.

---

## What I Learned

- Checking only the prefix of a file path is an ineffective security control.
- Filesystem path normalization resolves `../` sequences after validation.
- Applications should canonicalize the final path before verifying that it remains inside the intended directory.
- Secure file access must validate the resolved path, not just the user input.
- Burp Suite is useful for testing how applications handle path normalization.
