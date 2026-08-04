# 2FA Broken Logic

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: Authentication

Vulnerability Type:
- Multi-Factor Authentication (2FA)
- Broken Authentication
- Business Logic Flaw


## Vulnerability Overview

The application implements two-factor authentication (2FA), but the verification process contains a logical flaw.

Instead of securely binding the verification code to the authenticated user, the application relies on a user-controlled parameter to determine which account is being verified.

As a result, an attacker can request and brute-force a valid 2FA code for another user's account.


## Objective

The objective was to bypass the flawed two-factor authentication mechanism and gain access to Carlos's account.


## Methodology

The authentication workflow was analyzed using Burp Suite.

The objective was to understand how the application associated the generated 2FA code with a specific user account.

Each step of the login process was intercepted and inspected before attempting to manipulate the verification request.


## Discovery

During the authentication process, the request sent to the `/login2` endpoint contained a parameter named:

```http
verify=wiener
```

This parameter identified which user's account was being verified.

Because the parameter was fully controlled by the client, it could be modified without server-side validation.


## Exploitation

The authentication workflow was manipulated in several stages.

First, the `verify` parameter was changed from the attacker's username to:

```http
verify=carlos
```

This caused the application to generate a temporary verification code for Carlos's account.

After initiating a normal login using the attacker's credentials, the verification request was intercepted using Burp Intruder.

The `mfa-code` parameter was configured as the attack payload while keeping:

```http
verify=carlos
```

The verification code was successfully brute-forced.

Once the correct code was identified, the application granted access to Carlos's account.


## Impact

An attacker can bypass two-factor authentication and gain access to another user's account.

Successful exploitation may result in:

- Account takeover
- Unauthorized access to sensitive information
- Privilege escalation (if the victim has elevated permissions)
- Complete compromise of user accounts


## Root Cause

The application trusts a client-controlled parameter to determine which account is being verified.

The 2FA verification process is not securely linked to the authenticated session.

Security-sensitive decisions must never rely on parameters that can be modified by the client.


## Remediation

Recommended fixes:

- Bind the verification code to the authenticated server-side session.
- Ignore client-supplied account identifiers during 2FA verification.
- Invalidate verification codes immediately after use.
- Apply rate limiting to verification attempts.
- Log and monitor repeated failed 2FA submissions.


## Real-World Relevance

Two-factor authentication is often considered a strong security control, but implementation flaws can completely undermine its effectiveness.

Many real-world authentication bypasses are caused by incorrect application logic rather than weaknesses in the cryptographic algorithm itself.

This lab demonstrates the importance of testing the entire authentication workflow, not just the strength of the verification code.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- Burp Intruder
- Authentication Flow Analysis
- HTTP Request Manipulation
- Business Logic Testing
- Multi-Factor Authentication Testing


## Lessons Learned

Strong security mechanisms are only effective when implemented correctly.

Even a robust 2FA system can be bypassed if the application allows the client to control which account is being verified.

Authentication workflows should always bind security-critical operations to trusted server-side session data.
