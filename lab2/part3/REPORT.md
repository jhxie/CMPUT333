## Part 3

*filter
:INPUT ACCEPT [51543:7837746]
:FORWARD ACCEPT [12430:583137]
:OUTPUT ACCEPT [60331:28515252]
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

allow loopback

-A INPUT -i lo -j ACCEPT

allow icmp and ping

-A INPUT -p icmp -j ACCEPT

HTTP
These set of rules are for http and dropping anything
that comes in from the ports listed below
The accept rule is to allow anything else with the given IP address

-A INPUT -p tcp --dport 8080 -s 10.229.100.13 -j DROP
-A INPUT -p tcp --dport 8080 -s 10.229.100.97 -j DROP
-A INPUT -p tcp --dport 8080 -s 10.229.97.0/24 -j DROP
-A INPUT -p tcp --dport 8080 -s 10.229.0.0/16 -j ACCEPT

SSH
this rule is to allow for ssh service to be allowed

-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT

FTP
These set of rules are for ftp and dropping anything
that comes in from the ports listed below
The accept rule is to allow anything else with the given IP address

-A INPUT -p tcp --dport 21 -s 10.229.100.2 -j DROP
-A INPUT -p tcp --dport 21 -s 10.229.100.96 -j DROP
-A INPUT -p tcp --dport 21 -s 10.229.96.0/24 -j DROP
-A INPUT -p tcp --dport 21 -s 10.229.0.0/16 -j ACCEPT

TFTP
These set of rules are for tftp and dropping anything
that comes in from the ports listed below
The accept rule is to allow anything else with the given IP address

-A INPUT -p tcp --dport 69 -s 10.229.100.3 -j DROP
-A INPUT -p tcp --dport 69 -s 10.229.100.96 -j DROP
-A INPUT -p tcp --dport 69 -s 10.229.96.0/24 -j DROP
-A INPUT -p tcp --dport 69 -s 10.229.0.0/16 -j ACCEPT

-A INPUT -p tcp -m state --state NEW -m tcp --dport 21 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 20 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 21 -j ACCEPT

#Windows Host
-A OUTPUT -p tcp -d 10.229.100.96 -j DROP
-A OUTPUT -p tcp -d 10.229.96.0/24 -j DROP
COMMIT
*nat

Port forward from 80 to 8080
this rule is to forward any requests from 80 to 8080 because our web server is only accessable through 8080

-A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.229.1.2:8080
COMMIT

### Reference
* [Choosing Secure Passwords](
https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html#!s!xkcd)
* `man 1 passwd`

### Division of Workload
The Windows HTTP server was set up by Stephen Arychuk, he also wrote the IP
table rules for part 3 and the report section for it; the sliding part of
assignment 1 was done by Jiahui Xie, he set up the Linux FTP/TFTP server and
wrote relevant reprot section.
