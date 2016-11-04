## Part 2

The passwords for the Linux machine are chosen to be composed entirely of
random alphanumveric letters due to the fact that the only feasible way to
crack the random alphanumeric password hashes for the sliding part of
assignment 1 is to use the *brute force* incremental mode of *john the ripper*
program, which is the most computationally expensive to calculate due to the
large number of permutations to try one by one.

For the Windows machine they are memorable sentences using a combination
of alphanumeric letters and a symbol in one case. Windows Admin password is
derived from "some Computing Science students don't Sleep for more then thirty
hours". Windows user1 is derived from "Our third group member Dropped the
course". Windows User2 is derived from "my Poor room mate has been Unemployed
since Graduation".

Windows web server is done through the addition of a module called mod_auth_sspi
where it can pull windows credentials from the OS directly. This allows it to edit
the web server config file that can require the login credentials from the user
depending on which directory that they are trying to access.