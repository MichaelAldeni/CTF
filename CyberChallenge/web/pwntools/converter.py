from pwn import *

data = 380440006
#print(p32(data, endian='little'))
print(p32(data, endian='little')[:4])

