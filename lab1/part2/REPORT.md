## Part 2

### Question 1

The decrypted file is given as "output.jpg". The key is 23 characters long, given by these hexadecimal bytes:

{0x35, 0x33, 0x2E, 0x35, 0x30, 0x33, 0x35, 0x36, 0x33, 0x4E, 0x2C, 0x2D, 0x31, 0x31, 0x33, 0x2E, 0x35, 0x32, 0x38, 0x38, 0x39, 0x34, 0x57}

### Question 2

Similar to part 1, we used Kasiski's examination to see if we could find the length of the key. The distances between groupings of characters was siginificantly larger than in part 1, but after enough evaluation we found that 23 occurred frequently as a common factor. We then used the code from part 1 to evaluate ciphertext2, splitting it instead into 23 "bins", but the evaluation was unsuccessful and the code from part 1 was unable to find a key.

Here we realized we needed to deviate from our solution to part 1. We knew that being able to figure out what file type the plaintext is would be able to help us, so we looked at a range of different file signatures. Seeing as how the header for any file is a known plaintext, we used that, the ciphertext, and the given mapping to determine what the first bytes of the key would have to be if the plaintext were each file type.

Knowing the plaintext is supposed to be a common file type, we looked at file signatures for DOCX, DOC, PDF, PS, PNG, and JPG files and found what the keys would have to be if the plaintext were any of those. Seeing as how we know the key is limited in this part to printable ASCII characters (0x20 to 0x7f), we were able to immediately eliminate all of the file types we had picked but several JPG ones, as the partial keys for their headers all had at least one non-printable ASCII character in them. From the reference site we found six common options for the first four bytes of a JPG, three of which we were able to eliminate as their keys had a non-printable ASCII character in them.

Left with either a Samsung D807 JPEG file, Standard JPEG/Exif file, or Still Picture Interchange File Format (SPIFF) as potential headers, we decided to examine the ciphertext using each of the three combinations of initial four key bytes. We went through the first 10,000 ciphertext bytes decrypting every four with a potential key. In this way bytes 0-3 would be decrypted, then 1-4, then 2-5, and so on. The idea is that if we do in fact have the initial four bytes of the key, then at some point a decryption of four bytes should make sense and we would have a fairly good idea about the key length.

We looked at the hexadecimal of several JPGs we had to get a feel for the file structure, particularly to note anything that stood out. Two that really stood out early on in each were a timestamp and the occurrence of a bunch of 2s all in sequence. We ran the decryption with the three different JPG formats, and with the Standard JPEG/Exif file we got promising results. At the 575th byte we noticed the sequence of 4 bytes looked like it could be from a timestamp, so we then doubled that number and checked the 1150th byte to find a sequence of four 2s. We realized then that 575 was divisible by 23, so this with our findings from Kasiski's examination early on led us to believe the key length had to be 23 and that we had found the file type.

Having a strong hunch about what kind of JPG we were dealing with we looked at the full file signature which is 11 bytes long (where the 5th and 6th bytes are unknown). We then decrypted the whole ciphertext2 using a 23 byte key with the 9 bytes we knew filled in (and the others left as garbage). Taking a look at the hex dump of the decryption we could see in greater detail where the sequence of 2s was, and so knowing that the bytes we didn't have the key for in between two groupings of 2s should definitely be 2s, we had a known plaintext and ciphertext. We were able to then find the missing key bytes, and with the completed key we then decrypted the whole ciphertext.

### Question 3

We mostly calculated the key manually, using code to help with mapping and decryption. Once we had what we felt was the key, we gave it to the code to decrypt ciphertext2 with and output the result to "output.jpg". As we got a clear picture from the result we knew we had the right key and the right file format. The pattern recognition parts of finding and verifying the key would have been far too difficult to try to code and automate in any effective way, so we stuck with manually doing it for the most part, only using code to help with the simple but tedious tasks of mapping and decryption.

### Question 4

See README.md in lab1 for compilation and execution.

### Reference

http://www.garykessler.net/library/file_sigs.html
