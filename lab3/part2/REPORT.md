## Part 2

### Question a
The *weak* program takes one command line argument and use that to greet the
user; then it prompts one-line input, upon receiving an response after the user
has hitten the <kbd>Enter</kbd> key, it converts the first 12 letters of the
input to upper-case if they are lower-case letters; or it converts them to
lower-case if the first 12 letters are upper-case; lastly it echos back the
input given by the user after conversion and exits.

### Question b
The buffer size used by the *weak* program is 27, assuming the ending new line
does not count as a special letter.
This size is found by the *exploit.py* program as follows: at start it will
give a one-letter input to the *weak* program and repeatedly double the length
of input until a *SIGSEGV* signal is delivered to the *weak* program; the
current length of input is set to be the upper bound of the candidate buffer
size, then the *exploit.py* program also sets the half of this upper bound to
be the lower bound of the buffer size and starts running a binary search
algorithm using the upper and lower bound found; lastly it will report the
minimum number of letters (in this case *28*) that caused a *SIGSEGV* signal to
be delivered, which suggests that the actual buffer size is one less than that
size.

### Question c
To find the function that print the string *Magic cookie found!*, first find
the starting address of the *.rodata* section:
```bash
readelf -S ./weak
```
from the output it shows the starting address of *.rodata* section for the
*weak* program is *0809f260* (in the *Addr* column).

Next, find the offset of the string within *.rodata* section:
```bash
readelf -p .rodata ./weak | grep 'Magic cookie found!'
```
the number shown in square brackets is the offset of the string; in this case
it is *8*.

Now the address of the string literal can be calculated by adding the offset to
the starting address of *.rodata* section: 8 + 809f260 = 809f268

Lastly search for the address *809f268* in the disassembly output:
```bash
objdump -S ./weak|less
```
press <kbd>/</kbd> followed by *809f268* and <kbd>Enter</kbd> to find the address
reference in the pager; the only reference is at *804822d* in the *.text*
section: *804822d:       68 68 f2 09 08          push   $0x809f268*

The next instruction after this is *call*, the address given to *call* is
very likely to belong to *printf* function; but in order to get to this point
in the program, we need to find the starting address of this subroutine block:
scrolling back in the pager we can see that the most recent address that
involves a backup of *ebp* register is: *8048224:       55 push   %ebp*, the
instructions above this one are *nop* and *ret*, so this address is definitely
the starting address of this subroutine (function) block.

To call the address *8048224*, or in **Little Endian** byte series form:
*0x24 0x82 0x04 0x08*, we need to overflow the buffer in a way such that the
return address of the stack frame that containing the buffer is overwritten by
this byte series.

### Question d
The source code of the exploit is named **exploit.py** and resides under the
*part2* sub-directory.

### Question e

### Question f

### Question g
