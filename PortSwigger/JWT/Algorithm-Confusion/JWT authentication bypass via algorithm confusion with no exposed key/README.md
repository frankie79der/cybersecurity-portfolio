# JWT Authentication Bypass via Algorithm Confusion (No Exposed Key)

## Lab

PortSwigger Web Security Academy

Difficulty: Expert

Category:

JWT Vulnerabilities


Vulnerability Type:

- JWT Algorithm Confusion
- RS256 / HS256 Confusion
- Cryptographic Design Flaw
- Authentication Bypass


## Vulnerability Overview

JWT can use different algorithms to sign tokens.

Two common algorithms are:

### RS256

Asymmetric cryptography:

```
Private Key
     |
     | Sign
     v

JWT

     |
     | Verify
     v

Public Key
```


The server signs tokens using a private key and verifies them using the public key.


### HS256

Symmetric cryptography:

```
Secret Key
     |
     | Sign
     v

JWT

     |
     | Verify
     v

Same Secret Key
```


The same secret is used for both signing and verification.


The vulnerability occurs when the server supports both algorithms and incorrectly uses the RSA public key as an HMAC secret.


## Objective

The objective was to forge a JWT token that grants administrator privileges.

Required actions:

Access:

```
/admin
```

Then delete:

```
carlos
```


## Vulnerability Discovery

The application used:

```
RS256
```

for JWT signing.

The server generated tokens containing:

```json
{
    "alg":"RS256"
}
```


However, the verification logic allowed switching the algorithm to:

```json
{
    "alg":"HS256"
}
```


The server then incorrectly treated the RSA public key as an HMAC secret.


## Attack Concept


Normal flow:

```
Private RSA Key
       |
       |
    Sign JWT
       |
       v

JWT RS256


Server verifies with:

Public RSA Key
```


Vulnerable flow:

```
Public RSA Key
       |
       |
Used as HS256 Secret
       |
       v

Forged JWT
```


The attacker can create a valid signature without knowing the private key.


## Methodology

Tools used:

- Burp Suite
- JWT Editor Extension
- Docker sig2n tool


The attack required obtaining the server public key.


## Obtaining the Public Key

Two valid JWT tokens were collected from the server.

Because RSA signatures are mathematically related, two tokens signed with the same RSA key allow recovery of possible public key values.


The tool:

```
port swigger/sig2n
```

was used to calculate possible public keys.


Example:

```
docker run --rm -it portswigger/sig2n <JWT1> <JWT2>
```


The correct X.509 public key was identified by testing the generated tokens.


## Exploitation


A symmetric JWT signing key was created using the recovered RSA public key.


The JWT header was modified:

Before:

```json
{
    "alg":"RS256"
}
```


After:

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


The server accepted the token because it incorrectly used the same key material for both algorithms.


## Attack Chain

```
Obtain valid JWT tokens
          |
          v
Recover public key
          |
          v
Change algorithm RS256 -> HS256
          |
          v
Use public key as HMAC secret
          |
          v
Sign forged JWT
          |
          v
Become administrator
```


## Impact

Algorithm confusion can lead to complete authentication bypass.


Possible consequences:

- Account takeover
- Privilege escalation
- Administrative access
- Unauthorized operations


## Root Cause

The application failed to enforce strict JWT algorithm validation.

The verification process trusted the algorithm specified inside the token header.


Example vulnerable logic:

```
if token.alg == "HS256":
    verify_with_secret()

if token.alg == "RS256":
    verify_with_public_key()
```


The attacker can choose the algorithm.


## Remediation

Recommended fixes:

- Allow only explicitly configured algorithms.
- Never trust the JWT `alg` header.
- Separate RSA and HMAC verification logic.
- Maintain strict key management policies.
- Reject unexpected algorithm changes.


Example:

```
Allowed algorithms:

RS256 only
```


## Comparison With Other JWT Attacks


### alg:none

Problem:

Signature verification disabled.


### JWK Injection

Problem:

Attacker provides verification key.


### JKU Injection

Problem:

Attacker controls key location.


### KID Path Traversal

Problem:

Attacker controls key lookup.


### Algorithm Confusion

Problem:

Server uses the wrong cryptographic algorithm.


## Skills Demonstrated

- JWT Internals
- RSA Cryptography
- HMAC
- Algorithm Validation
- Authentication Bypass
- Burp JWT Analysis


## Lessons Learned

Strong cryptography does not guarantee security.

The application must correctly enforce:

- which algorithm is allowed
- which keys belong to which algorithm
- how verification keys are selected


A secure JWT implementation requires both correct cryptography and correct application logic.
