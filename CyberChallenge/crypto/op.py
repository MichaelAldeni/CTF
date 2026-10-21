m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1_bytes = bytes.fromhex(m1)
m2_bytes = bytes.fromhex(m2)
print(xor(m1_bytes, m2_bytes))


ciphertext = '104e137f425954137f74107f525511457f5468134d7f146c4c'

ciphertext_bytes = bytes.fromhex(ciphertext)

results = []
for key in range(256):
    decrypted = "".join([chr(x ^ key) for x in ciphertext_bytes])
    if all(32 <= ord(c) <= 126 for c in decrypted):
        results.append((key, decrypted))

print(results)



