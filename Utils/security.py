# Simple XOR Cipher for Password Protection
def xor_cipher(text, password):
    #Encrypts/Decrypts text using XOR logic.
    if not password: return text
    result = []
    for i in range(len(text)):
        char_code = ord(text[i]) ^ ord(password[i % len(password)])
        result.append(chr(char_code))
    return "".join(result)