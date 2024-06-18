from PIL import Image

def xor_encrypt_decrypt(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')

    width, height = img.size

    encrypted_img = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            encrypted_r = r ^ key
            encrypted_g = g ^ key
            encrypted_b = b ^ key

            encrypted_img.putpixel((x, y), (encrypted_r, encrypted_g, encrypted_b))

    return encrypted_img

def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return

    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == '1':
        encrypted_img = xor_encrypt_decrypt(image_path, key)
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted and saved as encrypted_image.png")
    else:
        decrypted_img = xor_encrypt_decrypt(image_path, key)
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted and saved as decrypted_image.png")

if __name__ == "__main__":
    main()
