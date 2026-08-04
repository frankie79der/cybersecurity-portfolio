# JWT Authentication Bypass via Weak Signing Key

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: JWT Vulnerabilities

Vulnerability Type:
- Weak Cryptographic Secret
- JWT Signature Forgery
- Authentication Bypass
- Offline Brute Force


## Vulnerability Overview

The application uses JSON Web Tokens (JWT) for session management.

The tokens are signed using a secret key to prevent tampering.

In this lab, the application uses an extremely weak signing key that can be discovered through offline brute force.

Once the secret key is recovered, an attacker can generate valid JWT signatures and impersonate other users.


## Objective

The objective was to:

1. Recover the JWT signing secret.
2. Create a forged administrator token.
3. Access:

```text
/admin
```

4. Delete:

```text
carlos
```


## JWT Signing

JWT tokens can use symmetric algorithms such as:

```
HS256
```

With symmetric signing:

```
Same secret
     |
     +---- Sign JWT
     |
     +---- Verify JWT
```

The security of the system depends entirely on the secrecy and complexity of this key.


## Methodology

The session token was captured using Burp Suite.

The JWT was analyzed to identify:

- Algorithm
- Payload claims
- Signature

The token was then tested for weak signing secrets.


## Discovery

The JWT was signed using a weak secret key.

Instead of a strong random secret, the application used a common password-like value.

The signing secret was recovered through offline brute force using Hashcat:

```bash
hashcat -a 0 -m 16500 <JWT> jwt.secrets.list
```

The recovered secret was:

```text
secret1
```


## Exploitation

After obtaining the signing secret, a valid JWT could be generated.

The payload was modified:

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

The token was then re-signed using the recovered secret.

Because the signature was now valid, the server accepted the forged administrator token.


## Impact

An attacker who discovers the signing secret can fully forge authentication tokens.

Potential consequences:

- Complete authentication bypass
- User impersonation
- Privilege escalation
- Unauthorized administrative actions


## Root Cause

The application uses a weak secret key for JWT signing.

JWT signatures are cryptographically secure only when:

- the algorithm is correctly implemented
- the secret is sufficiently random
- the key is protected


A weak secret transforms a cryptographic problem into a simple password cracking problem.


## Remediation

Recommended fixes:

- Use strong randomly generated secrets.
- Store secrets securely.
- Rotate signing keys periodically.
- Never use dictionary words or predictable values.
- Use appropriate key lengths.
- Monitor for unauthorized token generation.


## Real-World Relevance

Weak JWT signing keys are dangerous because attackers do not need to exploit application logic.

Once the secret is recovered, they can generate unlimited valid tokens offline.

This type of vulnerability has affected real-world applications where developers used predictable JWT secrets.


## Tools Used

- Burp Suite
- JWT Editor Extension
- Burp Decoder
- Hashcat


## Skills Demonstrated

- JWT Analysis
- Cryptographic Testing
- Offline Brute Force
- Hashcat
- Token Forgery
- Authentication Bypass


## Attack Chain

1. Capture JWT token
2. Identify signing algorithm
3. Test secret strength
4. Brute-force signing key
5. Modify JWT claims
6. Re-sign token
7. Access admin functionality


## Lessons Learned

JWT security depends more on key management than on the token format itself.

A perfectly implemented JWT system becomes insecure if the signing secret is weak.

Strong cryptography requires strong keys.
