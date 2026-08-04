# JWT Authentication Bypass via Unverified Signature

## Lab

PortSwigger Web Security Academy

Difficulty: Apprentice

Category: JWT Vulnerabilities

Vulnerability Type:
- JWT Signature Validation Failure
- Authentication Bypass
- Session Manipulation


## Vulnerability Overview

The application uses JSON Web Tokens (JWT) to manage user sessions.

JWT tokens contain authentication information inside their payload. To prevent tampering, the payload should be protected by a cryptographic signature.

In this lab, the server accepts JWT tokens without verifying their signature.

This allows an attacker to modify the token payload and impersonate another user.


## Objective

The objective was to modify the session JWT to gain administrative access to:

```text
/admin
```

and delete the user:

```text
carlos
```


## JWT Structure

A JWT consists of three parts:

```
Header.Payload.Signature
```

Example:

```
xxxxx.yyyyy.zzzzz
```

The payload contains claims such as:

```json
{
    "sub": "wiener"
}
```

where:

- `sub` identifies the authenticated user
- the signature should guarantee that the payload has not been modified


## Methodology

The session mechanism was analyzed using Burp Suite.

After authentication, the session cookie was identified as a JWT token.

The token was decoded using Burp's JWT Inspector functionality.


## Discovery

The JWT payload contained the username:

```json
{
    "sub": "wiener"
}
```

The application used this value to determine the current user.

However, modifying the payload and resending the token was accepted by the server.

This indicated that the server was not validating the JWT signature.


## Exploitation

The original JWT payload:

```json
{
    "sub": "wiener"
}
```

was modified to:

```json
{
    "sub": "administrator"
}
```

The modified token was then sent in the session cookie.

The application accepted the forged token and granted administrative access.


The following endpoint became accessible:

```http
GET /admin
```

The administrator panel allowed deleting the user:

```http
/admin/delete?username=carlos
```


## Impact

An attacker can forge authentication tokens and impersonate arbitrary users.

Potential consequences:

- Account takeover
- Privilege escalation
- Unauthorized administrative actions
- Access to sensitive data


## Root Cause

The application trusts JWT payload data without verifying the cryptographic signature.

JWT payloads are only encoded using Base64URL and can be modified by anyone.

The signature is the mechanism that provides integrity protection.

Without signature verification, attackers can freely modify claims.


## Remediation

Recommended fixes:

- Always verify JWT signatures before trusting claims.
- Reject tokens with invalid signatures.
- Use secure cryptographic algorithms.
- Validate expected claims:
  - issuer (`iss`)
  - audience (`aud`)
  - expiration (`exp`)
  - subject (`sub`)


## Real-World Relevance

JWT vulnerabilities are common in modern web applications and APIs.

A failure to properly validate tokens can allow attackers to bypass authentication completely without needing user credentials.


## Skills Demonstrated

- Burp Suite
- JWT Analysis
- Token Manipulation
- Session Testing
- Authentication Bypass


## Attack Chain

1. Authenticate normally
2. Capture JWT session cookie
3. Decode JWT payload
4. Modify user identity claim
5. Send forged token
6. Access administrator functionality
7. Perform privileged action


## Lessons Learned

JWTs should never be trusted because their contents are readable.

The security of a JWT depends entirely on proper signature verification.

A token that is accepted without verification is equivalent to an attacker-controlled authentication mechanism.
