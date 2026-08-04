## Completed Labs

- ✅ Unprotected admin functionality
- ✅ Unprotected admin functionality with unpredictable URL
- ✅ User role controlled by request parameter
- ✅ User role can be modified in user profile
- ✅ User ID controlled by request parameter
- ✅ User ID controlled by request parameter, with unpredictable user IDs
- ✅ User ID controlled by request parameter with data leakage in redirect
- ✅ User ID controlled by request parameter with password disclosure
- ✅ Insecure direct object references
- ✅ URL-based access control can be circumvented
- ✅ Method-based access control can be circumvented
- ✅ Multi-step process with no access control on one step
- ✅ Referer-based access control

- # Access Control Vulnerabilities

## Overview

Access control vulnerabilities occur when an application fails to properly enforce what actions an authenticated user is allowed to perform.

Authentication verifies who the user is.

Authorization determines what the user is allowed to access.

A failure in authorization logic can allow attackers to access unauthorized resources, perform privileged actions, or modify other users' data.

---

## Concepts Covered

This section covers:

- Unprotected administrative functionality
- Insecure Direct Object References (IDOR)
- Privilege escalation
- Parameter tampering
- Access control bypass techniques
- Multi-step workflow authorization flaws

---

## Tools Used

- Burp Suite
- Browser Developer Tools

---

## Completed Labs

- Unprotected admin functionality
- Unprotected admin functionality with unpredictable URL
- User role controlled by request parameter
- User role can be modified in user profile
- User ID controlled by request parameter
- User ID controlled by request parameter, with unpredictable user IDs
- User ID controlled by request parameter with data leakage in redirect
- User ID controlled by request parameter with password disclosure
- Insecure direct object references
- URL-based access control can be circumvented
- Method-based access control can be circumvented
- Multi-step process with no access control on one step
- Referer-based access control

---

## Detailed Write-ups

- [Unprotected Admin Functionality](./Unprotected-Admin-Functionality)
- [IDOR - Password Disclosure](./IDOR-Password-Disclosure)
- [Privilege Escalation](./Privilege-Escalation)
- [Access Control Bypass](./Access-Control-Bypass)
