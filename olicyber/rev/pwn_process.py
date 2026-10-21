from pwn import *

exe = ELF('./sw-19') 

HOST = 'software-19.challs.olicyber.it'
PORT = 13002

s = remote(HOST, PORT)

p = process(exe.path)

data = s.recv()
s.sendline()

for i in range(20):
    
    data = s.recvuntil(b'-> ')
    ps = s.recvuntil(b': ')

    print(hex(exe.sym[ps.decode().replace(': ', '')]))
    s.sendline(hex(exe.sym[ps.decode().replace(': ', '')]).encode())

data = s.recv()
print(data)