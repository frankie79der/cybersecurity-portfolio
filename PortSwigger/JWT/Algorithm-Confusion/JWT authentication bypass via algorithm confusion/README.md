# JWT Authentication Bypass via Algorithm Confusion

## Lab

PortSwigger Web Security Academy

Difficulty: Expert

Category:

JWT Vulnerabilities


## Vulnerability Type

- JWT Algorithm Confusion
- RS256 / HS256 Confusion
- Public Key Exposure
- Authentication Bypass


## Vulnerability Overview

JSON Web Tokens can use different cryptographic algorithms.

This lab uses RSA-based JWT signing:

```
RS256
```

RS256 uses asymmetric cryptography:

```
Private Key
      |
      | Sign
      v

JWT Token

      |
      | Verify
      v

Public Key
```


The application correctly uses RSA keys, but the implementation incorrectly allows the algorithm to be changed.

The vulnerability occurs because the server accepts the algorithm specified inside the JWT header and does not enforce the expected signing method.


## Objective

The objective was to forge a JWT token with administrator privileges.

Required actions:

Access:

```
/admin
```

Then delete:

```
carlos
```


## Discovery

The application exposed its public key through:

```
/jwks.json
```


The endpoint returned a JSON Web Key Set:

```json
{
    "keys":[
        {
            "kty":"RSA",
            "n":"...",
            "e":"AQAB"
        }
    ]
}
```


The public key was available without authentication.


## Understanding Algorithm Confusion


Normal RS256 flow:

```
RSA Private Key
       |
       |
    Sign JWT
       |
       v

JWT

       |
       |
RSA Public Key
       |
       v

Verification
```


Vulnerable flow:

```
RSA Public Key
       |
       |
Used as HS256 Secret
       |
       v

Forged JWT
```


The server incorrectly uses the RSA public key as an HMAC secret.


## Exploitation


Tools used:

- Burp Suite
- JWT Editor Extension


### Step 1 - Obtain Public Key


The public key was retrieved from:

```
/jwks.json
```


The JWK object was imported into Burp JWT Editor.


### Step 2 - Convert Public Key


The RSA public key was exported as PEM:

```
-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----
```


The PEM key was Base64 encoded and used as an HMAC secret.


### Step 3 - Modify JWT


The original JWT header:

```json
{
    "alg":"RS256"
}
```


was changed to:

```json
{
    "alg":"HS256"
}
```


The payload was modified:


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


The token was signed using HS256 with the RSA public key as the secret.


## Attack Chain

```
Access JWKS endpoint
          |
          v
Obtain RSA public key
          |
          v
Change RS256 to HS256
          |
          v
Use public key as HMAC secret
          |
          v
Generate forged JWT
          |
          v
Administrator access
```


## Impact

Successful exploitation allows:

- Authentication bypass
- Privilege escalation
- Administrator account access
- Unauthorized actions


## Root Cause

The application failed to enforce a strict JWT algorithm policy.

The server trusted:

```
alg
```

from the JWT header.

An attacker could select a weaker or incompatible algorithm.


## Remediation

Recommended fixes:

- Explicitly define allowed algorithms.
- Never trust the JWT `alg` header.
- Separate RSA and HMAC verification logic.
- Validate key type before verification.
- Do not expose unnecessary key material.


Example:

```
Allowed algorithm:

RS256 only
```


## Comparison With Other JWT Attacks


### Weak Secret

Problem:

The signing key can be brute-forced.


### JWK Injection

Problem:

The attacker supplies the verification key.


### JKU Injection

Problem:

The attacker controls the location of the verification key.


### KID Path Traversal

Problem:

The attacker controls the key lookup.


### Algorithm Confusion

Problem:

The server uses the wrong cryptographic algorithm.


## Tools Used

- Burp Suite
- JWT Editor
- JWKS Analysis
- RSA / HMAC Cryptography


## Skills Demonstrated

- JWT Security Testing
- Cryptographic Analysis
- Algorithm Validation
- Authentication Bypass
- Burp Suite Advanced Usage


## Lessons Learned

Cryptographic algorithms can be secure individually but dangerous when implemented incorrectly.

JWT security requires:

- correct algorithm selection
- correct key handling
- strict verification rules

A valid signature does not always mean a valid authentication token.
