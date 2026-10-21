from pwn import *
from string import printable

p = remote("padding.challs.cyberchallenge.it", 9030)
p.recvuntil(b"encrypt:")
BLOCK_SIZE = 16

def encrypt(payload):
    p.sendline(payload.encode())
    p.recvuntil(b"password: ")
    res = p.recvline().strip().decode()
    return [res[i:i+32] for i in range(0, len(res), 32)]

flag = ""

while True:
    padding_len = (BLOCK_SIZE - 1 - (len(flag) % BLOCK_SIZE))
    target_blocks = encrypt("A" * padding_len)
    
    target_block_idx = len(flag) // BLOCK_SIZE
    target_block = target_blocks[target_block_idx]

    found_char = False
    for c in printable:
        test_payload = ("A" * padding_len) + flag + c
        test_blocks = encrypt(test_payload)

        if test_blocks[target_block_idx] == target_block:
            flag += c
            print(f"Found: {flag}")
            found_char = True
            break
            
    if not found_char or "}" in flag:
        break

print(f"\nFinal Flag: {flag}")
