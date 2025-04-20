#!/usr/bin/env python3

import argparse

class CaesarCipher:
    def __init__(self):
        pass
        
    def encrypt(self, text, shift):
        return self._cipher(text, shift)
    
    def decrypt(self, text, shift):
        return self._cipher(text, -shift)
    
    def break_cipher(self, ciphertext):
        possible_solutions = []
        
        for shift in range(26):
            decrypted = self.decrypt(ciphertext, shift)
            possible_solutions.append((shift, decrypted))
        
        return possible_solutions
    
    def _cipher(self, text, shift):
        result = ""
        
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                
                shifted = (ord(char) - ascii_offset + shift) % 26
                
                result += chr(shifted + ascii_offset)
            else:
                result += char
        
        return result

def main():
    parser = argparse.ArgumentParser(description='Caesar Cipher encryption, decryption, and breaking tool')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the text')
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    group.add_argument('-b', '--break', dest='break_cipher', action='store_true', help='Break the cipher by trying all shifts')
    
    parser.add_argument('shift', type=int, nargs='?', help='Shift value for encryption or decryption')
    parser.add_argument('-c', '--ciphertext', type=str, required=True, help='Text to process')
    
    args = parser.parse_args()
    
    if (args.encrypt or args.decrypt) and (args.shift is None):
        parser.error("Encryption and decryption require a shift value")
    
    cipher = CaesarCipher()
    
    if args.encrypt:
        result = cipher.encrypt(args.ciphertext, args.shift)
        print(f"Encrypted (shift {args.shift}): {result}")
    elif args.decrypt:
        result = cipher.decrypt(args.ciphertext, args.shift)
        print(f"Decrypted (shift {args.shift}): {result}")
    elif args.break_cipher:
        print("All possible decryptions:")
        solutions = cipher.break_cipher(args.ciphertext)
        for shift, solution in solutions:
            print(f"Shift {shift}: {solution}")

if __name__ == "__main__":
    main()