#!/usr/bin/env python3

import argparse

class VigenereCipher:
    def __init__(self,text, key):
        self.text = text
        self.key = key

    def encrypt(self):
        encrypted = ''
        text = self.text.upper()
        key = self.key.upper()
        key_index = 0

        for i in range(len(text)):
            if text[i].isalpha():
                # Calculate the shift based on the key character
                shift = ord(key[key_index % len(key)]) - ord('A')
                encrypted += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
                key_index += 1
            else:
                encrypted += text[i]

        return encrypted
    
    def decrypt(self):
        decrypted = ''
        text = self.text.upper()
        key = self.key.upper()
        key_index = 0
            
        for i in range(len(text)):
            if text[i].isalpha():
                # Calculate the shift based on the key character
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted += chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
                key_index += 1
            else:
                decrypted += text[i]
        return decrypted


def main():
    parser = argparse.ArgumentParser(description='Vigenere Cipher encryption tool')

    parser.add_argument('-e', '--encrypt',action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help='Text to process')
    parser.add_argument('key', type=str, help='Key for encryption or decryption')
    
    args = parser.parse_args()
    
    if not (args.encrypt or args.decrypt):
        parser.error("You must specify either --encrypt or --decrypt")
    
    cipher = VigenereCipher(args.text, args.key)
    if args.encrypt:
        result = cipher.encrypt()
        print(f"Encrypted: {result}")
    elif args.decrypt:
        result = cipher.decrypt()
        print(f"Decrypted: {result}")
        
if __name__ == "__main__":
    main()