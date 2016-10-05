
ASM_DIR = asm/x$(AESNI_ARCH)
IAES = $(ASM_DIR)/iaesx$(AESNI_ARCH).s
RDTSC = $(ASM_DIR)/do_rdtsc.s
YASM = 

iaesx.o: $(IAES)
	$(YASM) -D__linux__ -g dwarf2 -f elf64 $(IAES) -o $@

rdtsc.o: $(RDTSC)
	$(YASM) -D__linux__ -g dwarf2 -f elf64 $(RDTSC) -o $@

aesni.o: iaes_asm_interface.h  iaesni.h  intel_aes.c
	$(CC) $(CFLAGS)   -Wall -Wdeclaration-after-statement -fomit-frame-pointer --param allow-store-data-races=0 -Wno-deprecated-declarations -Wno-format-extra-args -D_GNU_SOURCE -m64 -c intel_aes.c -o $@

all: iaesx.o rdtsc.o aesni.o

default: all

clean:

distclean: clean
	$(RM) Makefile
