## Part 2

### Question a

### Question b

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
press */* followed by *809f268* and <kbd>Enter</kbd> to find the address
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

### Question e

### Question f

### Question g
