# Emergency Call — OliCyber (Binary Exploitation)

## Overview
Exploitation of a **Stack-based Buffer Overflow** on an x86-64 Linux binary to spawn a remote shell using a custom **Return-Oriented Programming (ROP)** chain and a direct `execve` syscall invocation.

* **file output:** ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=cb0d1e08bc1c20bd468cd0f8402ee415a59a3d03, stripped
* **checksec output:**     
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000) 
* **Tools:** `pwntools`, `GDB`, `ROPgadget`, `readelf`

---

## Vulnerability Analysis
Static and dynamic analysis of the binary revealed the two following behaviors:
1. **Arbitrary Write to `.bss`:** The first user input is written directly into a fixed, predictable address inside the `.bss` section (`0x404000`).
2. **Stack Buffer Overflow:** The second input read operation does not properly enforce bounds checking, allowing us to overwrite the saved **Return Address** after a **40-byte** offset.

---

## Exploitation Strategy
The goal is to invoke the `execve("/bin/sh", NULL, NULL)` syscall directly by setting up the CPU registers according to the Linux x86-64 calling convention:

* `RAX` = `59` (`sys_execve`)
* `RDI` = `0x404000` (pointer to the `"/bin/sh\x00"` string)
* `RSI` = `0` (`argv`)
* `RDX` = `0` (`envp`)

### Bypassing the Missing `pop rax` Gadget
The binary lacks a direct `pop rax; ret` gadget. However, when the vulnerable function returns, `RAX` holds `0` (verified dynamically via GDB), and the binary provides a `xor rax, rdi; ret` gadget at `0x401038`. 

By loading `59` into `RDI` (`pop rdi; ret`) and executing `xor rax, rdi`, we set `RAX` to `59` (`0 ^ 59 = 59`).

### Attack Flow
1. Send `"/bin/sh\x00"` at the first prompt to store the command string at `0x404000` (`.bss`).
2. Send 40 bytes of padding followed by the ROP chain to populate `RAX`, `RDI`, `RSI`, and `RDX`.
3. Jump to the `syscall; ret` gadget (`0x40101a`) to execute `/bin/sh` and gain an interactive shell.
