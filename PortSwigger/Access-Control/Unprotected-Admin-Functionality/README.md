# Unprotected Admin Functionality

## Lab

PortSwigger Web Security Academy

Difficulty: Apprentice

Category: Access Control Vulnerabilities


## Vulnerability Overview

The application exposes an administrative panel without implementing proper access control.

The application relies on hiding the location of the admin functionality instead of enforcing authorization checks on the server side.


## Objective

The objective was to identify the administrative panel and delete the user `carlos`.


## Methodology

The first step was to perform basic reconnaissance on the application.

Common files such as `robots.txt` were checked because they may contain information about hidden resources or directories.


## Discovery

The file:
*`/robots.txt`*

was accessible without authentication.

The response revealed a hidden administrative path:
*`Disallow: /administrator-panel`*



## Exploitation

By navigating to:
*`/administrator-panel`*

the administrative interface became accessible.

No authorization mechanism prevented access to the admin functionality.


## Impact

An attacker could access administrative features without proper privileges.

Depending on the available functionality, this could allow:

- User deletion
- Account manipulation
- Unauthorized administrative actions


## Root Cause

The application attempted to protect the admin panel through obscurity.

Knowing or discovering the URL was enough to access administrative functionality.

The server did not verify whether the current user had administrator privileges.


## Remediation

Proper authorization checks should be implemented server-side.

The application should:

- Verify user permissions before allowing access to administrative endpoints
- Apply authorization checks to every sensitive action
- Never rely on hidden URLs as a security mechanism


## Lessons Learned

Hidden functionality is not protected functionality.

Access control must be enforced by the application logic, not by assuming that attackers cannot discover hidden URLs.
