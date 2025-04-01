def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    try:
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            raise ValueError("Invalid mode. Choose 'encrypt' or 'decrypt'")
        
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        
        # Encrypt or decrypt
        output = caesar_cipher(message, shift, mode)
        print(f"Result: {output}")
    except ValueError as e:
        print(f"Error: {e}")




