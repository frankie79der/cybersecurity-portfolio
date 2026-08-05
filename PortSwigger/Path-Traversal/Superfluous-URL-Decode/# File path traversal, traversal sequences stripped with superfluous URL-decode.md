# File path traversal, traversal sequences stripped with superfluous URL-decode

**Difficulty:** 🟡 Practitioner

## Objective

Exploit a Path Traversal vulnerability to retrieve the contents of the `/etc/passwd` file by abusing multiple URL decoding.

---

## Vulnerability

The application checks the input for traversal sequences before performing URL decoding.

Because the input is decoded after validation, an attacker can double URL-encode the `/` character so that the dangerous sequence is hidden during validation but reconstructed before the file is accessed.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Replace the `filename` parameter with a double URL-encoded traversal payload.
4. Send the modified request.
5. Observe that the application returns the contents of the target file.

---

## Payload

```http
GET /image?filename=..%252f..%252f..%252fetc/passwd HTTP/1.1
```

---

## Result

The server returned the contents of:

```text
/etc/passwd
```

showing that the validation was bypassed because the application decoded the input after checking it.

---

## What I Learned

- Input validation must occur after all decoding operations.
- Double URL encoding is a common technique for bypassing weak filters.
- The order of validation and decoding is critical for application security.
- Canonicalizing user input before applying security checks helps prevent these bypasses.
- Burp Suite makes it easy to test encoded payloads against web applications.
