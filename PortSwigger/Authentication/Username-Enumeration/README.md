# Username Enumeration via Response Timing

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: Authentication

Vulnerability Type:
- Username Enumeration
- Timing Attack
- Brute Force


## Vulnerability Overview

The application leaks information through differences in response times during the authentication process.

Although invalid login attempts generate similar error messages, the server takes longer to process requests for valid usernames. An attacker can use these timing differences to identify existing accounts before attempting a password attack.

The application also implements IP-based brute-force protection, but this protection can be bypassed by manipulating the `X-Forwarded-For` HTTP header.


## Objective

The objective was to identify a valid username using response timing analysis, brute-force the corresponding password, and successfully authenticate to the application.


## Methodology

The login request was intercepted using Burp Suite.

Authentication requests were analyzed to observe both response content and response times.

To avoid the application's IP-based rate limiting, the `X-Forwarded-For` header was manipulated so that each request appeared to originate from a different IP address.

Burp Intruder was then used to automate the enumeration process.


## Discovery

Repeated login attempts showed that invalid usernames consistently generated similar response times.

However, valid usernames required additional server-side processing, producing noticeably longer response times.

Using Burp Intruder, multiple candidate usernames were tested while spoofing the client IP through the `X-Forwarded-For` header.

The username with the consistently longest response time was identified as valid.


## Exploitation

After identifying a valid username, a second Intruder attack was launched using the same IP spoofing technique.

The username remained fixed while candidate passwords were tested automatically.

A successful authentication attempt was identified by an HTTP **302 Redirect** response, revealing the correct password.

The recovered credentials were then used to log into the application successfully.


## Impact

An attacker can enumerate valid usernames without relying on different error messages.

Once a valid account is identified, password attacks become significantly more effective.

Combined with weak brute-force protections, this can lead to unauthorized account compromise.


## Root Cause

The authentication process performs additional operations for existing users, causing measurable differences in response times.

Furthermore, the application trusts the `X-Forwarded-For` header when enforcing IP-based rate limiting, allowing attackers to bypass brute-force protections.


## Remediation

Recommended fixes:

- Ensure authentication requests require consistent processing time for both valid and invalid usernames.
- Return identical responses regardless of username validity.
- Implement server-side rate limiting using trusted client information.
- Do not rely on client-controlled headers such as `X-Forwarded-For` for security decisions.
- Enforce account lockout or progressive delays after repeated failed login attempts.


## Real-World Relevance

Timing attacks are commonly used during the reconnaissance phase of penetration tests.

Even when applications display identical login error messages, subtle timing differences can disclose valid usernames.

This information significantly reduces the search space for password attacks and is frequently chained with brute-force or credential-stuffing attacks.


## Lessons Learned

Authentication systems must avoid leaking information through observable behavior.

Even small differences in response times can reveal sensitive information when requests are automated and statistically analyzed.

## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- Burp Intruder
- HTTP Request Analysis
- Timing Analysis
- Username Enumeration
- Brute Force Testing

Security controls such as rate limiting should always rely on trusted server-side information rather than client-controlled HTTP headers.
