# -----------------------------------------------------------------------------
# Project: Simple Encryption Tool (Caesar Cipher)
# Description: A playful tool to practice Python logic and basic cryptography.
# -----------------------------------------------------------------------------

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    Preserves case and ignores non-alphabetic characters.
    """
    result = ""
    
    # Invert the shift for decryption mode
    if mode == "decrypt":
        shift = -shift
        
    for char in text:
        # Process only alphabetic characters
        if char.isalpha(): 
            # Determine ASCII base (A=65 or a=97)
            start = ord('a') if char.islower() else ord('A')
            
            # Apply modular arithmetic formula: (position + shift) % 26
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep numbers, spaces, and symbols as they are
            result += char 
            
    return result

# --- Testing Zone ---
if __name__ == "__main__":
    print("--- Python Encryption Tool ---")
    
    # Configuration
    secret_message = "Greeting to the Bat Cyber Team!"
    key = 7
    
    print(f"Original Message: {secret_message}")
    
    # 1. Execution: Encryption
    coded = caesar_cipher(secret_message, key, "encrypt")
    print(f"Encoded Message:  {coded}")
    
    # 2. Execution: Decryption
    original = caesar_cipher(coded, key, "decrypt")
    print(f"Decoded Message:  {original}")
