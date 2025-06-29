#!/usr/bin/env python3

import argparse

class AffineCipher:
    def __init__(self,text, a, b):
        self.text = text
        self.a = a
        self.b = b

    def encrypt(self):
        encrypted = ''
        for ele in self.text:
            if ele.isalpha():
                x = ord(ele) - ord('A') if ele.isupper() else ord(ele) - ord('a')
                char = chr((self.a*x + self.b) %26 + (ord('A') if ele.isupper() else ord('a')))

                encrypted += char
            else:
                encrypted += ele
                
        return encrypted
            
    
    def decrypt(self):
        decrypted = ''
        a_inv = pow(self.a, -1,26)  # Modular inverse of a under modulo 26
        for ele in self.text:
            if ele.isalpha():
                x = ord(ele) - ord('A') if ele.isupper() else ord(ele) - ord('a')
                char = chr((a_inv * (x - self.b) % 26) + (ord('A') if ele.isupper() else ord('a')))
                decrypted += char
            else:
                decrypted += ele
                
        return decrypted
        
def main():
    parser = argparse.ArgumentParser(description='Affine Cipher encryption and decryption tool')
    
    parser.add_argument('-e', '--encrypt', action = 'store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action = 'store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help='Text to process')
    parser.add_argument('a', type=int, help='Multiplicative key (must be coprime to 26)')
    parser.add_argument('b', type=int, help='Additive key (0 <= b < 26)')
    
    args = parser.parse_args()
    
    if not (args.encrypt or args.decrypt):
        parser.error("You must specify either --encrypt or --decrypt")
    elif args.a <= 0 or args.a >= 26 or args.b < 0 or args.b >= 26:
        parser.error("Invalid keys: 'a' must be coprime to 26 and 'b' must be in the range 0 <= b < 26")

    cipher = AffineCipher(args.text, args.a, args.b)
    
    if args.encrypt:
        result = cipher.encrypt()
        print(f'Encrypted text: {result}')
    elif args.decrypt:
        result = cipher.decrypt()
        print(f'Decrypted text: {result}')  
        
if __name__ == '__main__':
    main()
