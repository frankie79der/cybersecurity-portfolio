# File path traversal, traversal sequences blocked with absolute path bypass

**Difficulty:** 🟡 Practitioner

## Objective

Exploit a Path Traversal vulnerability to retrieve the contents of the `/etc/passwd` file, despite traversal sequences being blocked.

---

## Vulnerability

The application blocks classic directory traversal sequences such as `../`, but still accepts absolute file paths.

Instead of escaping directories, an attacker can directly specify the full filesystem path of a sensitive file.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Replace the value of the `filename` parameter with an absolute path.
4. Send the modified request.
5. Observe that the application returns the contents of the target file.

---

## Payload

```http
GET /image?filename=/etc/passwd HTTP/1.1
```

---

## Result

The server returned the contents of:

```text
/etc/passwd
```

showing that blocking traversal sequences alone was not enough to prevent unauthorized file access.

---

## What I Learned

- Blocking `../` is not a complete defense against Path Traversal.
- Absolute paths can bypass weak input validation.
- Applications should validate both relative and absolute file paths.
- User input should never be used directly to access files on the filesystem.
- Burp Suite makes it easy to test different path manipulation techniques.
