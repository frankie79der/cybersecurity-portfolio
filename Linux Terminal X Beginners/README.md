# 🐧 Linux Terminal from ZERO

> A practical Linux terminal guide for complete beginners.  
> Learn what each command does, why you would use it, what the options mean, and how to test it safely.

---

## 🎯 About This Repository

This repository is designed for someone who is starting Linux **from absolute zero**.

The goal is not to memorize hundreds of commands.

The goal is to understand:

```text
What am I asking Linux?
What does this command do?
What does the output mean?
When would I actually use it?
```

The guide starts with basic system information and file navigation, then gradually moves into:

- files and directories
- searching
- pipes and redirection
- processes
- permissions
- users and groups
- logs
- networking
- DNS
- ports and services
- packet capture
- systemd
- Bash scripting
- Nmap
- cybersecurity tools

---

# ⚠️ Cybersecurity Lab Notice

Some commands later in this guide involve:

- network scanning
- password testing
- packet capture
- ARP spoofing
- penetration-testing tools

Use them **only on systems and networks that you own or are explicitly authorized to test**.

A private virtual lab is perfect for learning these techniques safely.

---

# Table of Contents

1. [Linux Command Structure](#linux-command-structure)
2. [System Basics and Identity](#1-system-basics-and-identity)
3. [Filesystem and Navigation](#2-filesystem-and-navigation)
4. [Finding Files and Programs](#3-finding-files-and-programs)
5. [Redirection and Pipelines](#4-redirection-and-pipelines)
6. [Reading and Comparing Files](#5-reading-and-comparing-files)
7. [Archives](#6-archives)
8. [Processes and Jobs](#7-processes-and-jobs)
9. [Basic Permissions](#8-basic-permissions)
10. [Special Permissions](#9-special-permissions)
11. [Users and Groups](#10-users-and-groups)
12. [Kernel and Logs](#11-kernel-and-logs)
13. [Network Identity](#12-network-identity)
14. [Network Interfaces](#13-network-interfaces)
15. [Routing](#14-routing)
16. [Connectivity](#15-connectivity)
17. [DNS](#16-dns)
18. [Ports and Services](#17-ports-and-services)
19. [Processes and Ports](#18-processes-and-ports)
20. [ARP and Layer 2](#19-arp-and-layer-2)
21. [Firewall](#20-firewall)
22. [Packet Capture](#21-packet-capture)
23. [Important Network Files](#22-important-network-files)
24. [Testing Network Services](#23-testing-network-services)
25. [Nmap](#24-nmap)
26. [Linux Services with systemd](#25-linux-services-with-systemd)
27. [Basic Bash Scripting](#26-basic-bash-scripting)
28. [Real Network Services](#27-real-network-services)
29. [Netcat](#28-netcat)
30. [Security Lab Examples](#29-security-lab-examples)
31. [Useful Security Tools](#30-useful-security-tools)
32. [Practice Exercises](#31-practice-exercises)
33. [Final Cheat Sheet](#32-final-cheat-sheet)

---

# Linux Command Structure

Most Linux commands follow this structure:

```bash
command options arguments
```

Example:

```bash
ls -la /home
```

Breakdown:

```text
ls       = command
-la      = options
/home    = argument
```

Another example:

```bash
ping -c 4 8.8.8.8
```

```text
ping        = command
-c          = option
4           = value for the option
8.8.8.8     = target
```

You will often see commands written like this:

```bash
$ whoami
```

The `$` represents a normal user's shell prompt.

You normally type only:

```bash
whoami
```

A `#` prompt often represents the `root` user.

---

# 1. System Basics and Identity

These commands answer basic questions such as:

```text
Who am I?
What computer am I using?
What Linux system is this?
How long has it been running?
How much memory is available?
```

---

## `echo`

`echo` prints text to the terminal.

```bash
echo "Hello Linux"
```

Output:

```text
Hello Linux
```

It can also display variables.

```bash
echo $HOME
```

Example:

```text
/home/kali
```

Another example:

```bash
name="Alice"
echo $name
```

Output:

```text
Alice
```

`echo` becomes extremely useful when you start writing Bash scripts.

---

## `whoami`

Shows the currently logged-in user.

```bash
whoami
```

Example:

```text
kali
```

Think of it as asking Linux:

> Who am I?

---

## `id`

Shows detailed identity information.

```bash
id
```

Example:

```text
uid=1000(kali) gid=1000(kali) groups=1000(kali),27(sudo)
```

Important fields:

```text
uid     = User ID
gid     = Primary Group ID
groups  = Groups the user belongs to
```

You can also inspect another user:

```bash
id bob
```

---

## `uname`

Displays information about the kernel.

Basic:

```bash
uname
```

All available information:

```bash
uname -a
```

Kernel name:

```bash
uname -s
```

Hostname:

```bash
uname -n
```

Kernel release:

```bash
uname -r
```

Example:

```bash
uname -r
```

Output:

```text
6.8.0-amd64
```

---

## `uptime`

Shows how long the system has been running.

```bash
uptime
```

More human-readable:

```bash
uptime -p
```

Example:

```text
up 2 hours, 15 minutes
```

---

## `hostname`

Shows the computer's hostname.

```bash
hostname
```

Example:

```text
kali
```

---

## `hostnamectl`

Displays more detailed information about the machine.

```bash
hostnamectl
```

Typical information includes:

```text
Hostname
Operating System
Kernel
Architecture
Virtualization
```

---

## `lsb_release -a`

Displays Linux distribution information.

```bash
lsb_release -a
```

Example:

```text
Distributor ID: Kali
Description:    Kali GNU/Linux Rolling
Release:        2026
```

This command may not be installed on every distribution.

---

## `free -h`

Displays memory usage.

```bash
free -h
```

`-h` means:

```text
human-readable
```

Example:

```text
               total        used        free
Mem:            7.7Gi       2.1Gi       4.3Gi
Swap:           2.0Gi          0B       2.0Gi
```

---

## `vmstat 1`

Shows system statistics every second.

```bash
vmstat 1
```

It includes information about:

```text
Processes
Memory
Swap
Disk I/O
CPU
```

Stop it with:

```text
Ctrl + C
```

---

# 2. Filesystem and Navigation

Linux organizes everything under:

```text
/
```

This is called the:

```text
root directory
```

A simple structure might look like:

```text
/
├── home
├── etc
├── var
├── usr
├── tmp
└── root
```

---

## `pwd`

Before moving around, learn this command:

```bash
pwd
```

It means:

```text
Print Working Directory
```

Example:

```text
/home/kali/Documents
```

It answers:

> Where am I?

---

## `ls`

Lists files and directories.

```bash
ls
```

---

## `ls -l`

Long format:

```bash
ls -l
```

Example:

```text
-rw-r--r-- 1 kali kali 1200 Sep 22 10:30 notes.txt
```

It displays information such as:

```text
permissions
owner
group
size
date
filename
```

---

## `ls -a`

Shows hidden files.

```bash
ls -a
```

Linux hidden files normally begin with:

```text
.
```

Examples:

```text
.bashrc
.profile
.ssh
```

---

## `ls -la`

Combines:

```text
-l
-a
```

Command:

```bash
ls -la
```

This is one of the most useful everyday commands.

---

## `ls -F`

Adds symbols that help identify file types.

```bash
ls -F
```

Example:

```text
Documents/
script.sh*
notes.txt
```

A `/` usually indicates a directory.

---

## `ls -R`

Lists directories recursively.

```bash
ls -R
```

Be careful: it can generate a lot of output.

---

# `cd`

Changes directory.

Enter a directory:

```bash
cd Documents
```

Go up one level:

```bash
cd ..
```

Go to your home directory:

```bash
cd ~
```

You can also simply use:

```bash
cd
```

---

## Example

```bash
pwd
cd /var/log
pwd
```

Possible output:

```text
/home/kali
/var/log
```

---

# `mkdir`

Creates a directory.

```bash
mkdir linux-lab
```

---

## `mkdir -p`

Creates parent directories automatically.

```bash
mkdir -p projects/linux/notes
```

Without `-p`, the command could fail if the parent directories do not already exist.

---

# `touch`

Creates an empty file.

```bash
touch notes.txt
```

Check it:

```bash
ls -l notes.txt
```

---

# `cp`

Copies files.

```bash
cp notes.txt backup.txt
```

Copy into another directory:

```bash
cp notes.txt Documents/
```

---

## `cp -r`

Copies directories recursively.

```bash
cp -r project project-backup
```

---

# `mv`

Moves or renames files.

Rename:

```bash
mv old.txt new.txt
```

Move:

```bash
mv report.txt Documents/
```

---

# `rm`

Deletes files.

```bash
rm file.txt
```

> Linux normally does not move files deleted with `rm` into a recycle bin.

---

## `rm -i`

Interactive mode.

```bash
rm -i file.txt
```

Linux asks for confirmation before deleting.

This is useful while learning.

---

## `rm -r`

Deletes directories recursively.

```bash
rm -r test-directory
```

---

## `rm -f`

Force deletion.

```bash
rm -f file.txt
```

`-f` means:

```text
force
```

Use it carefully.

---

# `rmdir`

Deletes an empty directory.

```bash
rmdir empty-folder
```

If the directory contains files, the command fails.

---

# 3. Finding Files and Programs

---

## `find`

Searches the real filesystem.

Find a file:

```bash
find /home -name "notes.txt"
```

Find directories:

```bash
find /home -type d -name "Documents"
```

Find `.log` files:

```bash
find /var/log -type f -name "*.log"
```

Search from the current directory:

```bash
find . -name "*.txt"
```

The `.` means:

```text
current directory
```

---

# `locate`

Searches using an indexed database.

```bash
locate ssh_config
```

It is usually much faster than `find`.

If the database needs updating:

```bash
sudo updatedb
```

---

# `which`

Shows which executable will be used.

```bash
which python3
```

Example:

```text
/usr/bin/python3
```

Another example:

```bash
which nmap
```

---

# `whereis`

Searches for program binaries, manuals, and related files.

```bash
whereis ssh
```

Example:

```text
ssh: /usr/bin/ssh /usr/share/man/man1/ssh.1.gz
```

---

# `tree`

Displays directories visually.

```bash
tree
```

Example:

```text
project/
├── README.md
├── notes/
│   └── linux.txt
└── scripts/
    └── test.sh
```

If it is not installed:

```bash
sudo apt install tree
```

---

# 4. Redirection and Pipelines

This is one of the most powerful parts of Linux.

---

# `>`

Redirects output into a file.

```bash
whoami > user.txt
```

Then:

```bash
cat user.txt
```

Important:

```text
> overwrites the file
```

---

# `>>`

Appends output instead of overwriting.

```bash
uptime >> system.txt
```

---

# Multiple Commands into One File

You can group commands:

```bash
(whoami; uname -a; uptime) > system-info.txt
```

Then:

```bash
cat system-info.txt
```

---

# The Pipe `|`

A pipe sends the output of one command into another command.

Example:

```bash
ps aux | grep ssh
```

Think of it like:

```text
ps aux
   |
   v
lots of output
   |
   v
grep ssh
   |
   v
only lines containing "ssh"
```

---

# `grep`

Searches text.

```bash
grep "root" /etc/passwd
```

---

## `grep -w`

Matches a complete word.

```bash
grep -w "root" /etc/passwd
```

---

## `grep -E`

Uses extended regular expressions.

```bash
grep -E 'error|warning|failed' logfile.txt
```

Case-insensitive version:

```bash
grep -iE 'error|warning|failed' logfile.txt
```

Here:

```text
-i = ignore uppercase/lowercase
-E = extended regular expressions
|  = OR inside the expression
```

---

# 5. Reading and Comparing Files

---

# `cat`

Displays an entire file.

```bash
cat notes.txt
```

Good for small files.

---

# `less`

Opens a file in an interactive viewer.

```bash
less /var/log/syslog
```

Useful keys:

```text
q        quit
/word    search for "word"
n        next match
```

For large files, `less` is usually better than `cat`.

---

# `head`

Shows the beginning of a file.

```bash
head file.txt
```

Default:

```text
10 lines
```

Show 20 lines:

```bash
head -n 20 file.txt
```

Show the first 100 bytes:

```bash
head -c 100 file.txt
```

---

# `tail`

Shows the end of a file.

```bash
tail file.txt
```

Last 20 lines:

```bash
tail -n 20 file.txt
```

Last 100 bytes:

```bash
tail -c 100 file.txt
```

---

## Follow a Log in Real Time

One extremely useful variation is:

```bash
tail -f /var/log/syslog
```

`-f` means:

```text
follow
```

New log entries appear automatically.

Stop with:

```text
Ctrl + C
```

---

# `diff`

Compares files.

```bash
diff file1.txt file2.txt
```

Compare directories recursively:

```bash
diff -r folder1 folder2
```

---

# `man`

Displays the official manual page for a command.

```bash
man ls
```

Another example:

```bash
man find
```

Exit with:

```text
q
```

One of the best habits you can develop is:

```bash
man command
```

before searching the Internet.

---

# 6. Archives

The classic Linux archiving command is:

```bash
tar
```

---

## Important `tar` Options

```text
-c    create archive
-x    extract archive
-f    archive filename
-z    gzip compression
-v    verbose output
```

---

## Create an Archive

```bash
tar -cf archive.tar file1 file2
```

---

## Create a Compressed Archive

```bash
tar -czf archive.tar.gz file1 file2
```

Archive a directory:

```bash
tar -czf project.tar.gz project/
```

---

## Extract an Archive

```bash
tar -xf archive.tar
```

Compressed archive:

```bash
tar -xzf archive.tar.gz
```

---

# 7. Processes and Jobs

A **process** is a running program.

---

# `top`

Displays running processes in real time.

```bash
top
```

You can observe:

```text
PID
CPU
Memory
User
Command
```

Exit with:

```text
q
```

---

# `ps aux`

Displays running processes.

```bash
ps aux
```

Search for SSH:

```bash
ps aux | grep ssh
```

Search for Python:

```bash
ps aux | grep python
```

---

# PID

Every process has a:

```text
Process ID
```

or:

```text
PID
```

Example:

```text
root   1450 ... sshd
```

Here:

```text
1450 = PID
```

---

# `kill`

Sends a signal to a process.

```bash
kill 1450
```

By default, `kill` normally sends:

```text
SIGTERM
```

which politely asks the process to terminate.

---

# `kill -9`

Forces a process to stop.

```bash
kill -9 1450
```

`-9` means:

```text
SIGKILL
```

Use this only when normal termination does not work.

---

# Background Jobs

Start something in the background:

```bash
sleep 300 &
```

The `&` means:

```text
run in background
```

---

# `jobs`

Displays jobs started from your shell.

```bash
jobs
```

---

# `fg`

Moves a background job to the foreground.

```bash
fg
```

---

# `bg`

Continues a suspended job in the background.

```bash
bg
```

You can suspend a foreground process with:

```text
Ctrl + Z
```

---

# 8. Basic Permissions

Linux permissions are divided into:

```text
User
Group
Others
```

Common notation:

```text
u = user
g = group
o = others
```

Permissions:

```text
r = read
w = write
x = execute
```

---

# Numeric Permissions

Each permission has a number:

```text
4 = read
2 = write
1 = execute
```

Add them together.

Examples:

```text
7 = 4 + 2 + 1 = rwx
6 = 4 + 2     = rw-
5 = 4 + 1     = r-x
4 = 4         = r--
```

---

# `chmod`

Changes file permissions.

```bash
chmod 755 script.sh
```

Meaning:

```text
7 = owner = rwx
5 = group = r-x
5 = others = r-x
```

---

## Symbolic Mode

Add execution permission for the owner:

```bash
chmod u+x script.sh
```

Remove write permission from others:

```bash
chmod o-w file.txt
```

---

# `chown`

Changes file ownership.

```bash
sudo chown bob file.txt
```

Change owner and group:

```bash
sudo chown bob:developers file.txt
```

---

## `chown -R`

Recursive ownership change:

```bash
sudo chown -R bob:developers project/
```

---

# 9. Special Permissions

Linux has additional permission bits.

---

# SUID

Set User ID.

Set it with:

```bash
chmod u+s program
```

On an executable, SUID can cause the program to execute with the privileges of the file owner.

Search for SUID files:

```bash
find / -perm -4000 2>/dev/null
```

Breakdown:

```text
find /          search from root
-perm -4000     search for SUID
2>/dev/null     hide error messages
```

The number:

```text
2
```

represents:

```text
stderr
```

---

# SGID

Set Group ID.

```bash
chmod g+s file
```

On directories, SGID can cause newly created files to inherit the directory's group.

Example:

```bash
chmod g+s shared/
```

Search for SGID files:

```bash
find / -perm -2000 2>/dev/null
```

---

# Sticky Bit

Set with:

```bash
chmod +t directory
```

A classic example is:

```text
/tmp
```

Check it:

```bash
ls -ld /tmp
```

You may see:

```text
drwxrwxrwt
```

The final:

```text
t
```

is the sticky bit.

---

# `umask`

Displays the current default permission mask.

```bash
umask
```

Example:

```text
0022
```

`umask` influences the default permissions assigned to newly created files and directories.

---

# 10. Users and Groups

Most user-management commands require administrator privileges.

---

# `useradd`

Creates a user.

```bash
sudo useradd bob
```

---

## Create Home Directory

```bash
sudo useradd -m bob
```

`-m` creates the user's home directory.

---

## Specify Home Directory

```bash
sudo useradd -m -d /home/bob bob
```

---

# `userdel`

Deletes a user.

```bash
sudo userdel bob
```

---

## Delete User and Home

```bash
sudo userdel -r bob
```

---

# `usermod`

Modifies an existing user.

---

## Change Shell

```bash
sudo usermod -s /bin/bash bob
```

---

## Add User to a Group

```bash
sudo usermod -aG sudo bob
```

Very important:

```text
-a = append
-G = supplementary groups
```

Usually use them together:

```text
-aG
```

---

## Change Home Directory

```bash
sudo usermod -d /home/newbob bob
```

Move existing files too:

```bash
sudo usermod -d /home/newbob -m bob
```

---

# `groupadd`

Creates a group.

```bash
sudo groupadd developers
```

---

# `groupdel`

Deletes a group.

```bash
sudo groupdel developers
```

---

# `passwd`

Changes passwords.

Current user:

```bash
passwd
```

Another user:

```bash
sudo passwd bob
```

---

## Lock Password

```bash
sudo passwd -l bob
```

---

## Unlock Password

```bash
sudo passwd -u bob
```

---

## Password Status

```bash
sudo passwd -S bob
```

---

# `groups`

Shows group memberships.

```bash
groups
```

Another user:

```bash
groups bob
```

---

# `su -`

Switches user and opens a login shell.

```bash
su - bob
```

Switch to root if configured:

```bash
su -
```

---

# `id user`

Another useful way to inspect a user:

```bash
id bob
```

---

# 11. Kernel and Logs

---

# `dmesg`

Displays messages generated by the Linux kernel.

```bash
dmesg
```

Recent messages:

```bash
dmesg | tail
```

---

## Search Kernel Messages

```bash
dmesg | grep -i error
```

Search multiple words:

```bash
dmesg | grep -iE 'error|warning|failed'
```

Example:

```bash
dmesg | grep -iE 'usb|network|error'
```

---

# 12. Network Identity

---

# `hostname`

```bash
hostname
```

Shows the hostname.

---

# `hostname -I`

Shows the machine's IP addresses.

```bash
hostname -I
```

Example:

```text
192.168.1.50 10.10.10.5
```

---

# `uname -n`

Another way to display the network node name:

```bash
uname -n
```

---

# 13. Network Interfaces

Modern Linux networking heavily uses the:

```text
ip
```

command.

---

# `ip a`

Displays interfaces and addresses.

```bash
ip a
```

Look for information such as:

```text
interface name
MAC address
IPv4 address
IPv6 address
UP/DOWN state
```

---

# `ip -br a`

Brief output:

```bash
ip -br a
```

Example:

```text
lo       UNKNOWN    127.0.0.1/8
eth0     UP         192.168.1.50/24
```

This is one of the easiest ways to quickly inspect interfaces.

---

# `ip link`

Displays Layer 2 interface information.

```bash
ip link
```

Useful for checking:

```text
MAC addresses
interface state
MTU
```

---

# `ifconfig`

Older command:

```bash
ifconfig
```

Still common in tutorials.

Modern replacement:

```bash
ip a
```

If `ifconfig` is missing, the package may be:

```text
net-tools
```

---

# 14. Routing

Routing determines where packets go.

---

# `ip r`

Short form:

```bash
ip r
```

Equivalent to:

```bash
ip route
```

---

# `ip route show`

```bash
ip route show
```

Example:

```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel
```

This tells you:

```text
default gateway
connected networks
interfaces used
```

---

# `route -n`

Legacy command:

```bash
route -n
```

`-n` avoids hostname resolution.

Modern alternative:

```bash
ip route
```

---

# 15. Connectivity

---

# `ping`

Tests ICMP reachability.

```bash
ping -c 4 8.8.8.8
```

Breakdown:

```text
-c 4 = send four packets
```

Important:

A successful `ping` means ICMP communication works.

It does **not** automatically prove:

```text
HTTP works
SSH works
DNS works
the host is fully accessible
```

---

# `traceroute`

Shows the network path toward a destination.

```bash
traceroute -n 8.8.8.8
```

`-n` avoids DNS lookups.

---

# `tracepath`

Another route-discovery tool:

```bash
tracepath -n 8.8.8.8
```

---

# Netcat Port Test

```bash
nc -zv 192.168.1.50 22
```

Breakdown:

```text
nc      Netcat
-z      scan mode / no data transfer
-v      verbose
22      port
```

If the service responds, you may see:

```text
succeeded
```

---

# 16. DNS

DNS translates names and helps systems locate services.

---

# `resolvectl status`

Displays DNS configuration when `systemd-resolved` is being used.

```bash
resolvectl status
```

---

# `/etc/resolv.conf`

Inspect DNS resolver configuration:

```bash
cat /etc/resolv.conf
```

Example:

```text
nameserver 192.168.1.1
```

---

# `nslookup`

Resolve a hostname:

```bash
nslookup example.com
```

Query a specific DNS server:

```bash
nslookup example.com 8.8.8.8
```

---

# `dig`

More detailed DNS tool:

```bash
dig example.com
```

---

## Short Output

```bash
dig +short example.com
```

Example:

```text
93.184.216.34
```

---

## Specific DNS Server

```bash
dig @8.8.8.8 example.com
```

---

# 17. Ports and Services

A network service normally listens on a:

```text
IP address + port
```

Examples:

```text
SSH    TCP/22
HTTP   TCP/80
HTTPS  TCP/443
DNS    UDP/TCP 53
SMB    TCP/445
```

---

# `ss -tuln`

```bash
ss -tuln
```

Breakdown:

```text
-t = TCP
-u = UDP
-l = listening
-n = numeric addresses and ports
```

---

# `ss -ltnp`

```bash
sudo ss -ltnp
```

Breakdown:

```text
-l = listening
-t = TCP
-n = numeric
-p = process information
```

---

# `ss -lunp`

UDP version:

```bash
sudo ss -lunp
```

---

# `ss -tulnp`

Combined view:

```bash
sudo ss -tulnp
```

This is one of the most useful networking commands in Linux.

---

# `netstat -tuln`

Legacy version:

```bash
netstat -tuln
```

Modern Linux generally prefers:

```bash
ss
```

---

# 18. Processes and Ports

Sometimes you know the port and want to know:

> Which process owns it?

---

# `ss -lptn`

```bash
sudo ss -lptn
```

Shows listening TCP sockets and processes.

---

# `lsof -i`

```bash
sudo lsof -i
```

Shows open network connections and sockets.

---

## Specific Port

```bash
sudo lsof -i :80
```

Example:

```text
nginx  1250 root  ... TCP *:80 (LISTEN)
```

---

# `fuser`

Find the process using a port:

```bash
sudo fuser 80/tcp
```

Verbose:

```bash
sudo fuser -v 80/tcp
```

---

# 19. ARP and Layer 2

ARP connects:

```text
IPv4 addresses
```

to:

```text
MAC addresses
```

on the local network.

---

# `arp -a`

Legacy command:

```bash
arp -a
```

Displays the ARP cache.

---

# `ip neigh`

Modern equivalent:

```bash
ip neigh
```

Example:

```text
192.168.1.1 dev eth0 lladdr 08:00:27:aa:bb:cc REACHABLE
```

This means:

```text
IP address
    |
    v
MAC address
```

---

# 20. Firewall

---

# `iptables -L`

Displays firewall rules.

```bash
sudo iptables -L
```

---

## Numeric Output

```bash
sudo iptables -L -n
```

---

## Verbose Output

```bash
sudo iptables -L -n -v
```

---

# Default INPUT Policy

Set INPUT to DROP:

```bash
sudo iptables -P INPUT DROP
```

Restore ACCEPT:

```bash
sudo iptables -P INPUT ACCEPT
```

> ⚠️ Be careful on remote systems. A bad firewall rule can disconnect you from the machine.

---

# `ufw`

Check firewall status:

```bash
sudo ufw status
```

`ufw` means:

```text
Uncomplicated Firewall
```

It provides a simpler interface to firewall management.

---

# 21. Packet Capture

Packet capture lets you observe network traffic directly.

---

# `tcpdump`

Capture traffic:

```bash
sudo tcpdump -i eth0
```

---

## Disable Name Resolution

```bash
sudo tcpdump -n -i eth0
```

This is usually easier when learning because you see raw IP addresses.

---

## ICMP Only

```bash
sudo tcpdump -n -i eth0 icmp
```

Then from another terminal:

```bash
ping -c 4 8.8.8.8
```

You can watch the packets appear.

---

## Port 80 Only

```bash
sudo tcpdump -n -i eth0 port 80
```

---

## Save to PCAP

```bash
sudo tcpdump -n -i eth0 -w capture.pcap
```

The resulting:

```text
capture.pcap
```

can be opened with Wireshark.

---

# 22. Important Network Files

---

# `/etc/hosts`

```bash
cat /etc/hosts
```

Contains local hostname mappings.

Example:

```text
127.0.0.1 localhost
192.168.1.50 labserver
```

---

# `/etc/services`

```bash
cat /etc/services
```

Contains known service-to-port mappings.

Search SSH:

```bash
grep -w ssh /etc/services
```

Search HTTP:

```bash
grep -w http /etc/services
```

---

# `/etc/protocols`

```bash
cat /etc/protocols
```

Contains known IP protocol numbers.

Examples include:

```text
icmp
tcp
udp
```

---

# 23. Testing Network Services

---

# `curl`

HTTP request:

```bash
curl http://example.com
```

---

## Headers Only

```bash
curl -I http://example.com
```

`-I` requests response headers.

---

## Headers and Body

```bash
curl -i http://example.com
```

---

# `wget`

Downloads files:

```bash
wget https://example.com/file.txt
```

---

# Netcat Range Test

For your own machine or authorized lab:

```bash
nc -zv 127.0.0.1 1-1024
```

Single port:

```bash
nc -zv 127.0.0.1 22
```

---

# 24. Nmap

> ⚠️ Use Nmap only against machines and networks you own or have explicit permission to test.

Nmap is used for:

```text
Host discovery
Port scanning
Service detection
Basic enumeration
```

---

# SYN Scan

```bash
sudo nmap -sS 192.168.1.50
```

`-sS` means:

```text
TCP SYN scan
```

---

# Service Detection

```bash
nmap -sV 192.168.1.50
```

`-sV` attempts to identify:

```text
service
version
```

Example result:

```text
22/tcp open ssh OpenSSH
80/tcp open http Apache
```

---

# Scan Every TCP Port

```bash
nmap -p- 192.168.1.50
```

`-p-` means:

```text
ports 1 through 65535
```

---

# Aggressive Detection

```bash
sudo nmap -A 192.168.1.50
```

`-A` enables several detection features together.

For learning, it is usually better to understand the individual options first.

---

# A Good Beginner Workflow

First discover ports:

```bash
sudo nmap -sS -p- -T4 192.168.1.50
```

Suppose you discover:

```text
22
80
443
```

Then investigate those ports:

```bash
sudo nmap -sV -sC -p 22,80,443 192.168.1.50
```

Think:

```text
Step 1:
Which ports are open?

Step 2:
What services are behind those ports?
```

---

# 25. Linux Services with systemd

Linux often runs background programs called:

```text
services
```

or:

```text
daemons
```

Examples:

```text
SSH
Nginx
Apache
cron
```

---

# `systemctl`

---

## Check Status

```bash
systemctl status ssh
```

---

## Start Service

```bash
sudo systemctl start ssh
```

---

## Stop Service

```bash
sudo systemctl stop ssh
```

---

## Restart Service

```bash
sudo systemctl restart ssh
```

---

## Enable at Boot

```bash
sudo systemctl enable ssh
```

---

## Disable at Boot

```bash
sudo systemctl disable ssh
```

Important distinction:

```text
start   = start now
enable  = automatically start at boot
```

---

# `journalctl`

Displays logs managed by systemd.

```bash
journalctl
```

---

## Recent Errors

```bash
journalctl -xe
```

---

## Logs for One Service

```bash
sudo journalctl -u nginx
```

SSH:

```bash
sudo journalctl -u ssh
```

Last 20 entries:

```bash
sudo journalctl -u ssh -n 20
```

Follow live:

```bash
sudo journalctl -u ssh -f
```

---

# 26. Basic Bash Scripting

You do not need advanced Bash programming to automate simple Linux tasks.

---

# Variables

```bash
name="Frank"
echo "$name"
```

Important:

```bash
name="Frank"
```

works.

This:

```bash
name = "Frank"
```

does not.

Bash does not allow spaces around `=` when assigning variables.

---

# `$?`

`$?` contains the exit status of the previous command.

Example:

```bash
ping -c 1 127.0.0.1
echo $?
```

Usually:

```text
0
```

means success.

A non-zero value normally means some kind of failure.

---

# `if`

Example:

```bash
if ping -c 1 127.0.0.1 > /dev/null; then
    echo "Host reachable"
else
    echo "Host unreachable"
fi
```

---

# `for`

Example:

```bash
for user in alice bob charlie; do
    echo "$user"
done
```

Output:

```text
alice
bob
charlie
```

---

# `while`

```bash
count=1

while [ "$count" -le 3 ]; do
    echo "$count"
    count=$((count + 1))
done
```

Output:

```text
1
2
3
```

---

# `&&`

Run the second command only if the first succeeds.

```bash
mkdir test && cd test
```

Meaning:

```text
Create directory.

IF successful:

Enter directory.
```

---

# `||`

Run the second command only if the first fails.

```bash
cd /does-not-exist || echo "Directory not found"
```

---

# `alias`

Creates a shortcut.

```bash
alias ll='ls -lah'
```

Now:

```bash
ll
```

runs:

```bash
ls -lah
```

---

# 27. Real Network Services

One of the best ways to learn Linux networking is to run real services.

---

# SSH

Check status:

```bash
systemctl status ssh
```

Start:

```bash
sudo systemctl start ssh
```

Check port:

```bash
sudo ss -ltnp | grep ':22'
```

Connect:

```bash
ssh user@192.168.1.50
```

---

# Nginx

Check:

```bash
systemctl status nginx
```

Start:

```bash
sudo systemctl start nginx
```

Check port 80:

```bash
sudo ss -ltnp | grep ':80'
```

Test:

```bash
curl http://127.0.0.1
```

---

# Apache

```bash
systemctl status apache2
```

Start:

```bash
sudo systemctl start apache2
```

Test:

```bash
curl http://127.0.0.1
```

---

# 28. Netcat

Netcat is a very simple networking tool.

---

# Listen on a Port

In an authorized lab:

```bash
nc -lvnp 4444
```

Breakdown:

```text
-l      listen
-v      verbose
-n      no DNS resolution
-p      specify port
4444    port number
```

From another terminal:

```bash
nc 127.0.0.1 4444
```

Now type:

```text
hello
```

The text should appear in the listening terminal.

This is a simple way to understand:

```text
client
server
IP
port
TCP connection
```

---

# 29. Security Lab Examples

These examples belong in an isolated and authorized training environment.

---

# Hydra

Hydra performs authentication testing against supported services.

Example:

```bash
hydra -L users.txt -P passwords.txt ssh://<LAB_IP> -t 4
```

Breakdown:

```text
hydra                program
-L users.txt         username list
-P passwords.txt     password list
ssh://<LAB_IP>       target SSH service
-t 4                 four parallel tasks
```

Example lab logic:

```text
users.txt
+
passwords.txt
+
SSH server
=
authentication testing
```

Do not run password attacks against systems without explicit authorization.

---

# IP Forwarding

Check current status:

```bash
cat /proc/sys/net/ipv4/ip_forward
```

Typical values:

```text
0 = disabled
1 = enabled
```

Enable temporarily:

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

This allows the Linux machine to forward IPv4 packets between interfaces.

---

# ARP Spoofing

For an isolated authorized lab:

```bash
sudo arpspoof -i eth0 -t <LAB_TARGET_IP> <LAB_GATEWAY_IP>
```

Breakdown:

```text
-i eth0              interface
-t                   target
<LAB_TARGET_IP>      authorized target VM
<LAB_GATEWAY_IP>     lab gateway
```

This can be used to study:

```text
ARP
Layer 2
MITM concepts
traffic forwarding
```

Only use it inside networks you control.

---

# 30. Useful Security Tools

You do **not** need to learn all of these at once.

The important thing is to know what category each tool belongs to.

| Tool | Main Purpose |
|---|---|
| `lynx` | Text-based web browser |
| `hydra` | Authentication/password testing |
| `tcpdump` | Packet capture |
| `nmap` | Network discovery and service enumeration |
| `openssl` | Cryptography, certificates, TLS testing |
| `subfinder` | Subdomain discovery |
| `nuclei` | Template-based security scanning |
| `sqlmap` | SQL injection testing automation |
| `john` | Password/hash recovery |
| `hashcat` | High-performance password/hash recovery |
| `bettercap` | Network analysis and MITM lab testing |
| `metasploit` | Penetration-testing framework |
| `lsof` | Open files and network sockets |
| `strace` | System-call tracing |
| `exiftool` | Metadata inspection |
| `macchanger` | Change a local MAC address |
| `airmon-ng` | Wireless monitor-mode management |
| `airodump-ng` | Wireless network observation |
| `wifite` | Wireless security testing automation |

Some security distributions also contain third-party or less common tools with names such as:

```text
dirhunter
geoip
wiglenet
mxlookup
userrecon
nexfil
mailaccess
```

Tool names, packages, and availability can change.

Before installing an unfamiliar tool, verify:

```text
Official project
Official repository
Documentation
Maintenance status
Purpose
License
```

---

# Useful Advanced Linux Commands

---

# `lsof -i`

Network sockets:

```bash
sudo lsof -i
```

---

# `ss -tulnp`

Listening TCP/UDP services with process information:

```bash
sudo ss -tulnp
```

---

# `strace`

Trace system calls made by a process:

```bash
sudo strace -p PID
```

Example:

```bash
sudo strace -p 1234
```

This can help understand what a process is doing internally.

---

# `awk`

Extract fields from text.

Example:

```bash
ps aux | awk '{print $1}'
```

Prints the first column.

Example:

```bash
ps aux | awk '{print $1, $2}'
```

Prints:

```text
USER PID
```

---

# `watch`

Repeats a command automatically.

```bash
watch -n 1 df -h
```

Meaning:

```text
Run df -h every 1 second.
```

Another useful example:

```bash
watch -n 1 'ss -tuln'
```

---

# 31. Practice Exercises

Learning Linux requires actually using it.

Do not just read this README.

Open a terminal and experiment.

---

# Exercise 1 — Identify the Machine

Run:

```bash
whoami
id
hostname
hostnamectl
uname -a
uptime -p
```

Try to answer:

```text
What user am I?
What groups am I in?
What is the hostname?
What kernel is running?
How long has the system been online?
```

---

# Exercise 2 — Build a Directory Structure

Run:

```bash
mkdir -p ~/linux-lab/documents
cd ~/linux-lab
touch file1.txt
touch file2.txt
cp file1.txt documents/
mv file2.txt notes.txt
tree
```

Try to explain every command.

---

# Exercise 3 — Redirection

Run:

```bash
(whoami; hostname; uname -r; uptime -p) > system.txt
```

Read it:

```bash
cat system.txt
```

Append another line:

```bash
date >> system.txt
```

Then:

```bash
cat system.txt
```

Notice that:

```text
>
```

replaced the file initially.

While:

```text
>>
```

added new content.

---

# Exercise 4 — Pipeline

Run:

```bash
ps aux | grep ssh
```

Then:

```bash
ps aux | grep python
```

Understand the flow:

```text
ps
 |
 v
grep
```

---

# Exercise 5 — Processes

Start:

```bash
sleep 300 &
```

Check jobs:

```bash
jobs
```

Find the process:

```bash
ps aux | grep sleep
```

Stop it:

```bash
kill <PID>
```

Check again:

```bash
ps aux | grep sleep
```

---

# Exercise 6 — Permissions

Create a file:

```bash
touch script.sh
```

Check permissions:

```bash
ls -l script.sh
```

Add execute permission:

```bash
chmod u+x script.sh
```

Check again:

```bash
ls -l script.sh
```

Observe the difference.

---

# Exercise 7 — Network Identity

Run:

```bash
hostname
hostname -I
ip -br a
ip route
ip neigh
```

Try to identify:

```text
My hostname
My IP
My interface
My gateway
My local subnet
Known neighbors
```

---

# Exercise 8 — DNS

Run:

```bash
cat /etc/resolv.conf
```

Then:

```bash
nslookup example.com
```

Then:

```bash
dig example.com
```

Then:

```bash
dig +short example.com
```

Compare the outputs.

---

# Exercise 9 — Find Listening Services

Run:

```bash
sudo ss -tulnp
```

Choose one listening TCP port.

For example:

```text
22
```

Then:

```bash
sudo lsof -i :22
```

Try to answer:

> Which process owns TCP port 22?

---

# Exercise 10 — Build a Local Web Server

Start a simple HTTP server:

```bash
python3 -m http.server 8080
```

Open another terminal.

Check the port:

```bash
ss -ltnp | grep ':8080'
```

Request the page:

```bash
curl http://127.0.0.1:8080
```

Check headers:

```bash
curl -I http://127.0.0.1:8080
```

Now you have connected:

```text
Process
   |
   v
Socket
   |
   v
TCP port 8080
   |
   v
HTTP
   |
   v
Client request
```

---

# Exercise 11 — Watch HTTP Traffic

Keep the Python server running:

```bash
python3 -m http.server 8080
```

Capture traffic:

```bash
sudo tcpdump -n -i lo port 8080
```

From another terminal:

```bash
curl http://127.0.0.1:8080
```

Now you can see actual packets generated by your command.

This is where Linux commands and networking start connecting together.

---

# Exercise 12 — Service Investigation

Suppose you discover:

```text
TCP 22 LISTEN
```

Your investigation could be:

```bash
ss -ltnp
```

Then:

```bash
lsof -i :22
```

Then:

```bash
ps aux | grep ssh
```

Then:

```bash
systemctl status ssh
```

Then:

```bash
journalctl -u ssh
```

You are following a logical chain:

```text
Port
 ↓
Process
 ↓
Service
 ↓
Logs
```

This way of thinking is more important than memorizing individual commands.

---

# 32. Final Cheat Sheet

## Identity

```bash
whoami
id
hostname
hostnamectl
uname -a
uptime -p
```

---

## Memory and System

```bash
free -h
vmstat 1
```

---

## Navigation

```bash
pwd
ls
ls -l
ls -a
ls -la
ls -F
ls -R
cd
cd ..
cd ~
```

---

## Files and Directories

```bash
mkdir
mkdir -p
touch
cp
cp -r
mv
rm
rm -i
rm -r
rm -f
rmdir
```

---

## Searching

```bash
find
locate
which
whereis
tree
```

---

## Reading Files

```bash
cat
less
head
tail
diff
man
```

---

## Filtering

```bash
grep
grep -w
grep -E
grep -iE
```

---

## Redirection

```bash
>
>>
|
```

---

## Archives

```bash
tar -cf
tar -czf
tar -xf
tar -xzf
```

---

## Processes

```bash
top
ps aux
kill
kill -9
jobs
bg
fg
```

---

## Permissions

```bash
chmod
chown
chown -R
umask
chmod u+s
chmod g+s
chmod +t
```

---

## Special Permission Search

```bash
find / -perm -4000 2>/dev/null
find / -perm -2000 2>/dev/null
```

---

## Users

```bash
useradd
useradd -m
userdel
userdel -r
usermod
groupadd
groupdel
passwd
passwd -l
passwd -u
passwd -S
groups
su -
id user
```

---

## Kernel

```bash
dmesg
dmesg | tail
dmesg | grep -iE 'error|warning|failed'
```

---

## Interfaces

```bash
hostname -I
ip a
ip -br a
ip link
ifconfig
```

---

## Routing

```bash
ip r
ip route
ip route show
route -n
```

---

## Connectivity

```bash
ping
traceroute
tracepath
nc -zv
```

---

## DNS

```bash
resolvectl status
cat /etc/resolv.conf
nslookup
dig
dig +short
```

---

## Ports

```bash
ss -tuln
ss -ltnp
ss -lunp
ss -tulnp
netstat -tuln
```

---

## Process ↔ Port

```bash
ss -lptn
lsof -i
lsof -i :80
fuser 80/tcp
```

---

## Layer 2

```bash
arp -a
ip neigh
```

---

## Firewall

```bash
iptables -L
iptables -L -n
iptables -L -n -v
ufw status
```

---

## Packet Capture

```bash
tcpdump -i eth0
tcpdump -n -i eth0
tcpdump -i eth0 icmp
tcpdump -i eth0 port 80
tcpdump -i eth0 -w capture.pcap
```

---

## Network Files

```bash
cat /etc/hosts
cat /etc/services
cat /etc/protocols
```

---

## HTTP

```bash
curl
curl -I
curl -i
wget
```

---

## Nmap

```bash
nmap -sS
nmap -sV
nmap -p-
nmap -A
```

---

## Services

```bash
systemctl status
systemctl start
systemctl stop
systemctl restart
systemctl enable
systemctl disable
```

---

## Logs

```bash
journalctl
journalctl -xe
journalctl -u ssh
journalctl -u nginx
```

---

## Bash

```bash
variables
$?
if
for
while
&&
||
alias
```

---

## Useful Advanced Commands

```bash
awk
watch
strace
lsof
ss
```

---

# The Most Important Mental Model

Do not think:

> I need to memorize hundreds of commands.

Think in questions.

```text
Who am I?
    ↓
whoami

What permissions do I have?
    ↓
id

Where am I?
    ↓
pwd

What files are here?
    ↓
ls

Where is a file?
    ↓
find

What does this file contain?
    ↓
cat / less

What processes are running?
    ↓
ps aux / top

What ports are listening?
    ↓
ss -tulnp

Which process owns this port?
    ↓
lsof / ss / fuser

What is my IP?
    ↓
ip a

Where will packets go?
    ↓
ip route

What MAC belongs to this local IP?
    ↓
ip neigh

What DNS server am I using?
    ↓
resolvectl / resolv.conf

Can I reach this host?
    ↓
ping

Can I reach this TCP port?
    ↓
nc -zv

What packets are moving?
    ↓
tcpdump

What service is running?
    ↓
systemctl

What happened to that service?
    ↓
journalctl
```

That is how Linux starts becoming logical.

---

# Recommended Learning Method

For every new command:

```text
1. Read what the command does.
2. Run it.
3. Read the output.
4. Change one option.
5. Predict what will change.
6. Run it again.
7. Explain the result using your own words.
8. Repeat it later without looking at this README.
```

For example:

Do not simply memorize:

```bash
ss -tulnp
```

Understand it:

```text
I am asking Linux to show TCP and UDP sockets,
especially listening sockets,
using numeric addresses,
and showing the associated process when possible.
```

That means you understand the command.

---

# Final Message

The Linux terminal is not a collection of mysterious commands.

It is a way to **ask the operating system questions**.

Once you understand the questions, the commands become much easier to remember.

```text
Observe
Understand
Experiment
Break things safely
Fix them
Repeat
```

And always remember:

> **Learn the command. Understand the output. Explain what it proves.**

---

## Author's Note

This repository was created as both:

- a personal Linux review;
- a beginner-friendly learning resource;
- a foundation for networking;
- a foundation for cybersecurity labs;
- a reference to return to when a command has been forgotten.

The goal is not to look advanced.

The goal is to understand the fundamentals well enough that advanced topics eventually make sense.

Happy hacking — in your own lab. 🐧
