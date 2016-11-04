#
# This file is part of John the Ripper password cracker,
# Copyright (c) 1996-2014 by Solar Designer
#
# ...with changes in the jumbo patch, by various authors
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted.
#
# There's ABSOLUTELY NO WARRANTY, express or implied.
#
# This file converted into autoconf format by JimF and
# magnum, in 2014. That is still a work in progress.
#


CC = gcc
PTHREAD_CC = gcc
ifdef PTHREAD_CC
CC = gcc
endif
AS = gcc
LD = gcc
CPP = gcc -E
CP = cp
CP_PRESERVE = cp -p
LN = ln -s
RM = rm -f
MKDIR = /bin/mkdir -p
TR = tr
SED = /bin/sed
NULL = /dev/null
SORT = /usr/bin/sort
STRIP = strip

SHELL = /bin/sh


subdirs = aes escrypt
top_srcdir = .
srcdir = .
prefix = ../run
exec_prefix = ${prefix}
bindir = $(exec_prefix)/bin
infodir = $(prefix)/info
libdir = $(prefix)/lib/gnudl
mandir = $(prefix)/man/man1

# CUDA settings. See output of "nvcc -h"
NVCC_FLAGS = -c -Xptxas -v -fmad=true

CPPFLAGS =  -I/usr/local/include -I/usr/local/cuda/include
CFLAGSX = -c -g -O2 -I/usr/local/include -I/usr/local/cuda/include -DARCH_LITTLE_ENDIAN=1   -Wall -Wdeclaration-after-statement -fomit-frame-pointer --param allow-store-data-races=0 -Wno-deprecated-declarations -Wno-format-extra-args -D_GNU_SOURCE     -fopenmp  -pthread $(RELEASE_BLD)
# CFLAGS for use on the main john.c file only
CFLAGS_MAIN = -DAC_BUILT  $(CFLAGSX)
CFLAGS = -DAC_BUILT -march=native -msse4.1 $(CFLAGSX)
ASFLAGS = -DAC_BUILT  -DARCH_LITTLE_ENDIAN=1 -march=native -msse4.1 -c -fopenmp  
LIBS = 
LDFLAGS = -g  -L/usr/local/lib -L/usr/local/cuda/lib64 $(LIBS) 
#
OPT_NORMAL =  -funroll-loops
OPT_INLINE =  -Os -funroll-loops -finline-functions
#

