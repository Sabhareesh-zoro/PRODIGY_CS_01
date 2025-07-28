def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (number): "))
    except ValueError:
        print("Please enter a valid integer for the shift.")
        return

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice. Please select E or D.")

if __name__ == "__main__":
    main()
