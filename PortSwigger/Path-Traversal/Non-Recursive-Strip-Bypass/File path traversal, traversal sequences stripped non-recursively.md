# File path traversal, traversal sequences stripped non-recursively

**Difficulty:** 🟡 Practitioner

## Objective

Exploit a Path Traversal vulnerability to retrieve the contents of the `/etc/passwd` file by bypassing a filter that removes traversal sequences.

---

## Vulnerability

The application attempts to prevent Path Traversal by removing `../` sequences from the user input.

However, the filtering is performed only once (non-recursively). By using an obfuscated traversal sequence, the remaining characters are transformed into valid `../` sequences after the filter has been applied.

---

## Tools

- Burp Suite Repeater

---

## Exploitation Steps

1. Intercept the request used to load a product image.
2. Send the request to Burp Repeater.
3. Replace the `filename` parameter with an obfuscated traversal payload.
4. Send the modified request.
5. Observe that the server returns the contents of the target file.

---

## Payload

```http
GET /image?filename=....//....//....//etc/passwd HTTP/1.1
```

---

## Result

The application returned the contents of:

```text
/etc/passwd
```

demonstrating that the input filter could be bypassed because traversal sequences were removed only once.

---

## What I Learned

- Removing dangerous characters is not a reliable security control.
- Non-recursive filtering can often be bypassed using crafted payloads.
- Input validation should canonicalize paths before applying security checks.
- Secure applications should verify the final resolved path instead of filtering user input.
- Burp Suite is useful for testing filter bypass techniques against file access functionality.
