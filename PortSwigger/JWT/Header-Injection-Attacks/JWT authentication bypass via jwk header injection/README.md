# JWT Authentication Bypass via JWK Header Injection

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: JWT Vulnerabilities

Vulnerability Type:
- JWT Header Injection
- JWK Injection
- Public Key Trust Abuse
- Authentication Bypass


## Vulnerability Overview

JWT tokens using asymmetric cryptography require a public key to verify signatures.

The JWT header can contain a `jwk` parameter, which allows embedding the public key directly inside the token.

In this lab, the application accepts any public key supplied through the JWT header without verifying whether it comes from a trusted source.

This allows an attacker to generate their own RSA key pair, embed the public key inside the JWT, and create a valid forged token.


## Objective

The objective was to modify and sign a JWT that grants administrator privileges.

Required actions:

Access:

```text
/admin
```

Then delete:

```text
carlos
```


## JWT Asymmetric Authentication

With RSA-based JWT signing:

```
Private Key
     |
     | Sign JWT
     |
     v

JWT Token

     |
     | Verify
     v

Public Key
```

The server normally controls the trusted public key.

The vulnerability occurs when the client can provide the verification key.


## Methodology

The JWT authentication flow was analyzed using:

- Burp Suite
- JWT Editor Extension

The JWT header was inspected for parameters related to key handling.


## Discovery

The application accepted a `jwk` parameter inside the JWT header.

Example:

```json
{
    "alg":"RS256",
    "jwk":{
        "kty":"RSA",
        "n":"public-key-data",
        "e":"AQAB"
    }
}
```

The server used this attacker-controlled key to verify the JWT signature.


## Exploitation

A new RSA key pair was generated.

The JWT payload was modified:

Before:

```json
{
    "sub":"wiener"
}
```

After:

```json
{
    "sub":"administrator"
}
```

The JWT Editor extension was used to embed the generated public key directly into the JWT header.

The resulting header contained:

```json
{
    "alg":"RS256",
    "jwk":{
        "kty":"RSA",
        "n":"...",
        "e":"AQAB"
    }
}
```

The token was signed using the corresponding private key.

Because the server trusted the embedded public key, it accepted the forged administrator token.


## Impact

An attacker can bypass authentication by supplying their own verification key.

Potential consequences:

- Account takeover
- Privilege escalation
- Administrative access
- Unauthorized actions


## Root Cause

The application trusts the `jwk` parameter supplied by the client.

The verification key should never be accepted directly from an untrusted JWT header.

The server must control which public keys are allowed for verification.


## Remediation

Recommended fixes:

- Do not trust embedded JWK values from clients.
- Use server-controlled key stores.
- Validate key identifiers (`kid`) against trusted keys.
- Maintain strict JWT verification policies.
- Reject unexpected JWT header parameters.


## JWK vs JKU

### JWK Injection

The attacker provides the key directly:

```json
{
 "jwk":{
     "public-key"
 }
}
```

### JKU Injection

The attacker provides a URL where the key can be downloaded:

```json
{
 "jku":"https://attacker.com/key.json"
}
```

Both vulnerabilities exist because the application trusts attacker-controlled key material.


## Real-World Relevance

JWT key injection vulnerabilities are dangerous because the cryptographic implementation itself may be correct.

The failure is caused by trusting attacker-controlled metadata during the verification process.


## Tools Used

- Burp Suite
- JWT Editor Extension
- RSA Key Generation
- JWK Analysis


## Skills Demonstrated

- JWT Analysis
- RSA Cryptography
- Header Manipulation
- JWK Understanding
- Authentication Bypass


## Attack Chain

1. Capture JWT
2. Identify JWK support
3. Generate attacker RSA key pair
4. Embed public key in JWT header
5. Modify user claim
6. Sign token with private key
7. Submit forged JWT
8. Access admin functionality


## Lessons Learned

A valid cryptographic signature does not guarantee security if the verification key itself can be controlled by an attacker.

JWT security depends not only on strong algorithms, but also on strict control over trusted keys.
