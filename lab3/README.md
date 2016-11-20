# Lab Assignment 3

Due Monday, December 5th 4:59 pm.

## Part I:
Refer to [Port Scanning](./slide/port_scanning.pdf) on hints for using various
port scanning and packet sniffing tools.

## Part II:
The virtual address of "Magic cookie found!" string is 0x0809f268.

*28* is the minimum number of letters to overflow the buffer of the
[weak](./part2/weak) program.

To find the minimum number of letters that caused overflow, run:
```bash
cd part2
python3 ./exploit.py -e ./weak
```
