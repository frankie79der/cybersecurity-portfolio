# Password Reset Poisoning via Middleware

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: Authentication

Vulnerability Type:
- Password Reset Poisoning
- Host Header Injection
- Broken Authentication


## Vulnerability Overview

The application generates password reset links dynamically using information supplied by HTTP headers.

Because the application trusts the `X-Forwarded-Host` header without proper validation, an attacker can manipulate the generated password reset URL and redirect password reset tokens to an attacker-controlled domain.

This allows an attacker to steal a victim's password reset token and take over the account.


## Objective

The objective was to obtain Carlos's password reset token and use it to reset his password, ultimately gaining access to his account.


## Methodology

The password reset functionality was analyzed using Burp Suite.

The reset workflow was inspected to determine how the application generated password reset links and which HTTP headers influenced the generated URL.

Special attention was given to reverse proxy headers that are commonly trusted by web applications.


## Discovery

A password reset request generated an email containing a unique password reset link.

While testing the request in Burp Repeater, it was discovered that the application trusted the following header:

```http
X-Forwarded-Host
```

By modifying this header, the generated password reset URL pointed to an attacker-controlled domain instead of the legitimate application.


## Exploitation

A password reset request was submitted for the victim account while injecting a malicious `X-Forwarded-Host` value.

The application generated a password reset email containing a link to the attacker's server.

When the victim accessed the malicious reset link, the unique password reset token was transmitted to the attacker-controlled server.

The stolen token was then inserted into a legitimate password reset URL, allowing the attacker to define a new password for Carlos's account.

Finally, the new credentials were used to authenticate successfully as Carlos.


## Impact

Successful exploitation allows complete account takeover without knowing the victim's password.

Potential consequences include:

- Unauthorized password reset
- Account compromise
- Unauthorized access to sensitive information
- Privilege escalation if privileged accounts are targeted


## Root Cause

The application trusts the `X-Forwarded-Host` header when generating password reset URLs.

HTTP headers supplied by the client should never be trusted for security-sensitive operations unless they originate from a trusted reverse proxy and are properly validated.

Password reset tokens should only be delivered through trusted application-generated URLs.


## Remediation

Recommended fixes:

- Do not generate security-sensitive URLs using client-controlled headers.
- Use a fixed, server-side configured application hostname.
- Validate and sanitize reverse proxy headers.
- Ensure password reset tokens expire quickly and are single-use.
- Monitor password reset activity for suspicious behavior.


## Real-World Relevance

Password reset poisoning is a well-known attack against applications deployed behind reverse proxies or load balancers.

Applications that incorrectly trust headers such as `X-Forwarded-Host` or `Host` can unintentionally expose password reset tokens to attackers, leading to full account compromise.

This type of vulnerability has affected several real-world web applications.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- HTTP Header Manipulation
- Authentication Workflow Analysis
- Password Reset Testing
- Host Header Injection
- Account Takeover Techniques


## Lessons Learned

Password reset mechanisms are security-critical workflows.

Applications must never trust client-controlled headers when constructing password reset URLs.

A secure password reset process should rely entirely on trusted server-side configuration rather than information supplied by incoming HTTP requests.
