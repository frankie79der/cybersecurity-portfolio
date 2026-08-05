# File path traversal, validation of file extension with null byte bypass

**Difficulty:** 🟡 Practitioner

## Objective

Exploit a Path Traversal vulnerability to retrieve the contents of the `/etc/passwd` file by bypassing file extension validation.

---

## Vulnerability

The application checks that the supplied filename ends with the expected image extension (such as `.png`).

However, it is vulnerable to a **null byte injection** (`%00`). When the input is processed by the underlying system, the null byte terminates the filename, causing everything after it to be ignored.

As a result, the application validates `passwd%00.png` as an image, while the operating system opens `/etc/passwd`.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Replace the `filename` parameter with a traversal payload followed by a null byte and the expected file extension.
4. Send the modified request.
5. Observe that the application returns the contents of the target file.

---

## Payload

```http
GET /image?filename=../../../etc/passwd%00.png HTTP/1.1
```

---

## Result

The server returned the contents of:

```text
/etc/passwd
```

confirming that the file extension validation was bypassed using a null byte injection.

---

## What I Learned

- File extension validation alone is not a reliable security control.
- Null byte injection can terminate strings before the expected extension is processed.
- Path Traversal and input validation flaws can often be combined to bypass security mechanisms.
- Modern frameworks generally mitigate this issue, but legacy applications may still be vulnerable.
- Burp Suite is effective for testing encoding and validation bypass techniques.
