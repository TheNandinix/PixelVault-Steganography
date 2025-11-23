from PIL import Image
from utils.security import xor_cipher

def show_data(image_path, password=""):
    try:
        img = Image.open(image_path)
        pixels = list(img.getdata())
        
        bin_data = ""
        for p in pixels:
            for v in p[:3]:
                bin_data += str(v & 1)
                
        all_bytes = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
        decoded = ""
        
        for byte in all_bytes:
            decoded += chr(int(byte, 2))
            if decoded.endswith("#####"):
                msg = decoded[:-5]
                if msg.startswith("ENC:"):
                    if not password: return False, "Password Required"
                    return True, xor_cipher(msg[4:], password)
                return True, msg
        return False, "No Message Found"
    except Exception as e:
        return False, str(e)