# Lab Assignment 3

Due Monday, December 5th 4:59 pm.

## Part I:
Refer to [Port Scanning](./slide/port_scanning.pdf) on hints for using various
port scanning and packet sniffing tools.

## Part II:
Refer to [Stack Smashing](./slide/stack_smash.pdf) for hints on exploiting
stack overflow bugs.

The virtual address of "Magic cookie found!" string is 0x0809f268.

*28* is the minimum number of letters to overflow the buffer of the
[weak](./part2/weak) program.

To exploit the buffer overflow bug in the [weak](./part2/weak) program, run:
```bash
cd part2
python3 ./exploit.py -e ./weak -o buffer.bin
```
where the argument given to the *-e* flag is the *weak* program and the
argument given to the *-o* flag (*buffer.bin*) is the sequence of bytes used
to fill in the buffer.

To replicate the result afterwards, simply run:
```bash
cd part2
cat buffer.bin | ./weak
```
