# Method-based access control can be circumvented

## Lab

PortSwigger Web Security Academy

Difficulty: Practitioner

Category: Access Control Vulnerabilities

Vulnerability Type:
- Broken Access Control
- HTTP Method-based Access Control Bypass


## Vulnerability Overview

The application implements access control rules based on the HTTP method used in requests.

However, these restrictions are incorrectly enforced, allowing an attacker to bypass authorization checks by modifying the HTTP method.


## Objective

The objective was to promote a normal user account to administrator privileges by bypassing the flawed access control mechanism.


## Methodology

The application behavior was analyzed using Burp Suite.

A legitimate administrative request was captured and then modified to test whether the authorization controls were properly enforced for different HTTP methods.


## Discovery

Using administrator credentials, the request used to promote another user was captured.

The request was then replayed using a normal user session.

The application correctly rejected the unauthorized request:

```http
Unauthorized
```

This confirmed that the authorization check was active.


## Exploitation

The request was modified to test whether the access control depended on the HTTP method.

The original request used:

```http
POST /admin-roles
```

The request method was changed using Burp Repeater.

After changing the method to:

```http
GET /admin-roles
```

the authorization restriction was bypassed.

The username parameter was changed to the attacker's own account, allowing the normal user to gain administrator privileges.


## Impact

An attacker with a regular account could bypass authorization controls and obtain administrator privileges.

Possible consequences:

- Privilege escalation
- Unauthorized administrative actions
- Account manipulation
- Full compromise of application privileges


## Root Cause

The application applies authorization checks inconsistently depending on the HTTP method.

Access control must protect the underlying action regardless of how the request is formatted.

The server should verify authorization for every request that performs a privileged operation.


## Remediation

Recommended fixes:

- Apply authorization checks independently of HTTP methods
- Validate user permissions server-side for every sensitive action
- Do not rely on request methods as a security boundary
- Ensure all alternative request methods enforce the same access controls


## Lessons Learned

HTTP methods are part of the request structure, not a security mechanism.

Changing `POST` to `GET` should never allow a user to bypass authorization.

Access control must be enforced on the action itself, not on how the client requests it.
