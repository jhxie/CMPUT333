## Part 1

### Step 1

#### Question a
The IP addresses of the victim hosts connected to the backbone are
*10.229.100.55*, *10.229.100.101*, and *10.229.100.102*.

The procedure used to discover those victim hosts are running the following
command on the linux firewall virtual machine (*cs333fw001*):
```bash
nmap 10.229.100.14-94
nmap 10.229.100.98-255
```
The reason for skipping IP address ranges *10.229.100.1-13* and
*10.229.100.95-97* is that those ranges belong to the hosts assigned to each
student group and designated machines used by TAs, respectively.

#### Question b
The services running on the victim host *10.229.100.55* are the following:

| PORT     |  STATE | SERVICE       | VERSION                                                       |
| -------- | ------ | ------------- | ------------------------------------------------------------- |
| 7/tcp    |  open  | echo          |                                                               |
| 9/tcp    |  open  | discard?      |                                                               |
| 13/tcp   |  open  | daytime?      |                                                               |
| 17/tcp   |  open  | qotd          | Windows qotd                                                  |
| 19/tcp   |  open  | chargen       |                                                               |
| 25/tcp   |  open  | smtp          | Microsoft ESMTP 5.0.2172.1                                    |
| 42/tcp   |  open  | wins          | Microsoft Windows Wins                                        |
| 53/tcp   |  open  | domain        | Microsoft DNS                                                 |
| 80/tcp   |  open  | http          | Microsoft IIS webserver 5.0                                   |
| 135/tcp  |  open  | msrpc         | Microsoft Windows RPC                                         |
| 139/tcp  |  open  | netbios-ssn   |                                                               |
| 445/tcp  |  open  | microsoft-ds  | Microsoft Windows 2000 microsoft-ds                           |
| 515/tcp  |  open  | printer       | Microsoft lpd                                                 |
| 548/tcp  |  open  | afpovertcp?   |                                                               |
| 1025/tcp |  open  | mstask        | Microsoft mstask (task server - c:\winnt\system32\Mstask.exe) |
| 1029/tcp |  open  | mstask        | Microsoft mstask (task server - c:\winnt\system32\Mstask.exe) |
| 1032/tcp |  open  | mstask        | Microsoft mstask (task server - c:\winnt\system32\Mstask.exe) |
| 1033/tcp |  open  | msrpc         | Microsoft Windows RPC                                         |
| 3372/tcp |  open  | msdtc?        |                                                               |
| 3389/tcp |  open  | microsoft-rdp | Microsoft Terminal Service                                    |
| 6142/tcp |  open  | http          | Microsoft IIS webserver 5.0                                   |

The services running on the victim host *10.229.100.101* are:

| PORT     | STATE | SERVICE    | VERSION         |
| -------- | ----- | ---------- | --------------- |
| 22/tcp   | open  | tcpwrapped |                 |
| 111/tcp  | open  | rpcbind    | 2 (rpc #100000) |
| 113/tcp  | open  | ident      | OpenBSD identd  |
| 6000/tcp | open  | X11        | (access denied) |

The services running on the victim host *10.229.100.102* are:

| PORT     | STATE | SERVICE    | VERSION         |
| -------- | ----- | ---------- | --------------- |
| 22/tcp   | open  | tcpwrapped |                 |
| 111/tcp  | open  | rpcbind    | 2 (rpc #100000) |
| 113/tcp  | open  | ident      | OpenBSD identd  |
| 6000/tcp | open  | X11        | (access denied) |

And the *nmap* commands used to determine the above information are:
```bash
nmap -A 10.229.100.14-94
nmap -A 10.229.100.98-255
```

#### Question c
The OS information for the victim host *10.229.100.55* are the following:

| Running                             | OS details                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Microsoft Windows 95/98/ME/NT/2K/XP | Microsoft Windows Millennium Edition (Me), Windows 2000 Professional or Advanced Server, or Windows XP |

The OS information for the victim host *10.229.100.101* are:

| Running                 | OS details                                 |
| ----------------------- | ------------------------------------------ |
| Linux 2.4.X/2.5.X/2.6.X | Linux 2.4.0 - 2.5.20, Linux 2.4.7 - 2.6.11 |

The OS information for the victim host *10.229.100.101* are:

| Running                 | OS details                                 |
| ----------------------- | ------------------------------------------ |
| Linux 2.4.X/2.5.X/2.6.X | Linux 2.4.0 - 2.5.20, Linux 2.4.7 - 2.6.11 |

And the *nmap* commands used to obtain the above information are exactly the
same as the ones used in the previous question:
```bash
nmap -A 10.229.100.14-94
nmap -A 10.229.100.98-255
```

### Step 2

#### Question a

#### Question b

#### Question c

#### Question d
