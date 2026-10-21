from pwn import *

def main():
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001

    r = remote(HOST, PORT) 

    r.recv()
    r.sendline()

    for i in range(100):
        print(f"--- Level {i+1} ---")

        r.recvuntil(b"restituiscimi ")
        
        data = r.recvuntil(b" ")
        data_int = int(data.strip(), 16)
        data_hex = hex(data_int)
        print(data_hex)

        r.recvuntil(b"packed a ")
        format = r.recvline()
        print(format.strip())

        if b"32" in format:
            packed = p32(data_int)
        else: packed = p64(data_int)

        test = r.recv()

        print(f"Sending: {packed}")
        r.send(packed)

    r.interactive()

if __name__ == "__main__":
    main()