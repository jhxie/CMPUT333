# Lab Assignment 2
Refer to [INSTRUCTIONS.pdf](./INSTRUCTIONS.pdf) for the assignment
instructions.

Due Friday, November 4th 4:59 pm.

To set up the proxy server, run:
```bash
./sshXX 1 CCID
```
where *CCID* needs to be replaced with the actual value.

**NOTE**:  
The password for the proxy server is the one given to you privately on a piece
of paper.

## Part I:
Refer to [VM Setup](./slide/vm_setup.pdf) for instructions on how to change
passwords for both virtual machines.

| Platform | Password  |
|:--------:|:---------:|
| Linux    | c333VMlab |
| Windows  | c333VMlab |

Linux *root* password = "c333VMlab" without quotation marks.
Windows *administrator* password = "c333VMlab" without quotation marks.

We can decide on better passwords later on for creating a strong password with
reasons behind the choice.

One of the TAs has posted a [link](
https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html#!s!xkcd)
that contains useful tips for choosing secure passwords.

## Part II:
Refer to [VM Setup](./slide/vm_setup.pdf) for instructions on how to
take snapshots of both virtual machines before doing anything else;
[Firewall Setup](./slide/firewall_setup.pdf) has hints on how to set up
**HTTP** and **FTP** service properly.

Recompiled Linux so that the correct iptables have been enabled.

Distinction between *Active* FTP versus *Passive* FTP can be read [here](
http://slacksite.com/other/ftp.html).

One of the TAs gives hints on how to set up **FTP** service on the Linux host:

> Some tips about setting up your FTP service.
> 
> 1) To start/restart your server you can use:
> 
> /etc/rc.d/rc.inetd start 
> 
> /etc/rc.d/rc.inetd restart 
> 
> OR
> 
> You can also modify your /etc/rc.d/rc.local file to start the service when
> the server boots up.
> 
> 2) Before you start your server make sure that you edit the hosts.allow
> and/or hosts.deny files accordingly, as well as the inetd.conf and of course
> the vsftpd.conf file.
> 
> In the third you just need to uncomment the:
> ftp     stream  tcp     nowait  root    /usr/sbin/tcpd  vsftpd
> 
> 3)Check with
> netstat -a | grep ftp
> or/and
> telnet localhost
> that your server is working.
> 
> 4) To see if you have configured your server correctly and that you can
> retrieve the file on your Linux VM with a get command
> (http://www.cs.colostate.edu/helpdocs/ftp.html) you can use: 
> 
> i)ftp localhost
> 
> ii)log in as anonymous or one of the users you have added
> 
> iii)use get to retrieve your pdf file
> 
> Pointers:
> 
> https://wiki.archlinux.org/index.php/Very\_Secure\_FTP\_Daemon
> 
> http://its.virginia.edu/unixsys/sec/hosts.html
> 
> Cheers,
> 
> Katia
