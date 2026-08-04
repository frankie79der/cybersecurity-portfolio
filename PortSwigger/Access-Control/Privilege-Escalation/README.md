# User role controlled by request parameter

## Lab

PortSwigger Web Security Academy

Difficulty: Apprentice

Category: Access Control Vulnerabilities

Vulnerability Type:
- Privilege Escalation
- Broken Access Control
- Cookie Manipulation


## Vulnerability Overview

The application determines administrative privileges using a client-controlled cookie.

Because the server trusts the value of the `Admin` cookie, a regular user can modify it and gain administrator privileges.


## Objective

The objective was to access the admin panel and delete the user `carlos`.


## Methodology

The application was tested by analyzing authentication and authorization behavior using Burp Suite.

The goal was to identify how the application determines whether a user has administrator privileges.


## Discovery

After logging in with a normal user account:

```
wiener:peter
```

access to the administrator panel was denied.

The login response was intercepted using Burp Suite.

The response contained the following cookie:

```http
Set-Cookie: Admin=false
```

The cookie value appeared to control administrative privileges.


## Exploitation

The server trusted the client-controlled cookie value.

The cookie was modified from:

```http
Admin=false
```

to:

```http
Admin=true
```

After changing the cookie value, the administrator panel became accessible:

```
/admin
```

The admin functionality was then used to delete the user `carlos`.


## Impact

An attacker could escalate privileges from a normal user account to administrator.

Possible consequences include:

- Unauthorized access to administrative functionality
- User account deletion
- Modification of application data
- Complete compromise of application privileges


## Root Cause

The application makes authorization decisions based on a value controlled by the client.

Cookies and other client-side data cannot be trusted for security decisions.

The server should verify user privileges using trusted server-side information.


## Remediation

Recommended fixes:

- Store authorization information server-side
- Validate user permissions before accessing administrative functions
- Do not rely on client-controlled cookies
- Implement proper server-side access control checks


## Lessons Learned

Authentication and authorization are separate concepts.

A user can be correctly authenticated but still must be prevented from performing unauthorized actions.

Authorization decisions must always be enforced by the server.
