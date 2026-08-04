# Broken Brute-Force Protection, Multiple Credentials per Request

## Lab

PortSwigger Web Security Academy

Difficulty: Expert

Category: Authentication

Vulnerability Type:
- Broken Brute-Force Protection
- Business Logic Flaw
- Authentication Bypass


## Vulnerability Overview

The application attempts to protect user accounts against brute-force attacks.

However, the protection mechanism assumes that each authentication request contains only a single password.

Because the login endpoint accepts passwords in JSON format, an attacker can submit multiple candidate passwords within a single HTTP request, effectively bypassing the intended brute-force protection.


## Objective

The objective was to recover Carlos's password by exploiting a flaw in the application's brute-force protection and successfully authenticate to his account.


## Methodology

The authentication process was analyzed using Burp Suite.

The login request was intercepted and inspected to understand how user credentials were submitted to the server.

Particular attention was given to the JSON request body and the application's handling of authentication data.


## Discovery

The login endpoint accepted authentication requests using JSON.

Instead of submitting a single password value:

```json
{
    "username": "carlos",
    "password": "password123"
}
```

the application also accepted an array of password values.

This behavior suggested that the server processed multiple candidate passwords during a single authentication attempt.


## Exploitation

The request body was modified to replace the password string with an array containing all candidate passwords.

Example:

```json
{
    "username": "carlos",
    "password": [
        "123456",
        "password",
        "qwerty",
        "...additional candidates..."
    ]
}
```

The modified request was sent using Burp Repeater.

The server evaluated every password contained in the array during the same request.

One of the supplied passwords matched Carlos's credentials, resulting in an HTTP **302 Redirect**, indicating successful authentication.

The authenticated session was then used to access Carlos's account.


## Impact

An attacker can bypass brute-force protections by testing multiple credentials within a single request.

This significantly reduces the effectiveness of rate limiting and login attempt restrictions, increasing the risk of account compromise.


## Root Cause

The application enforces brute-force protection at the HTTP request level rather than at the credential validation level.

Instead of validating that each request contains exactly one password, the server processes every password included in the JSON array.

As a result, multiple authentication attempts occur while only a single request is counted.


## Remediation

Recommended fixes:

- Accept only a single password value per authentication request.
- Validate request structure before processing authentication data.
- Apply rate limiting to each credential verification rather than each HTTP request.
- Reject malformed or unexpected JSON input.
- Monitor abnormal authentication patterns.


## Real-World Relevance

Modern APIs commonly use JSON for authentication.

Applications that fail to validate input structure may unintentionally introduce business logic flaws that completely bypass traditional brute-force protections.

This vulnerability demonstrates why penetration testing should include unexpected input formats rather than relying only on standard user interactions.


## Skills Demonstrated

- Burp Proxy
- Burp Repeater
- JSON Request Analysis
- Authentication Testing
- Business Logic Testing
- Brute-Force Protection Analysis
- HTTP Request Manipulation


## Lessons Learned

Security controls are only effective when they protect the underlying operation rather than the request itself.

Even well-designed brute-force protections can fail if developers assume that clients always submit requests in the expected format.

Testing should include malformed, unexpected, and edge-case inputs to identify logic flaws that standard testing may overlook.
