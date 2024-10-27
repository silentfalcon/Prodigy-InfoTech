#Task 2 Image Encryption Tool

This Python program implements a simple image encryption tool using pixel manipulation techniques. The program can encrypt and decrypt images by performing basic mathematical operations on the pixel values. It is designed to be user-friendly, guiding users through the encryption and decryption processes with clear prompts.

Features

Image Encryption: Users can encrypt an image by applying a mathematical operation to each pixel value, effectively altering the image.
Image Decryption: The program can reverse the encryption process to restore the original image.
User Input: Users can specify the image file and the encryption key.
File Handling: The program saves the encrypted and decrypted images to specified file paths.
How It Works

Encrypt Image: Multiplies each pixel value by a key and then divides by the key plus one to create the encrypted image.
Decrypt Image: Reverses the encryption process by multiplying each pixel value by the key plus one and then dividing by the key.
Usage

Run the Program: Execute the script to start the Image Encryption program.
Select Action: Choose 'e' for encryption, 'd' for decryption, or 'q' to quit.
Encrypt Image:
Enter the encryption key.
Specify the location or URL of the image to be encrypted.
Decrypt Image:
Enter the decryption key.
Specify the location of the encrypted image.
View Results: The program saves and indicates the location of the encrypted and decrypted images.
This code was developed as part of my internship at The Prodigy Infotech, showcasing a basic approach to image encryption and decryption through pixel manipulation.
