from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Resize the key to match the image dimensions
    key = np.resize(key, img_array.shape[:2])

    # Encrypt the image by applying XOR operation
    encrypted_array = np.bitwise_xor(img_array, key[:, :, np.newaxis])
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_path)
    print("Image encrypted successfully.")

# User inputs
image_path = input("Enter the path to the image file: ")
output_path = "encrypted_image.png"

# Check if the file exists
try:
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Generate a random key
    key = np.random.randint(0, 256, size=img_array.shape[:2], dtype=np.uint8)

    # Encrypt the image
    encrypt_image(image_path, key, output_path)

except FileNotFoundError:
    print(f"Error: The file '{image_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")