# File path traversal, simple case

**Difficulty:** 🟢 Apprentice

## Objective

Exploit a Path Traversal vulnerability to read the contents of the `/etc/passwd` file.

---

## Vulnerability

The application loads product images based on a user-controlled `filename` parameter without properly validating the supplied path.

By using directory traversal sequences (`../`), it is possible to escape the intended directory and access arbitrary files on the server.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Modify the `filename` parameter to traverse outside the image directory.
4. Request the `/etc/passwd` file.
5. Observe that the server returns the contents of the system file.

---

## Payload

```http
GET /image?filename=../../../etc/passwd HTTP/1.1
```

---

## Result

The application returned the contents of:

```text
/etc/passwd
```

confirming that arbitrary files could be read from the server.

---

## What I Learned

- How Path Traversal vulnerabilities occur.
- Why user-controlled file paths must always be validated.
- How `../` sequences allow navigation through directories.
- How Burp Suite can be used to manipulate file path parameters.
- Why exposing arbitrary files can lead to sensitive information disclosure.
