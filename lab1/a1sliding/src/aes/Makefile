
CC = gcc
CXX = @CXX@
AS = gcc
LD = gcc
CPP = gcc
CFLAGS = -g -O2 -I/usr/local/include -I/usr/local/cuda/include -DARCH_LITTLE_ENDIAN=1   -Wall -Wdeclaration-after-statement -fomit-frame-pointer --param allow-store-data-races=0 -Wno-deprecated-declarations -Wno-format-extra-args -D_GNU_SOURCE  
ASFLAGS =  -DARCH_LITTLE_ENDIAN=1 -c 
LDFLAGS =  -L/usr/local/lib -L/usr/local/cuda/lib64 -lssl -lcrypto  
YASM = 
AR = /usr/bin/ar
FIND = /usr/bin/find
RM = /bin/rm -f
GCCV44 := $(shell expr `$(CC) -dumpversion` \>= 4.4)
USE_AESNI = linux

AESIN = aes.o openssl/ossl_aes.o
SUBDIRS = openssl
ifeq "$(GCCV44)" "1"
	ifneq "$(YASM)" ""
		ifdef USE_AESNI
			ifdef AESNI_ARCH
				AESIN += aesni/*.o
				SUBDIRS += aesni
				AESNI_DEC = -DAESNI_IN_USE=1
			endif
		endif
	endif
endif

aes.o: aes.c aes.h aes_func.h
	$(CC) $(CFLAGS) $(AESNI_DEC) -c aes.c -o aes.o

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ all

aes.a: $(SUBDIRS) aes.o
	$(AR) -r $@ $(AESIN)

default: aes.a
all: aes.a

clean:
	$(FIND) . -name \*.a -exec rm {} \;
	$(FIND) . -name \*.o -exec rm {} \;

distclean: clean
	$(RM) Makefile
	$(RM) aesni/Makefile
	$(RM) openssl/Makefile
