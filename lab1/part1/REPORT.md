## Part 1

### Question 1

In the file names "plaintext1" is the resulting plaintext from the decrypted file "ciphertext1". They key is 7 characters long in the hex order "{0x50},{0x2F},{0x08},{0x7C},{0x5F},{0x30},{0x00}".

### Question 2

From the ciphertext, we used Kasiski's examination to correctly find the length of the key. We found the distances between certain groups of lettering and then calculating the factors based on the length of distance. E.g. the grouping "76 b5 6e" appears multiple times in the ciphertext and the distances between some of them are is at least 21. Combining this with other character groupings we can calculate the common factor between all of them to be 7. Therefore the key length is 7. 

Once the key length was found, we then split up the ciphertext into 7 "bins" such that each bin had the first character of the first row and then the remaining characters following by multiples of 7. 

| Bin 1 | Bin 2 | Bin 3 | Bin 4 | Bin 5 | Bin 6 | Bin 7 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|   1   |   2   |   3   |   4   |   5   |   6   |   7   |
|   8   |   9   |  10   |  11   |  12   |  13   |  14   |
|  15   |  16   |  17   |  18   |  19   |  20   |  21   |

We then take the first and second character from the first bin and calculate all possible keys for each and pull out the keys that exist in both lists. This creates a "master list" of possible keys for this bin. Take the third key and calculate all possible keys and compare to the master list for similarities and take only the ones that exist in both. Do this until we only have possible key left that will decrypt the entire bin. Repeat for the rest of the bins. This will give us the full key.

### Question 3

By using the method in question 2, we can determine whether we have a possible key by outputting the calculated key afterwards. The program will then immediately start decrypting the ciphertext using the newly found key and start outputting it into the output file provided during execution. We can then open the output file to determine if the whole file is readable as the plaintext should be printable ASCII characters.

### Question 4

See README.md or REPORT.pdf for compilation and execution.

### Question 5

If the plaintext file had been first compressed then the strategy would have been similar to part 2. Since zip files also have file header information in it that will determine what the file should be, we can use this information to find out how large the uncompressed file is, what the name of it is, etc. The only place that we could use Kasiski's examination is in the last part of the file where we can calculate the the distances of the file header. 

### Reference

https://en.wikipedia.org/wiki/Zip_(file_format)

https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Kasiski_examination
