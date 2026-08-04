# Offline Password Cracking

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: Authentication

Vulnerability Type:
- Offline Password Cracking
- Insecure Password Storage
- Weak Persistent Authentication


## Vulnerability Overview

The application implements a "Stay logged in" feature using a persistent authentication cookie.

The cookie contains the username together with an unsalted MD5 hash of the user's password.

Once the cookie is obtained, the password hash can be extracted and cracked offline without interacting with the application.


## Objective

The objective was to obtain Carlos's persistent authentication cookie, recover the password hash, crack it offline, and authenticate successfully as Carlos.


## Methodology

The "Stay logged in" functionality was analyzed using Burp Suite.

The authentication cookie was inspected to determine its format and understand how persistent authentication was implemented.

After obtaining the victim's cookie through an existing Stored XSS vulnerability, the cookie was decoded and its password hash extracted for offline analysis.


## Discovery

Analysis of the authentication response revealed that the persistent login cookie was Base64 encoded.

After decoding the cookie, its structure was identified as:

```text
username:md5(password)
```

Example:

```text
carlos:26323c16d5f4dabff3bb136f2460a943
```

This exposed the user's password hash directly to anyone able to obtain the cookie.


## Exploitation

A Stored Cross-Site Scripting (XSS) vulnerability was used to steal Carlos's persistent authentication cookie.

Once the cookie was obtained, it was decoded using Burp Decoder.

The extracted MD5 hash was then cracked offline, revealing Carlos's password.

The recovered credentials were used to authenticate successfully and access Carlos's account.


## Impact

An attacker who obtains a persistent authentication cookie can recover the user's password without sending additional authentication requests.

Possible consequences include:

- Account takeover
- Credential disclosure
- Password reuse attacks against other services
- Unauthorized access to sensitive information


## Root Cause

The application stores a password-derived value directly inside the authentication cookie.

The cookie exposes an unsalted MD5 hash, allowing attackers to perform offline password cracking.

Persistent authentication mechanisms should never expose reusable password-derived information.


## Remediation

Recommended fixes:

- Never store password hashes inside client-side cookies.
- Use randomly generated session or remember-me tokens.
- Store authentication tokens securely on the server.
- Use strong password hashing algorithms such as Argon2, bcrypt, or scrypt.
- Invalidate persistent tokens after password changes or suspicious activity.


## Real-World Relevance

Persistent login ("Remember Me") functionality is commonly implemented in modern web applications.

Poorly designed authentication cookies have repeatedly led to account compromise when combined with other vulnerabilities such as Cross-Site Scripting (XSS).

This lab demonstrates how multiple low- and medium-severity issues can be chained together into a complete account takeover.


## Skills Demonstrated

- Burp Proxy
- Burp Decoder
- Cookie Analysis
- Base64 Decoding
- Password Hash Analysis
- Offline Password Cracking
- Authentication Testing
- Vulnerability Chaining


## Lessons Learned

Persistent authentication mechanisms should rely on random, server-managed tokens rather than password-derived values.

Even when passwords are not transmitted directly, exposing weak password hashes can allow attackers to recover credentials offline and completely compromise user accounts.
