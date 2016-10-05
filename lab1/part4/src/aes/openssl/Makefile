
CC = gcc
CXX = @CXX@
AS = gcc
LD = gcc
CPP = gcc
CFLAGS = -g -O2 -I/usr/local/include -I/usr/local/cuda/include -DARCH_LITTLE_ENDIAN=1   -Wall -Wdeclaration-after-statement -fomit-frame-pointer --param allow-store-data-races=0 -Wno-deprecated-declarations -Wno-format-extra-args -D_GNU_SOURCE  
ASFLAGS =  -DARCH_LITTLE_ENDIAN=1 -c 
LDFLAGS =  -L/usr/local/lib -L/usr/local/cuda/lib64 -lssl -lcrypto  

ossl_aes.o: ossl_aes.c ossl_aes.h
	$(CC) $(CFLAGS) -c ossl_aes.c -o $@

default: ossl_aes.o
all: ossl_aes.o

clean:

distclean: clean
	$(RM) Makefile
