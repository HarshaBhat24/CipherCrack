#!/usr/bin/env python3

import argparse

class Rot13Cipher:
    def __init__(self):
        pass

    def encrypt(self, text):
        return self._cipher(text)

    def decrypt(self, text):
        return self._cipher(text)

    def _cipher(self, text):
        result = ""

        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shifted = (ord(char) - ascii_offset + 13) % 26
                result += chr(shifted + ascii_offset)
            else:
                result += char

        return result
    
def main():
    parser = argparse.ArgumentParser(description='ROT13 encryption and decryption tool')
    
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')    
    
    parser.add_argument('text', type=str, help='Text to process')

    args = parser.parse_args()
    if not (args.encrypt or args.decrypt):
        parser.error("You must specify either --encrypt or --decrypt")
        
    cipher = Rot13Cipher()
    result = cipher.encrypt(args.text)
    print(f"Encrypted: {result}")


if __name__ == "__main__":
    main()