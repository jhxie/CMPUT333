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
give a one-letter (which is of one-byte length) input to the *weak* program and
repeatedly double the length of input until a *SIGSEGV* signal is delivered to
the *weak* program; the current length of input is set to be the upper bound of
the candidate buffer size, then the *exploit.py* program also sets the half of
this upper bound to be the lower bound of the buffer size and starts running a
binary search algorithm using the upper and lower bound found; lastly it will
report the minimum number of letters (or bytes, in this case *28*) that caused
a *SIGSEGV* signal to be delivered, which suggests that the actual buffer size
is one less than that size.

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
press <kbd>/</kbd> followed by *809f268* and <kbd>Enter</kbd> to find the
address reference in the pager; the only reference is at *804822d* in the
*.text* section: *804822d:       68 68 f2 09 08          push   $0x809f268*

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
As explained in question *b*, the **exploit.py** program finds the minimum
number of bytes (*28*) that caused the *weak* program to crash via *SIGSEGV*
signal through a binary search algorithm implemented in the *buffer_exploit*
function; and after it is successfully found, it appends two addresses
immediately after the 28 padding bytes (*0* in this case) that point to
the beginning location of the secret printing function (procedure to find it
is described in question *c*) and the exit function (procedure to find it is
described in question *f*) respectively, in order to *try to* overwrite the
back-up return address on the stack; turns out in this case after inputting
28 bytes the following bytes that are written after that will actually change
the return address of the input-requesting function based on observing the
*core dump* produced by the program through the following steps:

```bash
cd part2
python3 ./exploit.py -e ./weak -o buffer.bin
cat buffer.bin | ./weak
gdb ./weak core
```

note the binary content writing process is carried out on line *83* in the
*exploit.py* script; after finding that simply by appending the *"secret_byte"*
right after 28 bytes are written:
```python
padding_byte * buffer_size + secret_byte
```
where the multiplication part stands for repeating the *"padding_byte"*
*"buffer_size"* number of times.

The instruction pointer changes correspondingly when observing the address
printed by *gdb* based on the *core* file; so at this point the byte sequence
for *"secret_byte"* is simply changed to the address (*8048224*) found in
question *c* in order to make the program jump to this location upon the return
of the input-requesting function.

### Question f
Based on the observation made in question *c*, the virtual address for the
*printf* function (*call   0x8048f10* instruction after *push   $0x809f268*)
can actually be located within the binary itself, a situation in which suggests
that the binary is statically compiled, and this guess is further verified
through the *ldd* command:

```bash
cd part2
ldd ./weak
```

the output of it shows *"not a dynamic executable"*, hence it is a static
executable.

Since this is a *statically compiled* executable, the actual C library wrapper
for *system calls* can be located within the virtual address space of the
executable as well; after looking at the linux kernel documentation on system
calls, it becomes clear that the platform-specific system call table (in this
case *i386*) can be viewed in the kernel source directory:
*"linux/arch/x86/entry/syscalls/syscall_32.tbl"*

The system calls that are of interest are anything that relates to *exit*;
after searching for the keyword *exit*, the only two entries that match the
keyword are:

| System Call Number | ABI  | System Call Name | Entry Point    |
| ------------------ | ---- | ---------------- | -------------- |
| 1                  | i386 | exit             | sys_exit       |
| 252                | i386 | exit_group       | sys_exit_group |

Based on the calling convention described in the *"x86 Assembly: Interfacing
with Linux"* article, to locate the above two system calls in the assembly code
of *weak* program, we need to find cases where *int $0x80* kernel trap
instruction is issued and either one of the two above system call numbers are
placed into the *eax* register.

The hexadicimal representation for the system call number *1* and *252* are
*1* and *fc*, respectively; turns out the only case involves the above
calling pattern is at virtual address beginning at *8050dfc* and ending with
*8050e0f*:

```assembly
mov    0x4(%esp),%ebx
mov    $0xfc,%eax
int    $0x80
mov    $0x1,%eax
int    $0x80
hlt
nop
```

To jump to the address *8050dfc* after the secret-printing function returns,
all needs to be done is to continue overwriting past the input buffer such
that the return address for the secret-printing function becomes *8050dfc*;
to achieve this effect *"exit_byte"* is set to the starting address of this
block in **Little Endian** form *0xfc 0x0d 0x05 0x08*, so the final binary
content that used for buffer overflow is constructed as

```python
padding_byte * buffer_size + secret_byte + exit_byte
```
and the program indeed exits without receiving *SIGSEGV* signal.

### Reference
* [Linux Kernel Documentation on System Calls](
https://github.com/torvalds/linux/blob/master/Documentation/adding-syscalls.txt)
* [Linux x86 32-bit System Call Table](
https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_32.tbl)
* [x86 Assembly: Interfacing with Linux](
https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux)
* [Wireshark User's Guide](
https://www.wireshark.org/docs/wsug_html_chunked/)
* `man 1 ettercap`
* `man 1 nmap`

### Division of Workload
