# Lab Assignment 2
**NOTE**:  
Refer to [REPORT.pdf](./REPORT.pdf) for answers to each part.

Due Friday, November 4th 4:59 pm.

Refer to [INSTRUCTIONS.pdf](./INSTRUCTIONS.pdf) for the assignment
instructions.

To set up the proxy server, run:
```bash
./sshXX 1 CCID
```
where *CCID* needs to be replaced with the actual value.

**NOTE**:  
The password for the proxy server is the one given to you privately on a piece
of paper.

Please record the answer for each part in a separate file named
`REPORT.md` and place them inside the corresponding subdirectories:
[part1](./part1/), [part2](./part2/), [part3](./part3/), and [a1sliding](
../lab1/a1sliding/).

To generate the compiled report markdown file, make sure all 3
`REPORT.md` files are placed properly, then issue:
```bash
sh ./reportCompile.sh
```

## Part I:
Refer to [VM Setup](./slide/vm_setup.pdf) for instructions on how to change
passwords for both virtual machines.

| Platform | Administrator/Root Password  | User1 Password | User2 Password |
| -------- | ---------------------------- | -------------- | -------------- |
| Linux    | 9%0byu(zY                    | v1-#>;/jf      | 9up]~z@qm      |
| Windows  | sCSsd54>ttH                  | O3gmDtc        | mPrm8hbeenUsG  |

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
> https://wiki.archlinux.org/index.php/Very_Secure_FTP_Daemon
> 
> http://its.virginia.edu/unixsys/sec/hosts.html
> 
> Cheers,
> 
> Katia

For testing whether **FTP** and **HTTP** services are set up properly:

> You should now be able to use the script retrieve_files.pl which will attempt
> both an http request and an ftp request to your machine.
> 
> To trigger an http request (to your windows VM) and an ftp request (to your
> linux VM), you need to log onto your linux VM and run the following command:
> 
> curl http://10.229.100.XX/cgi-bin/retrieve_files.pl
> 
> where XX can be either 96 or 97. 
> 
> 
> This will start by attempting to retrieve webcontent.html from your windows
> VM. Once it successful grabs webcontent.html or unsuccessfully times out, it
> will then make an ftp request to your linux VM to grab ftpcontent.pdf, first
> using active ftp, and then using passive ftp. (Note: if your http service is
> not correctly set up, you'll have to wait a few minutes for the request to
> time out before it attempts the ftp requests). 
> 
> You can also trigger scan.pl to do a port scan of your machine as well from
> your linux VM using:
> 
> curl 10.229.100.XX/cgi-bin/scan.pl
> 
> where XX can be either 96 or 97. 
> 
> Remember: the port scan of the windows machine will take longer than the
> linux machine --- this is normal.
> 
> If you have any questions, as always don't hesitate to post to the forums or
> talk to myself or Mark.
> 
> Cheers,
> 
> Katia
