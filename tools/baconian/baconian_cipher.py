#!/usr/bin/env python3

import argparse

class BaconianCipher:
    def __init__(self,text,type):
        self.text = text
        self.type = type
        
    def get_bacons(self):
        cipher = {}
        if self.type == '24':
            letters = 'ABCDEFGHIKLMNOPQRSTUWXYZ'
            for i,val in enumerate(letters):
                binary = format(i,'05b')
                bacon = binary.replace('0','A').replace('1','B')
                cipher[val] = bacon
            
            cipher['J'] = cipher['I']
            cipher['V'] = cipher['U']
        elif self.type == '26':
            for i in range(26):
                val = chr(i + ord('A'))
                binary = format(i, '05b')
                bacon = binary.replace('0','A').replace('1','B')
                cipher[val] = bacon
                
        return cipher
        
        
    def encrypt(self):
        encrypted = ''
        bacons = self.get_bacons()
        for ele in self.text:
            if ele.isalpha():
                encrypted += bacons[ele.upper()]
                encrypted += ' '
            else:
                encrypted += ele
        return 'Encrypted text : ' + encrypted    

    def decrypt(self):
        decrypted = ''
        bacons = self.text.split(' ')
        
        reverse_map = {}
        cipher = self.get_bacons()
        
        for letter, code in cipher.items():
            reverse_map[code] = letter
        
        for bacon in bacons:
            bacon = bacon.strip()
            if len(bacon) == 5 and all(c in 'ABab' for c in bacon):
                bacon = bacon.upper()
                if bacon in reverse_map:
                    if self.type == '24':
                        if reverse_map[bacon] == 'I':
                            decrypted += '(I/J)'
                        elif reverse_map[bacon] == 'U':
                            decrypted += '(U/V)'
                        else:
                            decrypted += reverse_map[bacon]
                    else:
                        decrypted += reverse_map[bacon]
                else:
                    binary = bacon.replace('A','0').replace('B','1')
                    try:
                        dec = int(binary, 2)
                        if dec < 26:
                            decrypted += chr(dec + ord('A'))
                        else:
                            decrypted += f'[{bacon}]'
                    except ValueError:
                        decrypted += f'[{bacon}]'
            elif bacon == '':
                continue
            else:
                decrypted += ' ' + bacon
            
        return 'Decrypted text : ' + decrypted        
        
def main():
    parser = argparse.ArgumentParser(description='Baconian Cipher Solver')
    
    parser.add_argument('-e', '--encrypt',action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help='Text to process')
    parser.add_argument('-t','--type', type=str, default='24', help='Type of encryption or decryption (24 for standard,26 for full)')
    
    args = parser.parse_args()
    
    if not (args.decrypt or args.encrypt):
        parser.error('You must specify whether to encrypt or decrypt using any of -e,-d,--encrypt,--decrypt')
    
    if not args.type:
        args.type = '24'
    
    cipher = BaconianCipher(args.text,args.type)
    
    if args.encrypt:
        result = cipher.encrypt()
        print(result)
    elif args.decrypt:
        result = cipher.decrypt()
        print(result)
    
if __name__ == "__main__":
    main()