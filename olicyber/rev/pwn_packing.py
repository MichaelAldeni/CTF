from pwn import *

HOST = 'software-18.challs.olicyber.it'
PORT = 13001

s = remote(HOST, PORT)

data = s.recvuntil(b'iniziare ...')
s.sendline()

for i in range(100):
    data = s.recvuntil(b'restituiscimi ')
    number = s.recvuntil(b' ').strip().decode()
    data = s.recvuntil(b'packed a ')
    packing = s.recvuntil(b'\n').strip().decode()
    data = s.recvuntil(b'Result : ')

    print(data)

    print(number)
    print(packing)

    if '32' in packing:
        print(p32(int(number, 0)))
        s.send(p32(int(number, 0)))
    else:
        print(p64(int(number, 0)))
        s.send(p64(int(number, 0)))

    #data = s.recvline()
    #print(data)

data = s.recv()
print(data)