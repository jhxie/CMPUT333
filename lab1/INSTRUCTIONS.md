# CMPUT 333, Assignment 1, Fall 2016

(weak encryption, cipher modes, weak passwords)

## Weak Encryption & Cipher Modes (75%)

### Part 1 (25%)

You are given an encrypted file ([`ciphertext1`](./part1/ciphertext1)). You
know that the plaintext that was encrypted was a text file and that it was
encrypted using a variation of the Vigenère cipher. The key can be a
combination of any printable ASCII characters. The way the encryption takes
place between a single plaintext byte, `p`, and a single key byte, `k`,
to produce a single ciphertext byte, `c`, can be summarized as follows:
First we split the key byte into the lower 4 bits (`kl`) and the higher 4
bits (`kh`). We split the plaintext byte to its lower 4 bits (`pl`) and
the higher 4 bits (`ph`). Likewise, we will generate the resulting
ciphertext from two parts, the lower 4 bits (`cl`) and the higher 4 bits
(`ch`).

    ch <- map[ph][kl]
    cl <- map[pl][kh]

where:

    map[16][16] = {
       {0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe}, 
       {0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0}, 
       {0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7}, 
       {0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa},  
       {0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4},      
       {0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3},     
       {0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1}, 
       {0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf}, 
       {0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2),                             
       {0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5},                             
       {0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb},                             
       {0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6},                              
       {0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8},                              
       {0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9},                              
       {0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd},                              
       {0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc} 
    };

Your tasks are to:

*   Show the plaintext corresponding to the ciphertext given, and the key that
was used to encrypt it.
*   Explain in your submission what technique(s) you used to determine the key
and why. Note that the use of exhaustive search receives poor marks with
respect to the technique used component.
*   Explain how you automated (if you did) the process of recognizing whether
you had the right key? (If you did not automate it, or automate it completely,
                        explain why not.)
*   Submit any source code you write to solve this problem. You are free to use
the language of your choice, but C is preferred. Regardless of your choice of
language, you must also submit a `README.txt` file explaining how to
compile/run your code on the lab machines. The information you provide should
be sufficient for us to replicate your solution process on the lab machines.
*   Answer this question: if the plaintext was first compressed using one of
the standard compression tools (`zip`, `gzip`, etc.) before it was encrypted,
how would your strategy have changed? Explain your answer.

### Part 2 (25%)

You are given another encrypted file ([`ciphertext2`](./part2/ciphertext2))
encrypted using the same scheme as before but using longer key than the first
one. You know that the plaintext file is not a regular text file, but some
other commonly used file format.

Your tasks are to:

*   Determine the plaintext corresponding to the ciphertext given, and the key
that was used to encrypt it.
*   Explain in your submission how you modified the technique you used in Part
1 to solve Part 2\. Exhaustive search would again receive poor marks.
*   Explain how you automated (if you did) the process of recognizing whether
you had the right key? (If you did not automate it, or automate it completely,
explain why not.)
*   Submit any additional source code you write specifically to solve this
problem. You are free to use the language of your choice, but C is preferred.
Again, provide in the accompanying `README.txt` a description of the steps
necessary to compile and run your code on lab machines, for us to replicate
your solution process.

In your answers make sure to comment on the benefits of known (partial)
plaintext. Identify the points where the known plaintext structure helps you in
the process of decrypting the ciphertext and recovering the key.

### Part 3 (25%)

In this part of the assignment you will experiment with the various cipher
modes of DES. You should review the definition of ECB, CBC, CFB, and OFB modes
of operation from the textbook.

*   Create a plaintext file consisting of 10 repetitions (without any
whitespace between them) of the (ASCII character) string: `01234567`
That is, your file length should be _exactly_ 80 characters long.
*   Encrypt the file with DES using the following command: `openssl enc -e
-des-XYZ -nosalt -in plaintext -out cipherXYZ.enc` where `XYZ` is `ecb`, `cbc`,
`cfb`, `ofb`. In total you have produced four new ciphertext files. You are
free to choose any encryption key you like (but you have to use the same key
for all encryptions) as long as you submit the key you used with your
assignment. All the ciphertext files should also be submitted.
*   Inspect the contents of the `.enc` files. Explain the differences (i) with
respect to their sizes vs. the plaintext files, and (ii) with respect to seeing
any patterns in their contents.
*   Now create an "error" version of each file (name these versions
`cipherXYZerror.enc` following the previous convention) by replacing the 19th
byte in each file by a different byte. These, modified,
files must also be submitted.
*   Try now to decrypt each of the `cipherXYZerror.enc` and write your
explanation about what was the impact of the "error" on the decryption outcome.

Note that explanation is not the same as observation. In responding to all the
questions, you must refer back to the precise aspect of the ECB, CBC, CFB or
OFB mode operation that caused the behavior you observed.

*   Finally, you are given an encrypted file ([`ciphertext3`](./ciphertext3)),
which you know has been encrypted using DES in ECB mode. You also know that the
plaintext is a sequence of thirteen 8-byte long names, one name after the other
(with no extra whitespace or separators between them). The plaintext file has
been generated using a conventional text editor, on a Unix system. To spice
things up, consider that these thirteen names are the names of the thirteen
groups in CMPUT 333, and that their order in the file represents their score in
an assignment. Assume the instructor leaked the information that your group is
in the 3rd position. Modify the given file, so that when it is decrypted your
group will be in the 1st position and the group that was in the first
position is going to be in the 6th position. Submit the modified file.

## Password Cracking (25%) [Sliding Part]

Each group will be provided separate password hashes files from Unix/Linux and
Windows/LANMAN.

*   You are to crack as many passwords as possible from the files. We suggest
that you employ at least a well known password cracking program, namely John
the Ripper [http://www.openwall.com/john/](http://www.openwall.com/john/) but
you are free to find and use additional tools if you feel it is necessary.
Clearly, if you need to use a different tool than the one recommended, you have
to indicate why it was a better choice. You have limited amount of time to
break the passwords (until the Assignment 1 sliding deadline), so you are
encouraged to use the best strategy you can come up with. Do not use any other
University computers for cracking the passwords or any personal computers. This
includes machines in other labs, the GPU login servers, etc.
*   If you find your initial strategy not producing results (i.e., cracking
passwords), you might want to consider the hints given and to study how you
could provide more appropriate wordlists and rules to John the Ripper. Hints
are given out in class.
*   Your report must indicate which passwords you cracked (what was the
plaintext of the passwords) and what kind of a strategy (if any) you followed.
*   Explain why the cracked passwords were weak passwords and, additionally,
compare and contrast the Windows and Unix passwords. Which ones were easier to
crack and why?

In the interest of fairness, the release of the passwords will take place at a
specific time and date, which will be pre-announced in class and/or via eclass.

## Deliverables

Only one of the group members need to submit on behalf of the entire group (in
the event of more than one submission, the last one will be considered).
The sliding part (and the sliding part only) can be submitted at any point in
time prior to the deadline for the (non-sliding) part of Assignment 2\. Your
submission must include a report file (in `.pdf` format) which includes answers
to the questions and should cite any resources that you used to answer the
questions. It is assumed that all group members equally contribute to the
assignment but you have to provide a paragraph in your report which explains
how you split the workload. If you need to deviate from this model ("all
equally contributing")
of cooperation, explain why and indicate who/what was responsible for what.

[Optional: add a single paragraph at the end of the report indicating whether
you found any difficulties with this assignment and if you think there are ways
in which it could be improved. In particular, we are interested to know if the
assignment forced you to learn something new that you did not know of before,
and how much effort it took you. Was the workload reasonable?]
