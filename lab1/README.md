# Lab Assignment 1
**NOTE**:  
Refer to [REPORT.pdf](./REPORT.pdf) for answers to each part.

Due Monday, October 3rd 4:59 pm.

Refer to either [INSTRUCTIONS.html](./INSTRUCTIONS.html) or
[INSTRUCTIONS.md](./INSTRUCTIONS.md) for the assignment instructions.

Please record the answer for each part in a separate file named
`REPORT.md` and place them inside the corresponding subdirectories:
[part1](./part1/), [part2](./part2/), and [part3](./part3/).

To generate the compiled report markdown file, make sure all 3
`REPORT.md` files are placed properly, then issue:
```bash
sh ./reportCompile.sh
```

## Part I
**NOTE**:  
For marking purpose, please use implementation A; implementation B does not
have password cracking functionality at all.

Refer to the [Viginere Cipher](./slide/viginere_cipher.pdf) and
[Deciphering](./slide/deciphering.pdf) for hints on part I.

Currently there are two implementations available:  
Source code for implementation A can be viewed [here](./part1/part1.py),  
implementation B can be viewed [here](./part1/vigenere.py)

### Usage Info for Implementation A
The correct key can be deduced by running:
```bash
cd lab1/part1/
python ./part1.py ciphertext1 output
```
and then followed by an answer of '7' in the prompt.

### Usage Info for Implementation B
To encrypt a file using the special variant of Vigenere cipher specified in
the lab slide:
```bash
cd lab1/part1/
python3 ./vigenere.py input_file.txt -e output_file.txt -k 'cipher'
```
here the key used is 'cipher', the file to be encrypted is 'input\_file.txt',
and the encrypted output file is 'output\_file.txt'.

To decrypt a file:
```bash
python3 ./vigenere.py output_file.txt -d decrypted.txt -k 'cipher'
```

## Part II
**NOTE**:  
For marking purpose, please ignore the file type detector since it does not
have password cracking functionality at all.

Refer to the [File Signatures](./slide/file_signatures.pdf) for hints on
part II.

### Usage Info for File Type Detector
```bash
cd lab1/part2/
python3 ./detect.py test1.doc test2.docx test3.pdf
```

### Usage Info for Header Keys and Decryption
This will first print to the terminal the partial keys for each of the
hardcoded file signatures, and then it will use the hardcoded key we found (as
described in the report for part 2) to decrypt input\_file and write the result
to output\_file.
```bash
cd lab1/part2/
python3 ./part2.1.py input_file output_file
```

## Part III & Sliding Part
Refer to the [Password Cracking](./slide/password_cracking.pdf) for hints on
part III and sliding part.

## Sliding Part
Refer to the ["Screen Usage"](./slide/screen.pdf) for hints on the usage of
the "screen" program for sliding part.

### Hint
A connector can be any of the following: \_, $, %

### The Unix password hashes are:

> $1$03eQhEHr$VzfRY6Dc9MDNjKfTB8L/d0  
> $1$XRlLIqNU$PGziquQO.U2cYYkpjWZOS.  
> $1$z1Nk0xyf$sp/CDlMQNxhKw1Mn3kWmN.  
> $1$ENqxo5u0$81tdi0P3MAN9vAvUGHn6y.  
> $1$0gs0ZeaS$mAbjqR8ckVRYHCCHMRTBg.

### The Windows password hashes are:

> D5D8E24F574290F9302D113D646B368F:9BA8384BD50192588AFF5F9B5F9625F0  
> 8AFC234E5BE7BB568963805A19B0ED49:9C9607EBF3287C06876D8FC44FDC711E  
> F4C310F5B3FAC8D63B1217229AE349BC:CB71BC560D760E506D1E96010DFDA970

