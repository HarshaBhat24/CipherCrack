#!/usr/bin/env python3

import argparse

class SubstitutionCipher:
    def __init__(self, key):
        self.key = key
        self.inverse_key = {v: k for k, v in key.items()}
    
    def encrypt(self,key, text):
        char_map = dict(zip("abcdefghijklmnopqrstuvwxyz", key.lower()))
        return ''.join([char_map[x] if x in char_map else x for x in text.lower()])
              
    
    def decrypt(self,key, text):
        
        char_map = dict(zip("abcdefghijklmnopqrstuvwxyz", key.lower()))            
        
        return ''.join([char_map[x] if x in char_map else x for x in text.lower()])
    
def main():
    parser = argparse.ArgumentParser(description='Substitution Cipher encryption and decryption tool')
    
    parser.add_argument('-k', '--key', type=str, required=True, help='Substitution key as a string of 26 characters')
    parser.add_argument('-t', '--text', type=str, required=True, help='Text to process')
    
    args = parser.parse_args()
    if len(args.key) != 26 or not args.key.isalpha() or len(set(args.key.lower())) != 26:
        parser.error("Key must be a string of 26 unique alphabetic characters")
        
    cipher = SubstitutionCipher({chr(i + 97): args.key[i].lower() for i in range(26)})

    if args.key:
        result = cipher.decrypt(args.key, args.text)
        print(f"Decrypted: {result}")
    else:
        parser.error("You must specify either --encrypt or --decrypt")
        
        
if __name__ == "__main__":
    main()