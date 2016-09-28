# Lab Assignment 1

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
To encrypt a file using the special variant of Vigen¨¨re cipher specified in
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
Refer to the [File Signatures](./slide/file_signatures.pdf) for hints on
part II.

### Usage Info for File Type Detector
```bash
cd lab1/part2/
python3 ./part2.py test1.doc test2.docx test3.pdf
```

## Part III & Sliding Part
Refer to the [Password Cracking](./slide/password_cracking.pdf) for hints on
part III and sliding part.

## Sliding Part
Refer to the ["Screen Usage"](./slide/screen.pdf) for hints on the usage of
the "screen" program for sliding part.