PLUGFORMATS_OBJS = 7z_fmt_plug.o BFEgg_fmt_plug.o DMD5_fmt_plug.o DOMINOSEC_fmt_plug.o EPI_fmt_plug.o FGT_fmt_plug.o HDAA_fmt_plug.o IPB2_fmt_plug.o KRB4_fmt_plug.o KRB4_std_plug.o KRB5_fmt_plug.o KRB5_std_plug.o KeccakDuplex_plug.o KeccakF-1600-opt32_plug.o KeccakF-1600-opt64_plug.o KeccakNISTInterface_plug.o KeccakSponge_plug.o MSCHAPv2_bs_fmt_plug.o NETLM_fmt_plug.o NETLMv2_fmt_plug.o NETNTLM_bs_fmt_plug.o NETNTLMv2_fmt_plug.o NETSPLITLM_fmt_plug.o NS_fmt_plug.o NT_fmt_plug.o PHPS_fmt_plug.o PO_fmt_plug.o SKEY_fmt_plug.o SKEY_jtr_plug.o SybaseASE_fmt_plug.o SybasePROP_fmt_plug.o XSHA512_fmt_plug.o XSHA_fmt_plug.o agilekeychain_fmt_plug.o aix_smd5_fmt_plug.o aix_ssha_fmt_plug.o androidfde_fmt_plug.o asaMD5_fmt_plug.o bcrypt_pbkdf_plug.o bitcoin_fmt_plug.o blackberry_ES10_fmt_plug.o blake2b-ref_plug.o blake2b_plug.o blf_plug.o blockchain_fmt_plug.o chap_fmt_plug.o citrix_ns_fmt_plug.o clipperz_srp_fmt_plug.o cloudkeychain_fmt_plug.o common_opencl_pbkdf2_plug.o cq_fmt_plug.o crc32_fmt_plug.o crypt-sha1_fmt_plug.o cryptsha256_fmt_plug.o cryptsha512_fmt_plug.o cuda_cryptmd5_fmt_plug.o cuda_cryptsha256_fmt_plug.o cuda_cryptsha512_fmt_plug.o cuda_mscash2_fmt_plug.o cuda_mscash_fmt_plug.o cuda_phpass_fmt_plug.o cuda_pwsafe_fmt_plug.o cuda_rawsha512_fmt_plug.o cuda_wpapsk_fmt_plug.o cuda_xsha512_fmt_plug.o dahua_fmt_plug.o django_fmt_plug.o django_scrypt_fmt_plug.o dmg_fmt_plug.o dragonfly3_fmt_plug.o dragonfly4_fmt_plug.o drupal7_fmt_plug.o ecryptfs_fmt_plug.o efs_fmt_plug.o eigrp_fmt_plug.o encfs_fmt_plug.o episerver_fmt_plug.o feal8_plug.o formspring_fmt_plug.o gost_fmt_plug.o gpg_fmt_plug.o haval_fmt_plug.o haval_plug.o hmacMD5_fmt_plug.o hmacSHA1_fmt_plug.o hmacSHA224_fmt_plug.o hmacSHA256_fmt_plug.o hmacSHA384_fmt_plug.o hmacSHA512_fmt_plug.o hmailserver_fmt_plug.o hsrp_fmt_plug.o idea_plug.o ike_fmt_plug.o keepass_fmt_plug.o keychain_fmt_plug.o keyring_fmt_plug.o keystore_fmt_plug.o known_hosts_fmt_plug.o krb5-18_fmt_plug.o krb5pa-md5_fmt_plug.o krb5pa-sha1_fmt_plug.o kwallet_fmt_plug.o lastpass_sniffed_fmt_plug.o lotus5_fmt_plug.o lotus85_fmt_plug.o luks_fmt_plug.o md2_fmt_plug.o md2_plug.o md4_gen_fmt_plug.o mdc2_fmt_plug.o mdc2dgst_plug.o mediawiki_fmt_plug.o mongodb_fmt_plug.o mozilla_ng_fmt_plug.o mscash1_fmt_plug.o mscash2_fmt_plug.o mssql-old_fmt_plug.o mssql05_fmt_plug.o mssql12_fmt_plug.o mysqlSHA1_fmt_plug.o mysql_fmt_plug.o mysql_netauth_fmt_plug.o net_md5_fmt_plug.o net_sha1_fmt_plug.o nsldap_fmt_plug.o nt2_fmt_plug.o ntlmv1_mschapv2_fmt_plug.o nukedclan_fmt_plug.o o5logon_fmt_plug.o odf_fmt_plug.o office_fmt_plug.o oldoffice_fmt_plug.o openbsdsoftraid_fmt_plug.o opencl_7z_fmt_plug.o opencl_DES_bs_b_plug.o opencl_DES_bs_plug.o opencl_DES_fmt_plug.o opencl_agilekeychain_fmt_plug.o opencl_bf_fmt_plug.o opencl_bf_std_plug.o opencl_blockchain_fmt_plug.o opencl_cryptmd5_fmt_plug.o opencl_cryptsha256_fmt_plug.o opencl_cryptsha512_fmt_plug.o opencl_dmg_fmt_plug.o opencl_encfs_fmt_plug.o opencl_gpg_fmt_plug.o opencl_keychain_fmt_plug.o opencl_keyring_fmt_plug.o opencl_krb5pa-md5_fmt_plug.o opencl_krb5pa-sha1_fmt_plug.o opencl_lotus5_fmt_plug.o opencl_mscash2_fmt_plug.o opencl_mysqlsha1_fmt_plug.o opencl_nsldaps_fmt_plug.o opencl_nt_fmt_plug.o opencl_ntlmv2_fmt_plug.o opencl_o5logon_fmt_plug.o opencl_odf_aes_fmt_plug.o opencl_odf_fmt_plug.o opencl_office2007_fmt_plug.o opencl_office2010_fmt_plug.o opencl_office2013_fmt_plug.o opencl_oldoffice_fmt_plug.o opencl_pbkdf2_hmac_sha1_fmt_plug.o opencl_pbkdf2_hmac_sha256_fmt_plug.o opencl_pbkdf2_hmac_sha512_fmt_plug.o opencl_phpass_fmt_plug.o opencl_pwsafe_fmt_plug.o opencl_rakp_fmt_plug.o opencl_rar5_fmt_plug.o opencl_rar_fmt_plug.o opencl_rawmd4_fmt_plug.o opencl_rawmd5_fmt_plug.o opencl_rawsha1_fmt_plug.o opencl_rawsha256_fmt_plug.o opencl_rawsha512_fmt_plug.o opencl_sha1crypt_fmt_plug.o opencl_sha2_common_plug.o opencl_strip_fmt_plug.o opencl_sxc_fmt_plug.o opencl_wpapsk_fmt_plug.o opencl_zip_fmt_plug.o openssl_enc_fmt_plug.o oracle11_fmt_plug.o oracle_fmt_plug.o osc_fmt_plug.o panama_fmt_plug.o panama_plug.o pbkdf2-hmac-sha1_fmt_plug.o pbkdf2-hmac-sha512_fmt_plug.o pbkdf2_hmac_sha256_fmt_plug.o pdf_fmt_plug.o pdfcrack_md5_plug.o pfx_fmt_plug.o phpassMD5_fmt_plug.o pixMD5_fmt_plug.o pkzip_fmt_plug.o pkzip_plug.o postgres_fmt_plug.o pst_fmt_plug.o putty_fmt_plug.o pwsafe_fmt_plug.o racf_fmt_plug.o radmin_fmt_plug.o rakp_fmt_plug.o rar5_fmt_plug.o rar_fmt_plug.o rawBLAKE2_512_fmt_plug.o rawKeccak_256_fmt_plug.o rawKeccak_512_fmt_plug.o rawMD4_fmt_plug.o rawMD5_fmt_plug.o rawSHA0_fmt_plug.o rawSHA1_fmt_plug.o rawSHA1_linkedIn_fmt_plug.o rawSHA1_ng_fmt_plug.o rawSHA224_fmt_plug.o rawSHA256_fmt_plug.o rawSHA256_ng_fmt_plug.o rawSHA384_fmt_plug.o rawSHA512_fmt_plug.o rawSHA512_ng_fmt_plug.o rawmd5u_fmt_plug.o ripemd_fmt_plug.o ripemd_plug.o rsvp_fmt_plug.o salted_sha1_fmt_plug.o sapB_fmt_plug.o sapG_fmt_plug.o sha1_gen_fmt_plug.o siemens-s7_fmt_plug.o sip_fmt_plug.o skein_fmt_plug.o skein_plug.o snefru_fmt_plug.o snefru_plug.o ssh_fmt_plug.o ssh_ng_fmt_plug.o ssha512_fmt_plug.o strip_fmt_plug.o sunmd5_fmt_plug.o sxc_fmt_plug.o syb-prop_repro_plug.o tcp_md5_fmt_plug.o tiger_fmt_plug.o tiger_plug.o truecrypt_fmt_plug.o twofish_plug.o uaf_encode_plug.o vms_fmt_plug.o vnc_fmt_plug.o vtp_fmt_plug.o wbb3_fmt_plug.o whirlpool_fmt_plug.o whirlpool_plug.o wow_srp_fmt_plug.o wpapsk_fmt_plug.o zip_fmt_plug.o

