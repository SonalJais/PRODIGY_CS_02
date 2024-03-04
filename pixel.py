from PIL import Image

def encrypt_image(image_path, key):
    # Load the image
    image = Image.open(image_path)
    
    # Convert image to grayscale
    grayscale_image = image.convert("L")
    
    # Get the image size
    width, height = grayscale_image.size
    
    # Create a new image for encrypted pixels
    encrypted_image = Image.new("L", (width, height))
    
    # Perform XOR operation on each pixel
    for x in range(width):
        for y in range(height):
            pixel_value = grayscale_image.getpixel((x, y))
            encrypted_pixel = pixel_value ^ key  # XOR with the key
            encrypted_image.putpixel((x, y), encrypted_pixel)
    
    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    # Load the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    
    # Get the image size
    width, height = encrypted_image.size
    
    # Create a new image for decrypted pixels
    decrypted_image = Image.new("L", (width, height))
    
    # Perform XOR operation on each pixel
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = encrypted_pixel ^ key  # XOR with the key
            decrypted_image.putpixel((x, y), decrypted_pixel)
    
    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

# Example usage
image_path = "image.jpg"
key = 123

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the image
decrypt_image("encrypted_image.png", key)
