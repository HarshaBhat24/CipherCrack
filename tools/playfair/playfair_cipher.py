#!/usr/bin/env python3

import argparse

class PlayFairCipher:
    def __init__(self,text,key):
        self.text = text
        self.key = key
       
    def grid(self):
        seen = set()
        seq = []
        k = self.key.upper()
        for char in k:
            if char not in seen and char.isalpha():
                seen.add(char)
                if char.upper() == 'J' or char.upper() == 'I':
                    seq.append('I')
                    seen.add('I')
                    seen.add('J')
                else:
                    seq.append(char.upper())
        for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in seen:
                seq.append(char)
                seen.add(char)
        mat = [seq[i:i+5] for i in range(0, 25, 5)]
        return mat
    
    
    def get_pair(self):
        pairs = []
        text = self.text.upper().replace('J', 'I').replace(' ', '')
        i = 0
        n = len(text)
        while i < n:
            if i + 1 < n and text[i] == text[i + 1]:
                pairs.append([text[i], 'X'])
                i += 1
            elif i + 1 < n:
                pairs.append([text[i], text[i + 1]])
                i += 2
            else:
                pairs.append([text[i], 'X'])
                i += 1
        return pairs

    def encrypt(self):
        encrypted = ''
        mat = self.grid() 
        pairs = self.get_pair()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=' ')
            print()  
        print("Pairs:", pairs)
        print(mat[2][3],pairs[0][0],mat[2][3]==pairs[0][0] )
        return "Encrypted text : not yet implemented" + encrypted
    
    def decrypt(self):
        decrypted = ''
        
        return "Decrypted text : not yet implemented" + decrypted
    
    
def main():
    parser = argparse.ArgumentParser(description='Playfair Cipher Solver')
    
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help="Text to process")
    parser.add_argument('key', type=str, help="Key for encryption/decryption")
    
    args = parser.parse_args()

    if not (args.encrypt or args.decrypt):
        parser.error("Please specify either -e/--encrypt for encryption or -d/--decrypt for decryption.")
        
    if not args.key:
        parser.error("You must provide a key for the Playfair cipher.")
    
    if not args.text:
        parser.error("You must provide text to encrypt or decrypt.")
        
    cipher = PlayFairCipher(args.text, args.key)
    
    if args.encrypt:
        print(cipher.encrypt())
    elif args.decrypt:
        print(cipher.decrypt())
        
if __name__ == "__main__":
    main()