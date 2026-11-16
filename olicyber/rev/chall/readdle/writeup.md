# Readdle — OliCyber (Binary Exploitation)

## Overview
Injection of a **shellcode** on an x86-64 Linux binary to spawn a remote shell bypassing the size limitation of the `read` function

* **file output:** ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=66578411c6ce3af27eedc87476eb2ae99f062762, not stripped
* **checksec output:**     
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No 
* **Tools:** `pwntools`, `shellcraft`, `GDB`

---

## Vulnerability Analysis
Static and dynamic analysis of the binary revealed the following behavior:
1. **mmap(0x1337000, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, ...):** Create a fixed-address **RWX** page (this is the core vulnerability)
2. **read(0, 0x1337000, 4):** Write up to 4 bytes of user-controlled data into the RWX page.
3. Jumps directly to `0x1337000`.

---

## Exploitation Strategy
The goal is to invoke the `read(0, 0x1337000, 0x1000)` syscall changing the number of bytes read by the function by setting:

* `RAX` = `0` 
* `RDI` = `0` (stdin)
* `RSI` = `0x1337000` (pointer to the start of the heap)
* `RDX` = `0x1000` (4096 bytes)

And then the shellcode to invoke the remote shell.

### Bypassing the size limitation of 4 bytes 
Construct a small shellcode in which:
* the first 2 bytes are used to cahnge the edx register. It is used `dh` to change the high byte of `dx` (bits 8-15 of `edx`)
* the second 2 bytes are used to invoke the syscall   

### Attack Flow
1. Send:
    `mov dh, 0x10`
    `syscall`
2. Adding `\x41\x41\x41\x41` of padding to start the shell at `0x1337004`
3. Inject the shell through `shellcraft` of `pwntools`: `asm(shellcraft.sh())`