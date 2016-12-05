# Lab Assignment 3
**NOTE**:  
Refer to [REPORT.pdf](./REPORT.pdf) for compiled report of answers to each
part.

To generate this file, issue:
```bash
bash ./reportCompile.sh
```

Due Monday, December 5th 4:59 pm.

## Sliding Part of Assignment 2
**NOTE**:
The markdown report can he viewed [here](./a2sliding/REPORT.md).

## Part I:
**NOTE**:  
The captured results are [image.jpg](./image.jpg) and [sound.mp3](./sound.mp3).
The markdown report can be viewed [here](./part1/REPORT.md)

To inspect both the compressed *pcap* files, do the following:
```bash
tar xJf arp.tar.xz
tar xJf arp2.tar.xz
```
then use *wireshark* to open both *arp.pcap* and *arp2.pcap* files.

Refer to [Port Scanning](./slide/port_scanning.pdf) on hints for using various
port scanning and packet sniffing tools.

## Part II:
**NOTE**:  
The markdown report can be viewed [here](./part1/REPORT.md)

Refer to [Stack Smashing](./slide/stack_smash.pdf) for hints on exploiting
stack overflow bugs.

The virtual address of "Magic cookie found!" string is 0x0809f268.

*28* is the minimum number of letters (bytes) to overflow the buffer of the
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
