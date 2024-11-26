import base64
def xor_strings(byte_str1, byte_str2):
    # Ensure both strings are the same length by padding the shorter one
    max_len = max(len(byte_str1), len(byte_str2))
    # Perform XOR operation on each character and get the result as a byte string
    return bytes([b1 ^ b2 for b1, b2 in zip(byte_str1, byte_str2)])

def casecade_xor(byte_str1, byte_str2):
    numItr = 1
    if(len(byte_str1) > len(byte_str2)):
        numItr = int(len(byte_str1)/len(byte_str2))
    overall_result = b''
    for i in range(0,numItr):
        xor_result = xor_strings(byte_str1[i*len(byte_str2):(i+1)*len(byte_str2)], byte_str2)
        overall_result += xor_result
    return overall_result

    

# Input two strings
str1 = b'picoCTF{ECB_BADc62ba47cb40f37dc23}'
str2 = b'Hnn5YLmr5PbcQ469y'
overall_result = casecade_xor(str1, str2)

#print(f"{overall_result}")

# Output the result
print(f"Result of XOR operation:{overall_result}")
print(f"Result of XOR operation:{base64.b64encode(overall_result).decode('utf-8')}")

res = overall_result
print(res)
print(casecade_xor(b'Its wings are too small to get its fat little body off the ground.', res))