JOHN_OBJS = \
	jumbo.o john-mpi.o \
	DES_fmt.o DES_std.o DES_bs.o DES_bs_b.o \
	BSDI_fmt.o \
	MD5_fmt.o MD5_std.o \
	BF_fmt.o BF_std.o \
	scrypt_fmt.o \
	escrypt/crypto_scrypt-best.o escrypt/crypto_scrypt-common.o \
	escrypt/sha256.o \
	AFS_fmt.o \
	LM_fmt.o \
	trip_fmt.o \
	timer.o \
	md5_go.o \
	md5.o \
	rc4.o \
	hmacmd5.o \
	base64.o base64_convert.o \
	md4.o sha2.o \
	dynamic_fmt.o dynamic_parser.o dynamic_preloads.o dynamic_utils.o dynamic_big_crypt.o \
	ssh2john.o \
	pfx2john.o \
	unrarcmd.o unrarfilter.o unrarhlp.o unrar.o unrarppm.o unrarvm.o \
	rar2john.o \
	zip2john.o gladman_hmac.o gladman_pwd2key.o \
	racf2john.o \
	keychain2john.o \
	kwallet2john.o \
	pwsafe2john.o \
	dmg2john.o \
	keepass2john.o \
	keyring2john.o keystore2john.o \
	truecrypt_volume2john.o \
	hccap2john.o \
	$(PLUGFORMATS_OBJS) \
	plugin.o \
	dyna_salt.o dummy.o \
	gost.o \
	common-gpu.o \
	batch.o bench.o charset.o common.o compiler.o config.o cracker.o \
	crc32.o external.o formats.o getopt.o idle.o inc.o john.o list.o \
	loader.o logger.o mask.o math.o memory.o misc.o options.o params.o \
	path.o recovery.o rpp.o rules.o signals.o single.o status.o tty.o \
	wordlist.o \
	mkv.o mkvlib.o \
	listconf.o \
	fake_salts.o \
	win32_memmap.o \
	unicode.o \
	unshadow.o \
	unafs.o \
	undrop.o \
	regex.o \
	c3_fmt.o \
	unique.o putty2john.o gpg2john.o memdbg.o

OCL_OBJS = common-opencl.o opencl_autotune.o

CUDA_OBJS = common-cuda.o cuda_common.o cuda_cryptmd5.o cuda_phpass.o \
	cuda_cryptsha256.o cuda_cryptsha512.o cuda_mscash2.o \
	cuda_rawsha256.o cuda_rawsha224.o cuda_mscash.o \
	cuda_xsha512.o cuda_wpapsk.o cuda_rawsha512.o cuda_pwsafe.o \
	cuda_rawsha224_fmt.o cuda_rawsha256_fmt.o

GENMKVPWD_OBJS = \
	genmkvpwd.o mkvlib.o memory.o miscnl.o path.o memdbg.o

PROJ = ../run/john ../run/unshadow ../run/unafs ../run/unique ../run/undrop \
	../run/ssh2john ../run/rar2john ../run/zip2john \
	../run/genmkvpwd ../run/mkvcalcproba ../run/calc_stat \
	../run/tgtsnarf ../run/racf2john ../run/hccap2john \
	../run/pwsafe2john ../run/raw2dyna ../run/keepass2john ../run/pfx2john \
	../run/keychain2john ../run/keyring2john ../run/kwallet2john \
	../run/dmg2john ../run/putty2john ../run/uaf2john \
	../run/truecrypt_volume2john ../run/keystore2john ../run/wpapcap2john \
	../run/gpg2john ../run/cprepair ../run/luks2john ../run/base64conv

WITH_PCAP = 
ifdef WITH_PCAP
PROJ += ../run/SIPdump ../run/vncpcap2john
endif

WITH_CUDA = 
ifdef WITH_CUDA
NVCC = 
CCBIN = 
ifdef CCBIN
NVCC_FLAGS += -m64 -ccbin=$(CCBIN)
endif
JOHN_OBJS += $(CUDA_OBJS)
endif

WITH_OPENCL=
ifdef WITH_OPENCL
CFLAGS += -DHAVE_OPENCL 
CFLAGS_MAIN += -DHAVE_OPENCL 
JOHN_OBJS += $(OCL_OBJS)
endif

