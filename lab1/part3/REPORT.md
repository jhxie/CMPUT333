## Part 3

### Question 1
The plaintext file consisting of 10 repetitions of the string `01234567`
is named as `plaintext`.

### Question 2
The encryption key used for all the cipher modes of **DES** is `nosalt`; and
the corresponding encrypted outputs for the 4 modes of **DES** are named as
`cipherecb.enc`, `ciphercbc.enc`, `ciphercfb.enc`, and `cipherofb.enc`,
respectively.

### Question 3

#### Size Differences

##### ECB
The encrypted output `cipherecb.enc` is 8 bytes larger than the original
`plaintext` due to the extra 8-byte-padding added by `openssl` using the
PKCS5 scheme, which is enabled by default for block ciphers.
Source quoted from the `enc` manual page of `openssl`:
All the block ciphers normally use PKCS#5 padding also known as standard block
padding: this allows a rudimentary integrity or password check to be performed.
If padding is disabled then the input data must be a multiple of the cipher
block length."

##### CBC
The encrypted output `ciphercbc.enc` is 8 bytes larger than the original
`plaintext` due to the extra 8-byte-padding added by `openssl` using the
PKCS5 scheme, similar to the reason given for the **ECB** mode.

##### CFB
The encrypted output `ciphercfb.enc` is of the same size as the original
`plaintext` file (80 bytes) because the final size of output ciphertext
blocks is the same as the plaintext and there is no padding bytes added by
`openssl`.

##### OFB
The encrypted output `cipherofb.enc` is of the same size as the original
`plaintext` file (80 bytes) because the final size of output ciphertext
blocks is the same as the plaintext and there is no padding bytes added by
`openssl`.

#### Content Differences

##### ECB
The encrypted output `cipherecb.enc` has a repeating pattern
`e0b1 304d a28a fd3b`, which corresponds to the repeating pattern of the
original file `3031 3233 3435 3637`.

##### CBC, CFB, OFB
The encrypted output files `ciphercbc.enc`, `ciphercfb.enc`, and
`cipherofb.enc` does not have any repeating pattern possibly because `openssl`
makes changes to the IV (initialization vector, it is not explicitly specifed
as a commnad line arguemnt), which results in the same repeating plaintext
**01234567** being enciphered to a different output.

### Question 4
The "error" version of each file is named `cipherecberror.enc`,
`ciphercbcerror.enc`, `ciphercfberror.enc`, `cipherofberror.enc`, respectively.

### Question 5
The decrypted output files are named as `plaintextecb`, `plaintextcbc`,
`plaintextcfb`, and `plaintextofb`, respectively.

##### ECB
After decryption, only the *third* **01234567** block is corrupted because
blocks are enciphered **independently** of other blocks in the **ECB** mode;
in this case the 19th corrupted byte belongs to the *third* 64-bit (8-byte)
block, only this block is affected after decipherment.

##### CBC
After decryption, the *third* and *fourth* **01234567** blocks are both
corrupted: the difference is that the 19th byte error propagates to the
entire *third* block but only the third byte in the *fourth* block (*2*) is
affected. The reason for this is that the 19th byte is the *third* byte within
the *third* (64-bit) block, in **CBC** mode a byte error in ciphertext block
j affects decipherment of blocks j and j + 1; however, the extra *xor*
(exclusive or) operation during decryption between cipher block j and j + 1
(in the case the *third* and *fourth* block) would preserve the exact location
of the byte error in j + 1 plaintext block (in this case the *third* byte in
the *fourth* block).

##### CFB
After decryption, the *third* and *fourth* **01234567** blocks are both
corrupted: this time only the 19th byte (corrupted byte) is affcted in the
*third* block but the error also propagates to the entire *fourth* block.
The reason for this similar scenario with respect to the **CBC** case is that
the decryption of **CFB** mode is almost identical to the **CBC** encryption
performed in reverse: after the *xor* operation for decryption the byte error
is preserved in the exact location in block j (the *third* block in this case)
but propagates to the whole j + 1 block (the *fourth* block).

##### OFB
After decryption, only the 19th byte (corrupted byte) is affected because the
**OFB** mode does not have chaining dependencies among blocks, and there is a
final *xor* (exclusive or) operation involved to decipher the plaintext from
the ciphertext. In this case the original encrypted 19th byte is **0x3e**,
the bitmask used to corrupt it is **0x5f**, so to obtain the correct plaintext,
an extra *xor* operation needs to be performed between the corrupted plaintext
byte **0x6d** and the bitmask used previously.

### Question 6
The modified file is named as `ciphertext3.mod`.

### Reference
* `man 1 enc`
* Chapter 7 of the Handbook of Applied Cryptography
