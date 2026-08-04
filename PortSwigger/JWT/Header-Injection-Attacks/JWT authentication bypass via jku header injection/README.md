# JWT Authentication Bypass via JKU Header Injection

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: JWT Vulnerabilities

Vulnerability Type:
- JWT Header Injection
- JKU Injection
- Authentication Bypass
- Public Key Trust Abuse


## Vulnerability Overview

JSON Web Tokens can use asymmetric cryptography, where a private key signs the token and a public key verifies it.

JWT headers can contain a `jku` parameter:

```json
{
    "jku": "https://example.com/jwks.json"
}
```

This specifies the location of a JSON Web Key Set containing the public key used for verification.

In this lab, the application trusts any URL supplied in the `jku` header without verifying that the key comes from a trusted source.

This allows an attacker to provide their own public key and forge a valid JWT.


## Objective

The objective was to create a forged JWT that grants administrator privileges.

Required actions:

Access:

```text
/admin
```

Then delete:

```text
carlos
```


## JWT Asymmetric Signing

Unlike HS256, asymmetric algorithms use two keys:

```
Private Key
     |
     | Sign JWT
     |
     v

JWT Token

     |
     | Verify using
     v

Public Key
```

The server only needs the public key to verify the signature.


## Methodology

The JWT authentication mechanism was analyzed using:

- Burp Suite
- JWT Editor Extension

The JWT header was inspected for parameters controlling key retrieval.


## Discovery

The JWT header supported the `jku` parameter.

Example:

```json
{
    "alg": "RS256",
    "jku": "https://attacker-controlled-server/jwks.json"
}
```

The application automatically downloaded the public key from the supplied URL.

However, it did not verify whether the URL belonged to a trusted domain.


## Exploitation

A new RSA key pair was generated.

The public key was hosted on the exploit server as a JWK Set:

```json
{
    "keys": [
        {
            "kty": "RSA",
            "kid": "example-key-id",
            "n": "...",
            "e": "AQAB"
        }
    ]
}
```

The JWT header was modified:

Before:

```json
{
    "alg": "RS256"
}
```

After:

```json
{
    "alg": "RS256",
    "kid": "attacker-key-id",
    "jku": "https://attacker-server/jwks.json"
}
```

The payload was changed:

```json
{
    "sub": "administrator"
}
```

The token was signed using the attacker-controlled private key.

The server downloaded the attacker's public key and accepted the forged signature.


## Impact

An attacker can create valid authentication tokens without access to the application's private keys.

Potential consequences:

- Authentication bypass
- Account takeover
- Privilege escalation
- Unauthorized administrative access


## Root Cause

The application trusts user-controlled JWT header parameters.

The `jku` value should never be used directly without validation.

The server must maintain a trusted list of allowed key locations.


## Remediation

Recommended fixes:

- Never trust arbitrary `jku` URLs.
- Use a fixed list of trusted key locations.
- Validate the `kid` parameter.
- Avoid dynamic key retrieval when unnecessary.
- Implement strict JWT verification policies.


## Real-World Relevance

JKU injection is dangerous because the JWT signature itself is not broken.

The cryptographic algorithm works correctly.

The vulnerability exists because the application trusts attacker-controlled metadata that tells it where to obtain the verification key.


## Tools Used

- Burp Suite
- JWT Editor Extension
- RSA Key Generation
- JWK/JWKS Analysis


## Skills Demonstrated

- JWT Analysis
- RSA Key Handling
- Header Manipulation
- JWK/JWKS Understanding
- Authentication Bypass


## Attack Chain

1. Capture JWT token
2. Identify `jku` support
3. Generate attacker RSA key pair
4. Host public key as JWK Set
5. Inject malicious `jku` URL
6. Modify JWT claims
7. Sign token with private key
8. Access administrator functionality


## Lessons Learned

JWT headers are user-controlled input.

Even when cryptographic signatures are correctly implemented, trusting attacker-controlled key sources can completely compromise authentication.

Secure JWT validation requires controlling both the cryptographic process and the source of verification keys.
