f = open("crypto/message.enc", "r")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

msg = f.read().strip()
print("Ciphertext:", msg)

flag = ""
for c in msg:
    print("Processing:", c)
    if c not in {"_", "{", "}"}:
        flag += alphabet[(alphabet.index(c.upper()) + 9) % 26]
        print("Current flag:", flag)
    else: flag += c 

print("Plaintext:", flag)