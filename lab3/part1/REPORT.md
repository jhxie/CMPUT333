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

| Port     | State  | Service       | Version                                                       |
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

| Port     | State | Service    | Version         |
| -------- | ----- | ---------- | --------------- |
| 22/tcp   | open  | tcpwrapped |                 |
| 111/tcp  | open  | rpcbind    | 2 (rpc #100000) |
| 113/tcp  | open  | ident      | OpenBSD identd  |
| 6000/tcp | open  | X11        | (access denied) |

The services running on the victim host *10.229.100.102* are:

| Port     | State | Service    | Version         |
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

The victim hosts can be determined by following the instructions shown in step
one.

To capture the network traffic through ARP poisoning among three victim hosts
*10.229.100.55*, *10.229.100.101*, and *10.229.100.102*, issue the following
*ettercap* command:
```bash
ettercap -Q -T -w arp.pcap -M arp /10.229.100.55,101,102/
```
in this case the captured output is recorded in a file named *arp.pcap*; later
on either **Wireshark** or **tcpdump** can be used to analyze the network
traffic based on this file.

#### Question b
The connections initiated among three victim hosts are a series of **HTTP**
requests, the extracted repeating communication pattern is recorded in the
following table (note the *frame number* are for reference only):

| Frame Number | Source         | Destination    | Source Role | Destination Role |
| ------------ | -------------- | -------------- | ----------- | ---------------- |
| 457          | 10.229.100.101 | 10.229.100.55  | HTTP Client | HTTP Server      |
| 48590        | 10.229.100.102 | 10.229.100.55  | HTTP Client | HTTP Server      |

Within the thirty minutes of the *ettercap* run, host *10.229.100.101* sends
**HTTP GET** request to the **HTTP** server at *10.229.100.55* to get a file
named */Test2016/sound.mp3* on a regular basis while the other host
*10.229.100.102* sends another **HTTP GET** request to the **HTTP** server at
*10.229.100.55* to get a different file named */Test2016/image.jpg* from time
to time.

#### Question c

#### Question d
