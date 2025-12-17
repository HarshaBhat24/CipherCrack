#!/usr/nin/env python3

import argparse

class atbashCipher:
    def __init__(self, text):
        self.text = text

    def encrypt(self):
        encrypted = ''
        for ele in self.text:
            if ele.isalpha():
                if ele.isupper():
                    char = chr(ord('Z') - (ord(ele) - ord('A')))
                else:
                    char = chr(ord('z') - (ord(ele) - ord('a')))
                encrypted += char
            else:
                encrypted += ele
        return encrypted

    def decrypt(self):
        # Atbash cipher is symmetric; encryption and decryption are the same
        return self.encrypt()
    
def main():
    parser = argparse.ArgumentParser(description='Atbash Cipher encryption and decryption tool')
    
    parser.add_argument('-e', '--encrypt', action = 'store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action = 'store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help='Text to process')
    
    args = parser.parse_args()
    
    if not (args.encrypt or args.decrypt):
        parser.error("You must specify either --encrypt or --decrypt")

    cipher = atbashCipher(args.text)
    
    if args.encrypt:
        result = cipher.encrypt()
        print(f'Encrypted text: {result}')
    elif args.decrypt:
        result = cipher.decrypt()
        print(f'Decrypted text: {result}')
        
if __name__ == "__main__":
    main()