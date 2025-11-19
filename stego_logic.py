#Function to convert data into binary format
def data_to_binary(data):
    binary_list = []
    # Convert input data to string if it's not already
    if isinstance(data, str):
        # ord turns letter to numbers. format turns number to binary
        binary_list = [format(ord(i), '08b') for i in data]
    return binary_list
from PIL import Image  # Import the library we installed
def hide_data(image_path, secret_message, output_filename):
    # Load the image
    image = Image.open(image_path)
    # Create a copy so we don't destry the original
    new_image = image.copy()
    # Add a delimiter so we know when the text ends
    secret_message += "#####"
    # Convert our message to binary using function we created earlier
    data_binary = data_to_binary(secret_message)
    # Get all the pixels from the image
    data_index = 0
    binary_message = ''.join(data_binary)
    data_len = len(binary_message)
    # Get pixel data
    pixels = list(new_image.getdata())
    new_pixels = []
    pixel_index = 0
    # -----The CORE Loop-----
    for pixel in pixels:
        # A pixel is a tuple of (R, G, B)
        # We need to make it into list to modify it
        pixel = list(pixel)

        # Loop through RGB values
        for i in range(3):
            if data_index < data_len:
                # This is the bitwise operation (THE MATH)
                # We clear the last bit and replace it with our secret bit
                # pixel[i] and ~1 clears the last bit (makes it even)
                # | int(binary_message[data_index]) adds our secret bit (0 or 1)
                pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                data_index += 1
        # Add the modified pixel to new pixel list
        # Convert back to tuple
        new_pixels.append(tuple(pixel))
    #Put the new pixels back into image
    new_image.putdata(new_pixels)
    new_image.save(output_filename)
    print("Data hidden successfully in", output_filename)    

def show_data(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    binary_data = ""
    for pixel in pixels:
        for value in pixel:
            #Extract the last bit using value & 1
            binary_data += str(value & 1)
    # We have massive strings of 0s and 1s. We need to cut it into chunks of 8.
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    decoded_data = ""

    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        # Check for our delimiter
        if decoded_data[-5:] == "#####":
                  return decoded_data[:-5]
    return "No hidden message found."


if __name__ == "__main__":
     # Test encoding
     print("Hiding data...")
     hide_data("test.png", "This is a secret message from June", "secret_image.png")
     # Test decoding
     print("Retrieving data...")
     secret = show_data("secret_image.png")
     print("The secret is:", secret)
     
