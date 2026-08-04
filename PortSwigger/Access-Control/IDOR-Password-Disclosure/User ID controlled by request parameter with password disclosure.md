# IDOR - User ID controlled by request parameter with password disclosure

## Lab

PortSwigger Web Security Academy

Category:
Access Control Vulnerability

Difficulty:
Apprentice


## Vulnerability Overview

The application exposes user account information through a user-controlled parameter.

The server fails to properly verify whether the authenticated user is authorized to access the requested account.

This results in an Insecure Direct Object Reference (IDOR) vulnerability.


## Objective

Retrieve the administrator's password and use it to access the `administrator` account and remove another user.


## Environment

Tools used:

- Browser
- Burp Suite Proxy


## Analysis

After logging into my own account using the provided credentials, I accessed the account page.

The application loaded user information through a parameter in the URL:


**`?id=wiener`**


The parameter appeared to control which user account information was retrieved.


## Exploitation

I intercepted the request using Burp Suite and modified the user identifier.

Original request:


`GET /my-account?id=wiener`


Modified request:


`GET /my-account?id=administrator`


The application returned the `administrator` account information.

The response contained the `administrator` password inside the page source, despite the input field being visually masked in the browser.


## Impact

An attacker could:

- Access another user's account information
- Obtain sensitive credentials
- Compromise administrator access
- Perform unauthorized actions


## Root Cause

The application trusts user-controlled input to identify accounts without performing proper authorization checks.

The server verifies that the user is authenticated, but it does not verify that the user is authorized to access the requested account.


## Remediation

Possible fixes:

- Perform server-side authorization checks for every account request
- Avoid exposing sensitive information such as passwords
- Never store or display plaintext passwords
- Use indirect object references where appropriate


## Lessons Learned

Authentication and authorization are different security concepts.

A user being logged in does not mean they should have access to every account resource.
