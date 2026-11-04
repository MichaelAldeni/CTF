def pair_strings(s1: str, s2: str, length: int = 8) -> str:
    """Interleaves alternating characters from s1 and s2 up to 'length' each."""
    return "".join(c1 + c2 for c1, c2 in zip(s1[:length], s2[:length]))

def make_serial(key: str) -> str:
    # Extract the three 8-character chunks based on the byte offsets
    chunk_a = key[0:8]    # a1 + 0
    chunk_b = key[9:17]   # a1 + 9
    chunk_c = key[18:26]  # a1 + 18

    # Line 3: pairStrings(a2, a1 + 18, a1 + 9, 8)
    part1 = pair_strings(chunk_c, chunk_b, 8)

    # Line 4: pairStrings(a2 + 16, a1, a1 + 18, 8)
    part2 = pair_strings(chunk_a, chunk_c, 8)

    # Line 5: pairStrings(a2 + 32, a1 + 9, a1, 8)
    part3 = pair_strings(chunk_b, chunk_a, 8)

    # Concatenate the three 16-character parts (48 chars total)
    return part1 + part2 + part3

input_key = "xaT5b4ja-7DdyOBOk-NU3kcp7y"


final_serial = make_serial(input_key)
print(final_serial)
