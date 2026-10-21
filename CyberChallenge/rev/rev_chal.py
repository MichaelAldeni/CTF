f = open("rev/flag.txt.aes", "rb")
bin = bytearray(f.read())
n = len(bin)
print(n)
print(bin)


flag = []
for i in range(n):
    val = bin[i]
    shift = (i + 1) % 8
    decr = val << shift & 0xFF | (val >> (8 - shift)) 

    flag.append(decr)

print(bytes(flag).decode('ascii', errors='ignore'))
