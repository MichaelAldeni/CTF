from pwn import *
import ast

def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    
    r = remote(HOST, PORT)    

    r.recv()
    r.sendline() 

    for i in range(10):
        print(f"--- Level {i+1} ---")
        
        r.recvuntil(b"numeri\n")
        data = r.recvline()
        print(f"Received: {data}")

        converted = ast.literal_eval(data.decode().strip())
        total = sum(converted)
        
        print(f"Sending: {total}")
        r.sendline(str(total).encode())

    r.interactive()

if __name__ == "__main__":
    main()