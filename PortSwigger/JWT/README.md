# JWT Vulnerabilities

## Overview

JSON Web Tokens (JWT) are widely used for authentication and authorization in modern web applications and APIs.

JWT vulnerabilities often occur when applications incorrectly validate tokens, trust user-controlled fields, or implement cryptographic verification incorrectly.

A successful JWT attack can allow attackers to modify claims, bypass authentication, or impersonate other users.


## Topics Covered

This section includes practical exercises covering:

- JWT Structure Analysis
- Signature Validation
- Weak Signing Keys
- JWK Injection
- JKU Injection
- KID Path Traversal
- Algorithm Confusion


## Tools Used

- Burp Suite
- Burp Decoder
- JWT Editor Extension


## Completed Labs

✅ JWT authentication bypass via unverified signature

✅ JWT authentication bypass via flawed signature verification

✅ JWT authentication bypass via weak signing key

✅ JWT authentication bypass via jwk header injection

✅ JWT authentication bypass via jku header injection

✅ JWT authentication bypass via kid header path traversal

✅ JWT authentication bypass via algorithm confusion

✅ JWT authentication bypass via algorithm confusion with no exposed key


## Selected Write-ups

- Signature Validation Flaws
- Weak Signing Keys
- JWT Header Injection
- Algorithm Confusion
