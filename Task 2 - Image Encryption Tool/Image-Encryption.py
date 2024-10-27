from PIL import Image
import random

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())  # Get pixel data as a list
    random.seed(key)  # Set the seed for reproducibility
    random.shuffle(pixels)  # Shuffle pixels based on key
    img.putdata(pixels)  # Put shuffled pixels back into the image
    encrypted_path = "encrypted_" + image_path
    img.save(encrypted_path)
    print(f"Encrypted image saved as: {encrypted_path}")
    return encrypted_path

def decrypt_image(encrypted_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    pixels = list(img.getdata())  # Get pixel data as a list
    random.seed(key)  # Reset the seed to ensure we can reverse the shuffle
    order = list(range(len(pixels)))
    random.shuffle(order)  # Shuffle the indices based on the key
    decrypted_pixels = [None] * len(pixels)
    for idx, pix in zip(order, pixels):
        decrypted_pixels[idx] = pix  # Place each pixel back in original order
    img.putdata(decrypted_pixels)  # Put decrypted pixels back
    decrypted_path = "decrypted_" + encrypted_path
    img.save(decrypted_path)
    print(f"Decrypted image saved as: {decrypted_path}")
    return decrypted_path

# Usage
image_path = input("Enter the image file path: ")
key = int(input("Enter encryption key: "))

# Encrypt the image
encrypted_image = encrypt_image(image_path, key)

# Decrypt the image
decrypt_image(encrypted_image, key)