#########################################################
# this is what ./configure && make
# gets you. NOTE, we have to do the link in ./configure.
#   ** DONE $(LN) x86-sse.h arch.h or $(LN) x86-64 arch.h
# for now, in my testing, this is hard coded to x86-32.h
# NOTE, we also need to add extra .o file's some how.
#  ** DONE x86-64.o sse-intrinsics.o for 64 bit
#  ** DONE x86.o x86-sse.o sha1-mmx.o md4-mmx.o md5-mmx.o sse-intrinsics.o  for 32 bit:
#
# for ssexi builds:
# x86-64.o sse-intrinsics-64.o for 64 bit
# x86.o x86-sse.o sha1-mmx.o md4-mmx.o md5-mmx.o sse-intrinsics-32.o  for 32 bit:
#   and add -DUSING_ICC_S_FILE to CFLAGS
#
#  also need to figure out -DUNDERSCORES and add to ASFLAGS
#  also need to figure out -mpreferred-stack-boundary=4 and add (or whatever the stack size is)
#
#########################################################
default:
	$(MAKE) $(PROJ) \
		JOHN_OBJS="$(JOHN_OBJS) x86-64.o sse-intrinsics.o" \
		AESNI_ARCH=64
ifdef WITH_OPENCL
	$(MKDIR) ../run/kernels/
	$(CP_PRESERVE) opencl/*.cl ../run/kernels/
	$(CP_PRESERVE) opencl_*.h ../run/kernels/
endif
	@echo
	@echo Make process completed.

#########################################################
## This is the 'END' of the main default make target.
#########################################################

# Default build is always using -g (stripped when 'make install') but this
# target turns off optimizations for better debugging, and defines DEBUG
# so code can adopt.
debug:
	$(MAKE) default CFLAGS="-DDEBUG $(CFLAGS) -O0" CFLAGS_MAIN="-DDEBUG $(CFLAGS_MAIN) -O0"

# Similar but just turn memdbg on instead, and normal optimizations.
memdbg:
	$(MAKE) default CFLAGS="-DMEMDBG_ON $(CFLAGS)" CFLAGS_MAIN="-DMEMDBG_ON $(CFLAGS_MAIN)"
memdbg_ex:
	$(MAKE) default CFLAGS="-DMEMDBG_ON -DMEMDBG_EXTRA_CHECKS $(CFLAGS)" CFLAGS_MAIN="-DMEMDBG_ON -DMEMDBG_EXTRA_CHECKS $(CFLAGS_MAIN)"

help:
	@echo "The 'older' fat makefile can be done with make --file=Makefile.legacy [target]"

# Digital/Compaq's cc and make use the .S suffix for a different purpose...
digipaq-alpha.o: alpha.S
	$(CPP) $(CPPFLAGS) alpha.S > tmp.s
	$(AS) $(ASFLAGS) tmp.s -o digipaq-alpha.o
	$(RM) tmp.s

cuda_common.o:	cuda/cuda_common.cuh cuda/cuda_common.cu
	cd cuda; $(NVCC) $(NVCC_FLAGS) cuda_common.cu -o ../cuda_common.o

cuda_cryptmd5.o:  cuda_cryptmd5.h cuda/cryptmd5.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) cryptmd5.cu -o ../cuda_cryptmd5.o

cuda_phpass.o:  cuda_phpass.h cuda/phpass.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) phpass.cu -o ../cuda_phpass.o

cuda_cryptsha256.o:  cuda_cryptsha256.h cuda/cryptsha256.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) cryptsha256.cu -o ../cuda_cryptsha256.o

cuda_cryptsha512.o:  cuda_cryptsha512.h cuda/cryptsha512.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) cryptsha512.cu -o ../cuda_cryptsha512.o

cuda_mscash2.o:  cuda_mscash2.h cuda/mscash2.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) mscash2.cu -o ../cuda_mscash2.o

cuda_mscash.o:  cuda_mscash.h cuda/mscash.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) mscash.cu -o ../cuda_mscash.o

cuda_rawsha256.o:  cuda_rawsha256.h cuda/rawsha256.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) -DSHA256 rawsha256.cu -o ../cuda_rawsha256.o

cuda_rawsha256_fmt.o: cuda_rawsha256.o cuda_rawsha256_fmt.c
	$(CC)  $(CFLAGS) -DSHA256 cuda_rawsha256_fmt.c -o cuda_rawsha256_fmt.o

cuda_rawsha224.o:  cuda_rawsha256.h cuda/rawsha256.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) -DSHA224 rawsha256.cu -o ../cuda_rawsha224.o

cuda_rawsha224_fmt.o: cuda_rawsha224.o cuda_rawsha256_fmt.c
	$(CC)  $(CFLAGS) -DSHA224 cuda_rawsha256_fmt.c -o cuda_rawsha224_fmt.o

cuda_xsha512.o: cuda_xsha512.h cuda/xsha512.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) xsha512.cu -o ../cuda_xsha512.o

cuda_wpapsk.o:  cuda_wpapsk.h cuda/wpapsk.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) wpapsk.cu -o ../cuda_wpapsk.o

cuda_rawsha512.o: cuda_rawsha512.h cuda/rawsha512.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) rawsha512.cu -o ../cuda_rawsha512.o

cuda_pwsafe.o: cuda_pwsafe.h cuda/pwsafe.cu cuda_common.o
	cd cuda; $(NVCC) $(NVCC_FLAGS) pwsafe.cu -o ../cuda_pwsafe.o

SUBDIRS = aes

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ all

# Inlining the S-boxes produces faster code as long as they fit in the cache.
DES_bs_b.o: DES_bs_b.c sboxes.c nonstd.c sboxes-s.c
	$(CC) $(CFLAGS) $(OPT_INLINE) DES_bs_b.c

miscnl.o: misc.c
	$(CC) $(CFLAGS) $(OPT_NORMAL) -D_JOHN_MISC_NO_LOG misc.c -o miscnl.o

###############################################################################
#  Process targets.  Note, these are *nix targets, but also work fine under
#  cygwin.  The only problem with cygwin, is that the ln -s will NOT generate
#  a valid exe which can be run under native Win32 cmd shell
#  If a use wants that behavior, then run configure, with --enable-ln-s
#  By default, it is set to cygwin will use the .EXE symlink.c building,
#  where the macro EXE_EXT is .exe.  Mingw builds always set EXE_EXT to .exe
###############################################################################

# PTHREAD_CFLAGS and OPENMP_CFLAGS may actually contain linker options,
# like -fopenmp
../run/john: $(JOHN_OBJS) $(SUBDIRS)
	$(LD) $(JOHN_OBJS) $(LDFLAGS) -lssl -lcrypto    -fopenmp -lgmp     -pthread  -lm -lz -ldl -lcrypt  -lbz2 aes/aes.a -o ../run/john

../run/unshadow: ../run/john
	$(RM) ../run/unshadow
	$(LN) john ../run/unshadow

../run/unafs: ../run/john
	$(RM) ../run/unafs
	$(LN) john ../run/unafs

../run/undrop: ../run/john
	$(RM) ../run/undrop
	$(LN) john ../run/undrop

../run/ssh2john: ../run/john
	$(RM) ../run/ssh2john
	$(LN) john ../run/ssh2john

../run/putty2john: ../run/john
	$(RM) ../run/putty2john
	$(LN) john ../run/putty2john

../run/pfx2john: ../run/john
	$(RM) ../run/pfx2john
	$(LN) john ../run/pfx2john

../run/keepass2john: ../run/john
	$(RM) ../run/keepass2john
	$(LN) john ../run/keepass2john

../run/keyring2john: ../run/john
	$(RM) ../run/keyring2john
	$(LN) john ../run/keyring2john

../run/zip2john: ../run/john
	$(RM) ../run/zip2john
	$(LN) john ../run/zip2john

../run/gpg2john: ../run/john
	$(RM) ../run/gpg2john
	$(LN) john ../run/gpg2john

../run/rar2john: ../run/john
	$(RM) ../run/rar2john
	$(LN) john ../run/rar2john

../run/racf2john: ../run/john
	$(RM) ../run/racf2john
	$(LN) john ../run/racf2john

../run/keychain2john: ../run/john
	$(RM) ../run/keychain2john
	$(LN) john ../run/keychain2john

../run/kwallet2john: ../run/john
	$(RM) ../run/kwallet2john
	$(LN) john ../run/kwallet2john

../run/pwsafe2john: ../run/john
	$(RM) ../run/pwsafe2john
	$(LN) john ../run/pwsafe2john

../run/dmg2john: ../run/john
	$(RM) ../run/dmg2john
	$(LN) john ../run/dmg2john

../run/hccap2john: ../run/john
	$(RM) ../run/hccap2john
	$(LN) john ../run/hccap2john

../run/base64conv: ../run/john
	$(RM) ../run/base64conv
	$(LN) john ../run/base64conv

../run/truecrypt_volume2john: ../run/john
	$(RM) ../run/truecrypt_volume2john
	$(LN) john ../run/truecrypt_volume2john

../run/keystore2john: ../run/john
	$(RM) ../run/keystore2john
	$(LN) john ../run/keystore2john

../run/unique: ../run/john
	$(RM) ../run/unique
	$(LN) john ../run/unique

#####################################################################
# These targets MUST match ALL of the john targets that use ln -s
# These are built for Win32, so that we have a 'native' symlink back
# to the john exe.  The john exe is still built fat, but there is no
# workable ln -s, so we have built a 'symlink.c' file. It works in
# a limited way, like symlink. Mingw and default cygwin use these.
# cygwin can override this within ./configure using --enable-ln-s
#####################################################################
../run/unshadow.exe: symlink.c
	$(CC) symlink.c -o ../run/unshadow.exe
	$(STRIP) ../run/unshadow.exe

../run/unafs.exe: symlink.c
	$(CC) symlink.c -o ../run/unafs.exe
	$(STRIP) ../run/unafs.exe

../run/undrop.exe: symlink.c
	$(CC) symlink.c -o ../run/undrop.exe
	$(STRIP) ../run/undrop.exe

../run/ssh2john.exe: symlink.c
	$(CC) symlink.c -o ../run/ssh2john.exe
	$(STRIP) ../run/ssh2john.exe

../run/putty2john.exe: symlink.c
	$(CC) symlink.c -o ../run/putty2john.exe
	$(STRIP) ../run/putty2john.exe

../run/pfx2john.exe: symlink.c
	$(CC) symlink.c -o ../run/pfx2john.exe
	$(STRIP) ../run/pfx2john.exe

../run/keepass2john.exe: symlink.c
	$(CC) symlink.c -o ../run/keepass2john.exe
	$(STRIP) ../run/keepass2john.exe

../run/keyring2john.exe: symlink.c
	$(CC) symlink.c -o ../run/keyring2john.exe
	$(STRIP) ../run/keyring2john.exe

../run/zip2john.exe: symlink.c
	$(CC) symlink.c -o ../run/zip2john.exe
	$(STRIP) ../run/zip2john.exe

../run/gpg2john.exe: symlink.c
	$(CC) symlink.c -o ../run/gpg2john.exe
	$(STRIP) ../run/gpg2john.exe

../run/rar2john.exe: symlink.c
	$(CC) symlink.c -o ../run/rar2john.exe
	$(STRIP) ../run/rar2john.exe

../run/racf2john.exe: symlink.c
	$(CC) symlink.c -o ../run/racf2john.exe
	$(STRIP) ../run/racf2john.exe

../run/keychain2john.exe: symlink.c
	$(CC) symlink.c -o ../run/keychain2john.exe
	$(STRIP) ../run/keychain2john.exe

../run/kwallet2john.exe: symlink.c
	$(CC) symlink.c -o ../run/kwallet2john.exe
	$(STRIP) ../run/kwallet2john.exe

../run/pwsafe2john.exe: symlink.c
	$(CC) symlink.c -o ../run/pwsafe2john.exe
	$(STRIP) ../run/pwsafe2john.exe

../run/dmg2john.exe: symlink.c
	$(CC) symlink.c -o ../run/dmg2john.exe
	$(STRIP) ../run/dmg2john.exe

../run/hccap2john.exe: symlink.c
	$(CC) symlink.c -o ../run/hccap2john.exe
	$(STRIP) ../run/hccap2john.exe

../run/base64conv.exe: symlink.c
	$(CC) symlink.c -o ../run/base64conv.exe
	$(STRIP) ../run/base64conv.exe

../run/truecrypt_volume2john.exe: symlink.c
	$(CC) symlink.c -o ../run/truecrypt_volume2john.exe
	$(STRIP) ../run/truecrypt_volume2john.exe

../run/keystore2john.exe: symlink.c
	$(CC) symlink.c -o ../run/keystore2john.exe
	$(STRIP) ../run/keystore2john.exe

../run/unique.exe: symlink.c
	$(CC) symlink.c -o ../run/unique.exe
	$(STRIP) ../run/unique.exe

########################################################
# Not linked to symlink for a .exe file, so simply make
# single targets, using the EXE_EXT macro
########################################################
../run/genmkvpwd: $(GENMKVPWD_OBJS)
	$(LD) $(GENMKVPWD_OBJS) $(LDFLAGS) -lm -fopenmp -o ../run/genmkvpwd

../run/mkvcalcproba: mkvcalcproba.o
	$(LD) mkvcalcproba.o memdbg.o $(LDFLAGS) -lm -fopenmp -o ../run/mkvcalcproba

../run/calc_stat: calc_stat.o
	$(LD) calc_stat.o memdbg.o $(LDFLAGS) -lm -fopenmp -o ../run/calc_stat

../run/raw2dyna: raw2dyna.o
	$(LD) raw2dyna.o memdbg.o $(LDFLAGS) -fopenmp -o ../run/raw2dyna

../run/SIPdump: SIPdump.o
	$(LD) SIPdump.o memdbg.o $(LDFLAGS)  -fopenmp -o ../run/SIPdump

../run/vncpcap2john: vncpcap2john.o
	$(CC) -DAC_BUILT -Wall vncpcap2john.o memdbg.o $(LDFLAGS)  -fopenmp -o ../run/vncpcap2john

../run/uaf2john: uaf2john.o uaf_encode_plug.o
	$(LD) $(LDFLAGS) -pthread  uaf2john.o uaf_encode_plug.o memdbg.o -fopenmp -o ../run/uaf2john

# Note that this is NOT depending on PCAP lib. It is self-contained.
../run/wpapcap2john: wpapcap2john.o
	$(LD) $(LDFLAGS) wpapcap2john.o memdbg.o -fopenmp -o ../run/wpapcap2john

../run/luks2john: luks2john.o
	$(LD) ${LDFLAGS} luks2john.o -lssl -lcrypto   memdbg.o jumbo.o -fopenmp -o ../run/luks2john

../run/cprepair: cprepair.c unicode.c unicode.h options.h misc.h misc.c \
	memdbg.h memdbg.c
	$(CC) -DAC_BUILT -Wall -O3   -Wall -Wdeclaration-after-statement -fomit-frame-pointer --param allow-store-data-races=0 -Wno-deprecated-declarations -Wno-format-extra-args -D_GNU_SOURCE   -DNOT_JOHN -D_JOHN_MISC_NO_LOG cprepair.c unicode.c \
	misc.c memdbg.c -o ../run/cprepair

../run/tgtsnarf: tgtsnarf.o
	$(LD) tgtsnarf.o memdbg.o $(LDFLAGS) -fopenmp -o ../run/tgtsnarf

john.o: john.c fmt_externs.h fmt_registers.h
	$(CC) $(CFLAGS_MAIN) $(OPT_NORMAL) -O0 $*.c

# Workaround for gcc 3.4.6 (seen on Sparc32) (do not use -funroll-loops)
unrarppm.o: unrarppm.c
	$(CC) -DAC_BUILT $(CFLAGS) $< -o $@

.c.o:
	$(CC) $(CFLAGS) $(OPT_NORMAL) $< -o $@

.S.o:
	$(AS) $(ASFLAGS) $*.S

check: default
	../run/john --test=0 --verbosity=2

depend:
	makedepend -fMakefile.dep -Y *.c 2>> /dev/null

test: default
	cd ../test && perl jtrts.pl -q

test_full: default
	cd ../test && perl jtrts.pl -q -type full

test_utf8: default
	cd ../test && perl jtrts.pl -q -type utf-8

test_verbose: default
	cd ../test && perl jtrts.pl

test_full_verbose: default
	cd ../test && perl jtrts.pl -type full

test_utf8_verbose: default
	cd ../test && perl jtrts.pl -type utf-8

bash-completion:
	[ -d /etc/bash_completion.d ] && $(CP) ../run/john.bash_completion /etc/bash_completion.d/ || true
	[ -d /usr/local/etc/bash_completion.d ] && $(CP) ../run/john.bash_completion /usr/local/etc/bash_completion.d/ || true
	[ -d /opt/local/etc/bash_completion.d ] && $(CP) ../run/john.bash_completion /opt/local/etc/bash_completion.d/ || true
	@echo Bash-completion for JtR opportunistically installed.
	@echo Source \". ../run/john.bash_completion\" or logout/login to activate the changes

zsh-completion:
	[ -d /usr/share/zsh/functions/Completion/Unix ] && $(CP) ../run/john.zsh_completion /usr/share/zsh/functions/Completion/Unix/_john || true
	[ -d /usr/share/zsh/site-functions ] && $(CP) ../run/john.zsh_completion /usr/share/zsh/site-functions/_john || true
	[ -d /usr/local/share/zsh/site-functions ] && $(CP) ../run/john.zsh_completion /usr/local/share/zsh/site-functions/_john || true
	@echo zsh-completion for JtR opportunistically installed.
	@echo Source \". ../run/john.zsh_completion\" or logout/login to activate the changes

shell-completion: bash-completion zsh-completion

clean:
	$(RM) $(PROJ)
	@for exe in ${PROJ}; do \
	  ($(RM) $$exe.exe) \
	done
	$(RM) john-macosx-* *.o escrypt/*.o *.bak core
	$(RM) ../run/kernels/*.cl ../run/kernels/*.h ../run/kernels/*.bin
	$(RM) detect bench para-bench generic.h tmp.s
	$(RM) cuda/*.o cuda/*~ *~
	$(CP) $(NULL) Makefile.dep
	@for dir in ${subdirs}; do \
	  (cd $$dir && $(MAKE) clean) \
	  || case "$(MFLAGS)" in *k*) fail=yes;; *) exit 1;; esac; \
	done && test -z "$$fail"

# These are mostly for internal use.
charsets: ../run/ascii.chr ../run/alpha.chr ../run/lowernum.chr ../run/uppernum.chr ../run/lowerspace.chr ../run/lower.chr ../run/upper.chr ../run/digits.chr ../run/alnum.chr ../run/lanman.chr ../run/lm_ascii.chr ../run/alnumspace.chr ../run/latin1.chr ../run/utf8.chr

../run/ascii.chr: charset.c params.h
	../run/john -make-charset=../run/ascii.chr -pot:rockyou.ansi.pot -ext:filter_ascii

../run/alpha.chr: charset.c params.h
	../run/john -make-charset=../run/alpha.chr -pot:rockyou.ansi.pot -ext:filter_alpha

../run/lowernum.chr: charset.c params.h
	../run/john -make-charset=../run/lowernum.chr -pot:rockyou.ansi.pot -ext:filter_lowernum

../run/uppernum.chr: charset.c params.h
	../run/john -make-charset=../run/uppernum.chr -pot:rockyou.ansi.pot -ext:filter_uppernum

../run/lowerspace.chr: charset.c params.h
	../run/john -make-charset=../run/lowerspace.chr -pot:rockyou.ansi.pot -ext:filter_lowerspace

../run/lower.chr: charset.c params.h
	../run/john -make-charset=../run/lower.chr -pot:rockyou.ansi.pot -ext:filter_lower

../run/upper.chr: charset.c params.h
	../run/john -make-charset=../run/upper.chr -pot:rockyou.ansi.pot -ext:filter_upper

../run/digits.chr: charset.c params.h
	../run/john -make-charset=../run/digits.chr -pot:rockyou.ansi.pot -ext:filter_digits

../run/alnum.chr: charset.c params.h
	../run/john -make-charset=../run/alnum.chr -pot:rockyou.ansi.pot -ext:filter_alnum

../run/lanman.chr: charset.c params.h
	../run/john -make-charset=../run/lanman.chr -pot:rockyou.lm850.pot -ext:filter_lanman

../run/lm_ascii.chr: charset.c params.h
	../run/john -make-charset=../run/lm_ascii.chr -pot:rockyou.lm850.pot -ext:filter_lm_ascii

../run/alnumspace.chr: charset.c params.h
	../run/john -make-charset=../run/alnumspace.chr -pot:rockyou.ansi.pot -ext:filter_alnumspace

../run/latin1.chr: charset.c params.h
	../run/john -make-charset=../run/latin1.chr -pot:rockyou.ansi.16.pot

../run/utf8.chr: charset.c params.h
	../run/john -make-charset=../run/utf8.chr -pot:rockyou.utf8.24.pot


# For the time being, icc builds a better sse-intrinsics.S but this may
# change over time. NOTE that sse-intrinsics.S is never re-built unless you
# manually do a "make intrinsics".
intrinsics: clean-intrinsics sse-intrinsics-64.S sse-intrinsics-32.S

clean-intrinsics:
	$(RM) sse-intrinsics-64.S sse-intrinsics-32.S sse-intrinsics-win32.S

sse-intrinsics-64.S:
	$(LN) x86-64.h arch.h
	icc -S -o sse-intrinsics-64.S sse-intrinsics.c -O2 -fno-builtin -fno-verbose-asm -openmp -DUSING_ICC_S_FILE -Wall

sse-intrinsics-32.S:
	$(LN) x86-sse.h arch.h
	icc -m32 -S -o sse-intrinsics-32.S sse-intrinsics.c -O2 -fno-builtin -fno-verbose-asm -openmp -DUSING_ICC_S_FILE -Wall
	perl sse2i_winfix.pl sse-intrinsics-32.S sse-intrinsics-win32.S
	mv sse-intrinsics-win32.S sse-intrinsics-32.S

#######################################################################
## NOTE, auto re-building configure will ONLY happen IF the user has ##
## CONFIG_MAINT=1 environment variable.  Beware.                     ##
#######################################################################

## automatic re-running of configure if the configure.ac file has changed
ifeq ($(CONFIG_MAINT), 1)
configure: configure.ac
	autoconf
else
configure: configure.ac
	@touch configure
endif

# autoheader might not change autoconfig.h.in, so touch a stamp file
ifeq ($(CONFIG_MAINT), 1)
autoconfig.h.in: autoconfig-stamp-h
autoconfig-stamp-h-in: configure.ac aclocal.m4
	autoheader
	echo "timestamp from Makefile" > autoconfig-stamp-h-in
else
autoconfig.h.in: autoconfig-stamp-h
autoconfig-stamp-h-in: configure.ac aclocal.m4
	echo "timestamp from Makefile" > autoconfig-stamp-h-in
endif

ifeq ($(CONFIG_MAINT), 1)
autoconfig.h: autoconfig-stamp-h
autoconfig-stamp-h: autoconfig.h.in config.status
	./config.status
else
autoconfig.h: autoconfig-stamp-h
autoconfig-stamp-h: autoconfig.h.in config.status
	@touch config.status
	@touch autoconfig.h.in
	@touch autoconfig-stamp-h
	@touch autoconfig.h
endif

ifeq ($(CONFIG_MAINT), 1)
Makefile: Makefile.in config.status
	./config.status
endif

ifeq ($(CONFIG_MAINT), 1)
config.status: configure
	./config.status --recheck
endif

all:
	@for dir in ${subdirs}; do \
	  (cd $$dir && $(MAKE) all) \
	  || case "$(MFLAGS)" in *k*) fail=yes;; *) exit 1;; esac; \
	done && test -z "$$fail"

distclean: clean
	$(RM) -rf autom4te.cache
	@for dir in ${subdirs}; do \
	  (cd $$dir && $(MAKE) distclean) \
	  || case "$(MFLAGS)" in *k*) fail=yes;; *) exit 1;; esac; \
	done && test -z "$$fail"
	$(RM) -f Makefile autoconfig.h config.status config.cache config.log autoconfig-stamp-h stamp-h1
	$(LN) Makefile.stub Makefile
	$(RM) arch.h
	$(RM) fmt_registers.h fmt_externs.h john_build_rule.h

# a rule to make snapshots  (NOTE, still to be done for JtR)
snapshot: $(SOURCES) $(DOCS) $(OTHERFILES)
	@echo
	@echo "->Note: The version for now is hacked into Makefile.in as"
	@echo "->" $(VERS)
	@echo
	@echo "->copying all release files to the directory " xyplot-$(VERS)
	@echo
	tar cf - $(SOURCES) $(DOCS) $(OTHERFILES) | gzip > xyplot-$(VERS).tar.gz
	-mkdir xyplot-$(VERS)
	gzcat xyplot-$(VERS).tar.gz | (cd xyplot-$(VERS); tar xf -)
	$(RM) xyplot-$(VERS).tar.gz
	@echo
	@echo "->making the compressed tar file " xyplot-$(VERS).tar.gz
	@echo
	tar cf - xyplot-$(VERS) | gzip > xyplot-$(VERS).tar.gz
	@echo
#	@echo "->placing the snapshot for anonymous ftp in " $(FTPDIR)
#	@echo
#	rcp xyplot-$(VERS).tar.gz $(FTPDIR)
	echo "->removnig the temporary directory " xyplot-$(VERS)
	/bin/rm -rf xyplot-$(VERS)             # remove the old directory

install: default shell-completion
	@echo Stripping executables.
	$(STRIP) $(PROJ)

#install:
#	@for dir in ${subdirs}; do \
#	  (cd $$dir && $(MAKE) install) \
#	  || case "$(MFLAGS)" in *k*) fail=yes;; *) exit 1;; esac; \
#	done && test -z "$$fail"

# TBD JtR
#install: all
#	$(top_srcdir)/mkinstalldirs $(bindir)
#	$(top_srcdir)/mkinstalldirs $(libdir)
#	$(INSTALL) xyplot $(bindir)
#	$(INSTALL) xyps $(bindir)
#	$(INSTALL) xyug $(bindir)
#	$(INSTALL) xypost $(libdir)

# TBD JtR
uninstall:
	-$(RM) $(bindir)/xyplot
	-$(RM) $(bindir)/xyps
	-$(RM) $(bindir)/xyug
	-$(RM) $(libdir)/xypost

include Makefile.dep
