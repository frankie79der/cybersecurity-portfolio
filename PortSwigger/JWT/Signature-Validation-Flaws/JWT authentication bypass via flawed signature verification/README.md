# JWT Authentication Bypass via Flawed Signature Verification

## Lab

PortSwigger Web Security Academy

Difficulty: Apprentice

Category: JWT Vulnerabilities

Vulnerability Type:
- JWT Signature Validation Failure
- Algorithm None Attack
- Authentication Bypass


## Vulnerability Overview

The application uses JSON Web Tokens (JWT) for session management.

JWT tokens normally contain a cryptographic signature that prevents attackers from modifying the token payload.

In this lab, the server is configured to incorrectly accept unsigned JWT tokens by allowing the `none` algorithm.

This allows an attacker to remove the signature completely and forge a valid authentication token.


## Objective

The objective was to modify the session token, access:

```text
/admin
```

and delete:

```text
carlos
```


## JWT Structure

A JWT consists of:

```
Header.Payload.Signature
```

Example:

```
xxxxx.yyyyy.zzzzz
```

The header defines how the token is signed:

```json
{
    "alg": "RS256",
    "typ": "JWT"
}
```

The `alg` value tells the server which cryptographic algorithm should be used for verification.


## Methodology

The session token was analyzed using Burp Suite.

The JWT payload contained the authenticated user:

```json
{
    "sub": "wiener"
}
```

The goal was to modify the token to impersonate the administrator account.


## Discovery

The application accepted JWTs using the `none` algorithm.

The JWT header was modified from:

```json
{
    "alg": "RS256"
}
```

to:

```json
{
    "alg": "none"
}
```

The server incorrectly trusted this unsigned token format.


## Exploitation

The JWT payload was modified:

Before:

```json
{
    "sub": "wiener"
}
```

After:

```json
{
    "sub": "administrator"
}
```

The JWT header was changed:

Before:

```json
{
    "alg": "RS256"
}
```

After:

```json
{
    "alg": "none"
}
```

The signature section was removed:

```
header.payload.signature
```

became:

```
header.payload.
```

The forged token was accepted by the application, granting administrator access.


## Impact

An attacker can create valid-looking authentication tokens without knowing any cryptographic keys.

Potential consequences:

- Authentication bypass
- User impersonation
- Privilege escalation
- Administrative access


## Root Cause

The application incorrectly trusts the JWT algorithm specified inside the token header.

The attacker controls the JWT header and can request insecure algorithms.

The `none` algorithm disables signature verification entirely.

JWT libraries must explicitly reject unsigned tokens unless there is a legitimate use case.


## Remediation

Recommended fixes:

- Disable the `none` algorithm.
- Enforce a server-side list of allowed algorithms.
- Never trust the algorithm specified by the client.
- Always verify JWT signatures.
- Validate JWT claims after successful verification.


## Real-World Relevance

Algorithm confusion and insecure JWT configurations have historically caused authentication bypass vulnerabilities.

JWT headers are user-controlled input and must always be treated as untrusted data.


## Skills Demonstrated

- Burp Suite
- JWT Manipulation
- JWT Header Analysis
- Algorithm Validation Testing
- Authentication Bypass


## Attack Chain

1. Capture JWT session token
2. Decode JWT structure
3. Modify user claim
4. Change signing algorithm to `none`
5. Remove signature
6. Submit forged token
7. Access administrator functionality


## Lessons Learned

The JWT header is not trusted metadata.

If an application allows the client to choose the verification algorithm, the authentication mechanism can be completely bypassed.

A JWT is secure only when the server strictly controls and validates the cryptographic process.
