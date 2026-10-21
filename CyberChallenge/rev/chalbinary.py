from pwn import *
import re

HOST = 'piecewise.challs.cyberchallenge.it'
PORT = 9110

r = remote(HOST, PORT)

while True:
    data = r.recvline()
    if b'flag' in data:
        print("Partial flag found: " + data.decode())
        data = r.recvline()
    print(data)
    if b'empty' in data:
        r.sendline()
    else:
        numbers = re.findall(rb'\d+', data)
        print(numbers)

        endian = 'little' if b'little' in data else 'big'

        if numbers[1] == b'32':
            r.send(p32(int(numbers[0]), endian=endian)[:int(numbers[2])])
        elif numbers[1] == b'64':
            r.send(p64(int(numbers[0]), endian=endian)[:int(numbers[2])])


