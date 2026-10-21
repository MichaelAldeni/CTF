from pwn import *

def main():
    HOST = "software-19.challs.olicyber.it"
    PORT = 13002

    exe = ELF("./sw-19")


    r = remote(HOST, PORT)    

    r.recvuntil(b"iniziare ...")
    r.sendline()

    for i in range(20):

        data = r.recvuntil(b": ")
        word = data.split(b'-> ')[1].split(b':')[0].decode()
        print(word)


        #p = process(exe.path)
        index = exe.sym[word]
        print(hex(index).encode())

        r.sendline(hex(index).encode())  

    r.interactive()


if __name__ == "__main__":
    main()