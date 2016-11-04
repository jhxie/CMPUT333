## Assignment 1 Sliding Part

As group 1, the Unix hashes we are supposed to crack are:

> $1$03eQhEHr$VzfRY6Dc9MDNjKfTB8L/d0  
> $1$XRlLIqNU$PGziquQO.U2cYYkpjWZOS.  
> $1$z1Nk0xyf$sp/CDlMQNxhKw1Mn3kWmN.  
> $1$ENqxo5u0$81tdi0P3MAN9vAvUGHn6y.  
> $1$0gs0ZeaS$mAbjqR8ckVRYHCCHMRTBg.

The actual passwords are:

> flavius$aetius  
> UNKNOWN  
> misbehavior  
> UNKNOWN  
> UNKNOWN

Only the first and third is successfully cracked using word lists; the *Roman
General* one requires additional connectors (\_, $, %) to be added to each
name in the word list file to work properly.

The commands used are:
```bash
cd a1sliding
run/john --wordlist=list/roman.txt --rules hashes.txt
run/john --wordlist=list/11letterwords.txt --rules hashes.txt
run/john --show hashes.txt
```
where *hashes.txt* is the text file containing only the Unix passwords.

The Windows hashes we are supposed to crack are:

> D5D8E24F574290F9302D113D646B368F:9BA8384BD50192588AFF5F9B5F9625F0  
> 8AFC234E5BE7BB568963805A19B0ED49:9C9607EBF3287C06876D8FC44FDC711E  
> F4C310F5B3FAC8D63B1217229AE349BC:CB71BC560D760E506D1E96010DFDA970

The actual passwords are:

> UNKNOWN  
> gondolier  
> UNKNOWN  

Similar to the Unix hashes, only word lists are used to crack the second
hash.

The commands used are:
```bash
run/john --wordlist=list/9letterwords.txt -format=LM --rules first_half.txt
run/john --wordlist=list/9letterwords.txt -format=nt --rules second_half.txt
```
In this case, the three Windows hashes are break into two separate files named
*first_half.txt* and *second_half.txt* because the encryption schemes used are
different for each portion of the Windows hashes.

### Explanation
All 3 cracked password hashes are variations of English words that can be
easily tried one by one given a dictionary file; therefore they are all weak
passwords. One of the Unix and Windows passwords are composed entirely of
alphanumeric letters and no result has been returned from *john the ripper*
(running *incremental mode*) up until the deadline of this sliding part since
they are very computationlly expensive to try out all possible permutations
even length is known.

For the passwords that we have cracked, the Windows one (*gondolier*) and the
11-letter word password of Unix (*misbehavior*) are easier to crack than the
*Roman General* password of Unix (*flavius$aetius*) because the former two
can be *directly* cracked given word lists; however, for the *Roman General*
case, each name needs to apply *three* different modifications based on the
connectors.
