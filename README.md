# Python Encryption Tool (Learning Project)
> **A personal practice project developed alongside my formal studies to master Python logic in a fun, hands-on way.**
> *Focus: Exploring symmetric cryptography and string manipulation.*

---

## 1. Why this project?
While working through my certifications, I decided to build this tool to practice Python "in the field." My goal was to turn theoretical **confidentiality** concepts into a concrete script. This self-taught approach helps me better integrate programming logic while staying immersed in the cybersecurity world.

## 2. The Concept: Shift Cipher
This script implements an enhanced version of the **Caesar Cipher**. One of the simplest encryption methods, making it a perfect exercise for beginners (like me X) to understand how data can be protected.

* **Confidentiality**: The message becomes unreadable to anyone without the key.
* **Symmetric Logic**: The same shift value (the key) is used to both encode and decode the information.

## 3. Technical Implementation
To make this more than just a basic exercise, I added several robust features:
* **Case Sensitivity**: The script recognizes and preserves both uppercase and lowercase letters.
* **Symbol Preservation**: Spaces, numbers, and punctuation remain unchanged so the message structure stays intact.
* **Modular Arithmetic**: I used the `% 26` operator to ensure the alphabet "wraps around" correctly (e.g., shifting 'z' forward returns to 'a').

---

## 4. The Code (`encrypt_decrypt.py`)
```python
def caesar_cipher(text, shift, mode):
    result = ""
    
    # Invert the shift for decryption mode
    if mode == "decrypt":
        shift = -shift
        
    for char in text:
        if char.isalpha(): # Process only letters
            # Determine base ASCII (A=65 or a=97)
            start = ord('a') if char.islower() else ord('A')
            # Apply the shift formula
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char # Numbers and symbols remain unchanged
            
    return result

# --- Testing Zone ---
secret_message = "Greetings to the Bat Cyber Team"
shift_key = 7

# 1. Encryption
coded_message = caesar_cipher(secret_message, shift_key, "encrypt")
print(f"Encoded Message: {coded_message}")

# 2. Decryption
original_message = caesar_cipher(coded_message, shift_key, "decrypt")
print(f"Decoded Message: {original_message}")
