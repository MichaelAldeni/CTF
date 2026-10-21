import pwn
import json

HOST = 'software-17.challs.olicyber.it'
PORT = 13000

s = pwn.remote(HOST, PORT)
text = s.recvuntil(b'iniziare ...')

s.sendline()

for i in range(10):

    text = s.recvline()
    numbers = s.recvline().decode()
    text = s.recvuntil(b'Somma? : ')

    data = json.loads(numbers)
    s.sendline(str(sum(data)).encode())


print(s.recvline())
