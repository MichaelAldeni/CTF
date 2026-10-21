from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib


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


decrypt_alice_message()