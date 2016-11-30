## Assignment 2 Sliding Part

### Question 1

Password to key files is "KitHpwuaaUni". Created a private/public key of 4096 bits long. "ca.crt" is the Certificate Authorities crt, "ca.key" is the Certificate Authorities key.

### Question 2

"server.csr" is the Servers Certificate request.

### Question 3

"server.crt" is the Servers crt for used in the Apache Server, and "server.key" is the Servers key.

Insert impact of not including policy_anything.

### Question 4

Modifying the http-ssl.conf file located in the Apache files, edit the <Virtualhost> fields such that you include the needed SSL requirements. Look into the apache files to gather correct items.

### Question 5

Screenshot of web server not recognizing the certificate is called "BeforeCertificate.png". 

![Before Certificate](./BeforeCertificate.png)

*Get Screenshot of importing the certificate into the webserver.

Screenshot of web server successfully loading in the certificate is called "AfterCertificate.png"

![After Certificate](./AfterCertificate.png)

Explain the different file types encountered, what each type is used for and why it is needed.

.crt --	Digitial Certificate file.

.key -- Key

.csr -- Certificate Signing Request file.

Outline any problems that arrived.

### Question 6

Write up the process of	how to generate signed Java code and explain what is the purpose of each step (WHY each step is needed). What (if any) are the differences with respect to the web server certificates?