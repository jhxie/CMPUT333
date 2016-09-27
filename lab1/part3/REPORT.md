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
padding: this allows a rudimentary integrity or password check to be
performed. If padding is disabled then the input data must be a multiple of the
cipher block length."

##### CBC

##### CFB

##### OFB


#### Content Differences

##### ECB
The encrypted output `cipherecb.enc` has a repeating pattern
`e0b1 304d a28a fd3b`, which corresponds to the repeating pattern of the
original file `3031 3233 3435 3637`.

##### CBC

##### CFB

##### OFB



### Question 4
### Question 5
### Question 6

### Reference
* `man 1 enc`
