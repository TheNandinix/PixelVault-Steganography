from PIL import Image
from utils.converters import data_to_binary
from utils.security import xor_cipher

def hide_data(image_path, secret_msg, output_path, password=""):
    try:
        img = Image.open(image_path)
        new_img = img.copy()
        
        if password:
            secret_msg = "ENC:" + xor_cipher(secret_msg, password)
            
        secret_msg += "#####" # Delimiter
        binary_msg = ''.join(data_to_binary(secret_msg))
        data_len = len(binary_msg)
        
        pixels = list(new_img.getdata()) # Syllabus Unit 5: Lists
        new_pixels = []
        idx = 0
        
        for pixel in pixels:
            pixel = list(pixel) # Tuples to Lists
            for i in range(3): # R,G,B
                if idx < data_len:
                    # LSB Logic
                    pixel[i] = pixel[i] & ~1 | int(binary_msg[idx])
                    idx += 1
            new_pixels.append(tuple(pixel))
            
        new_img.putdata(new_pixels)
        new_img.save(output_path)
        return True, "Success"
    except Exception as e:
        return False, str(e)