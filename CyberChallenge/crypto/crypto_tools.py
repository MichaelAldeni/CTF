from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Hash import SHA3_384, SHA224, HMAC, SHA256
from Crypto.PublicKey import DSA
from Crypto.Util import number
from Crypto.Util.Padding import pad, unpad
import hashlib


def modular_exp():
    print("Modular Exponentiation:")

    m = 11
    e = 13
    n = 91
    c = pow(m, e, n)
    print(c)
    print('-----------------------------')

def des_encryption():
    print("DES Encryption:")

    plaintext = 'La lunghezza di questa frase non è divisibile per 8'
    key = bytes.fromhex('716b18adbcba8129')

    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size, style='x923'))

    print(ciphertext.hex())
    print(bytes.hex(cipher.iv))
    print('-----------------------------')

def aes_encryption():
    print("AES Encryption:")

    plaintext2 = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
    key = "32 bytes key for aes-256!!!!!!!!"
    key_bytes = key.encode()
    print(key_bytes.hex())

    cipher2 = AES.new(key_bytes, AES.MODE_CFB, segment_size=24)
    ciphertext2 = cipher2.encrypt(pad(plaintext2.encode(), AES.block_size, style='pkcs7'))
    print(ciphertext2.hex())
    print(bytes.hex(cipher2.iv))

    print('-----------------------------')


def chacha20_decryption(): 
    print("ChaCha20 Decryption:")

    key = "ffd5a868b3f8614511926aca46a1d7e00f611b8a448b8e20ec28e3b1aa9cd232"
    ciphertext3 = "44c3e6c73f57d8e49979910adb751463602c565272e4645fa138406d"
    nonce = "7c0758e1e8058236"

    cipher3 = ChaCha20.new(key=bytes.fromhex(key), nonce=bytes.fromhex(nonce))
    plaintext3 = cipher3.decrypt(bytes.fromhex(ciphertext3))
    print(plaintext3.decode())
    print('-----------------------------')


def sha3_func():
    print("SHA3-384:")

    msg = "hash_me_pls"
    h_obj = SHA3_384.new()
    h_obj.update(msg.encode())
    print(h_obj.hexdigest())
    print('-----------------------------')


def hmac_func():
    print("HMAC-SHA224:")

    key = "ed827e69556dd8712c522d0e996eeec4243e713b35f553d8a06520e91ff2490c"
    msg = "La mia integrità è importante!" 
    h_obj = HMAC.new(bytes.fromhex(key), digestmod=SHA224)
    h_obj.update(msg.encode()) 
    print(h_obj.hexdigest())
    print('-----------------------------')

def dsa_func():
    print("DSA Signature:")

    key = "3082025d0201003082023506072a8648ce38040130820228028201010098d072ed403aa897dce8984b385200b5bd098cfe165059c764bef318841bb357539bcacd2bb2b8416fb2fb444d1cd5b395d2d739f0cb015b7c970e64000d0b35acabf0077fa051deb9267b213e8d8d4db5b47b625630c3c769dfd8ab220dcdedef3e6a9edadc1fa6cff392f54a6cb244ff4a720fa46268cad61ab3ed3c9badc0b1c7e394df13194af0b08982f14ac1cace33a0e829e184e2ee51542bd90e63d86c47a9e99bc5390d4b93b1293669083478777305d95e4e734cbb3024ec042f227e265c89b88572f16a083ddcc1344d454b8f3edf8dc417ad9afc7d37558f051af045912f057a642a5af00955133041edf9ffe7178546065768d4ffae580cfaa5021d00be305e4ca500399851517f8500b8bdf5ae54851b63818288081a1473028201002f6fc617a7e15cebb1830e0f20b72e19a3b77778ad67dfdab3de4e23b782cae2b0e7efc35da8a08eeeb8fd040a09e853ea720132fd158b0aafec0d1999262dfe1c70b91b8b186a4b276edf26b01a06aaac61984cdd49feb8537efbbf6a0e6f1f71189e2c48b66825761b4807cb18cf4c2fbf460a232fea37ceaebec313a7dfdec8c762a88efe291c3bc9ee22fc851d8aa974e9d8e0d1caf1e49ef1ec30340eddf64d989ca84dd1f604926d0d26fe957c6320b84070a3d9b961cb3aaa701a3cf8b13bc4711cb4914335a3ecdd66813d72a4308438d95d291a54f437d0637d899f3fc398fa16a502bd3e2da8e877d4a1d4bc40d34da8d24831843616a852d84daa041f021d00ac450a7b8a633582c03a81d7ba9362ccae22e1182489a9622477e4b4"
    pubkey = DSA.import_key(bytes.fromhex(key))
    print(pubkey.x)
    print("Separator")
    print(pubkey.g)
    print("Separator")
    print(pubkey.y)
    print('-----------------------------')

def gen_random_prime():
    print("Generate Random Prime:")
    prime = number.getPrime(1024)
    print(prime)
    print('-----------------------------')

