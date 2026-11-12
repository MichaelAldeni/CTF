# Capture The Flag (CTF) Write-ups & Exploits

A curated collection of exploit scripts, reverse engineering notes, and technical write-ups from various CTF competitions and training platforms, including **CyberChallenge.IT**, **OliCyber**, and **Hack The Box**.

## Focus Areas
* **Binary Exploitation (Pwn):** Stack/Heap Buffer Overflows, Return-Oriented Programming (ROP), `ret2libc`, Format String vulnerabilities.
* **Reverse Engineering:** Static and dynamic analysis of ELF/PE binaries, deobfuscation, and algorithm reconstruction.
* **Tools & Languages:** Python (`pwntools`), C/C++, x86/x86_64 Assembly, GDB (`pwndbg`), Ghidra, IDA Free. 

## Featured Challenges
| Platform / Event | Challenge | Category | Key Techniques / Vulnerabilities | Solution |
| :--- | :--- | :--- | :--- | :--- |
| **OliCyber** | `emergency-call` | Pwn | Stack Buffer Overflow, Custom ROP Chain, `execve` Syscall, Register Manipulation (`XOR`) | [Write-up & Exploit](./olicyber/rev/chall/emergency-call) |