def check_if_prime():
    print("Check if Prime:")

    num = 168650892237780521837535305280573631531018673700544431742435881271270649597040489242703958636501938745526977818349741317034692754635246124517341788542157542710196095654256630360958426677360901014763577289842465937241688672411204320479624236229165585125959165585930881425490997899048555802502005714211800575726
    if number.isPrime(num):
        print("It is prime.")
    else:
        print("It is not prime.")
    print('-----------------------------')

def diffie_hellman():
    print("Diffie-Hellman Key Exchange:")

    checker = True
    tried = 0
    while checker:
        p = number.getPrime(1024)
        print("Tried:", tried)
        tried += 1
        if number.isPrime((p * 2) + 1):
            checker = False

    print ("Prime p:", p * 2 + 1)


p = 218799905571218870818050004171233602732768715048376783224753985672277955351261081927201989217136286063775983041761579598020363134629356180225235626451145110870627232109520728840261266470456346613718340267846770790158256857596105569240788356699445041911670016777222931505769840315797413456890067068816974412127
g = 143771296371665500621901863276593059367905113875299206285785458949782313678208473232959833644023551553007144856109961329025162815022858163826395555958274779380686875969176097392508623852495231650734966512973601014620868057487905902261492396943091397992384425944440790761842927869237669297113255775244450359899
Xa = 148053998105410471739866402898257770582065760799898261933722212160954010385585193427711526040479013282921929825195920801367443299718116394147419667217285300609055499509253987196840348310230366857660794933313476065309952327241935908364026708850966885080130586832527995363905381721641610749047152090718746623953

Pa = pow(g, Xa, p)
print("Public Key Pa:", Pa)
print("------------------------------")

msg = 'eb43c7c1a22d65861cee2003a09674b4d4bf9c50f7ac2140587232707ed6b8fc66c0c376a54394bc8bef0f6f3936360bae00f629aaeeb3894823e2d83457a61e'
iv = '96095bb6b2a52a63fe97c70a34edfaa8'
mode = AES.MODE_CBC
Pb = 'af41239c2229f9bc40184df64bed8e75ffc4842f1ed9dfed6572bc49a6acbc4d909d6907501a7ecbf6f3f785d1d7240a5435e3ab6be64b7c4a55ea290fdf30e4ad0868c83aa0554b3ed64de82dd449c6bd10b0a851fef9b04c9c28b3fa0cf535a355853ef9101569c099a29d03b1caa898ab27ac70743858722b71fdea75ba0d'

key = pow(int(Pb, 16), Xa, p)
print("Shared Key:", key)
print("------------------------------")


def decrypt_alice_message():
    shared = key
    shared_bytes = shared.to_bytes((shared.bit_length() + 7) // 8, 'big')
    hex_shared = format(shared, 'x')

    def printable_ratio(b):
        if len(b) == 0:
            return 0
        return sum(1 for x in b if 32 <= x < 127) / len(b)

    sources = {}
    sources['sha256_str'] = hashlib.sha256(str(shared).encode()).digest()
    sources['sha256_hexstr'] = hashlib.sha256(hex_shared.encode()).digest()
    sources['sha256_bytes'] = hashlib.sha256(shared_bytes).digest()
    sources['sha1_str'] = hashlib.sha1(str(shared).encode()).digest()
    sources['md5_str'] = hashlib.md5(str(shared).encode()).digest()
    sources['raw_shared_bytes'] = shared_bytes
    sources['decstr_bytes'] = str(shared).encode()
    hexp = hex_shared if len(hex_shared) % 2 == 0 else '0' + hex_shared
    sources['hex_bytes'] = bytes.fromhex(hexp)

    candidates = []
    for name, src in sources.items():
        for keylen in (16, 24, 32):
            if len(src) >= keylen:
                k_bytes = src[:keylen]
            else:
                k_bytes = src.rjust(keylen, b'\x00')
            try:
                cipher = AES.new(k_bytes, AES.MODE_CBC, bytes.fromhex(iv))
            except Exception:
                continue
            dec = cipher.decrypt(bytes.fromhex(msg))
            try:
                pt = unpad(dec, AES.block_size)
            except Exception:
                pt = dec
            ratio = printable_ratio(pt)
            text = pt.decode('ascii', errors='replace')
            match = any(k in text.lower() for k in ('flag', 'ctf{', 'picoctf', 'actf', '{'))
            candidates.append((name, keylen * 8, ratio, match, text, pt.hex()))

    candidates.sort(key=lambda x: (not x[3], -x[2]))
    print('Top candidates:')
    for c in candidates[:12]:
        name, bits, ratio, match, text, hx = c
        print(f"Source={name}, key={bits} bits, printable_ratio={ratio:.2f}, match={match}")
        print('ascii_preview:', text[:200])
        print('hex_preview:', hx[:200])
        print('---')

    print('\nMatches with potential flag indicators:')
    for c in candidates:
        if c[3]:
            name, bits, ratio, match, text, hx = c
            print(f"Source={name}, key={bits} bits, ratio={ratio:.2f}")
            print(text)
            print('---')


