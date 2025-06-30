#!/usr/bin/env python3

import argparse

class HillCipher:
    def __init__(self, n, text):
        self.n = n
        self.text = text
        
    def mat(self):
        print('Enter the key matrix (row-wise):')
        try:    
            matrix = []
            for i in range(self.n):
                matrix.append(list(map(int, input().split())))
            return matrix
        except Exception:
            print(f'Please enter exactly {self.n**2} elements')
            return None
            
    
    def mul(self,lst, matrix):
        product = []
        for i in range(len(matrix)):
            prod_sum = 0
            for j in range(len(matrix[i])):
                prod_sum += lst[j] * matrix[j][i]
            product.append(prod_sum % 26)
        return product
    
    def is_valid_mat(self,matrix):
        if len(matrix) != self.n:
            return False
        for row in matrix:
            if len(row) != self.n:
                return False
            
        return True
    
    def determinant(self, matrix):
        """Calculate determinant of matrix using cofactor expansion"""
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for i in range(n):
            # Create minor matrix
            minor = []
            for j in range(1, n):
                row = []
                for k in range(n):
                    if k != i:
                        row.append(matrix[j][k])
                minor.append(row)
            
            # Calculate cofactor
            cofactor = ((-1) ** i) * matrix[0][i] * self.determinant(minor)
            det += cofactor
        
        return det
    
    def mod_inverse(self, a, m=26):
        """Find modular inverse of a mod m using extended Euclidean algorithm"""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, _ = extended_gcd(a % m, m)
        if gcd != 1:
            return None  # No modular inverse exists
        return (x % m + m) % m    

    def matrix_inverse(self, matrix):
        """Calculate inverse of matrix mod 26"""
        det = self.determinant(matrix) % 26
        det_inv = self.mod_inverse(det, 26)
        
        if det_inv is None:
            return None
        
        n = len(matrix)
        if n == 1:
            return [[det_inv]]
        
        if n == 2:
            return [
                [(matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
                [(-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26]
            ]
        
        # For larger matrices, use adjugate matrix method
        # (Implementation would be more complex - for now, limit to 2x2)
        raise NotImplementedError("Matrix inversion for n>2 not implemented")

    def preprocess_text(self, text):
        """Extract only alphabetic characters and convert to uppercase"""
        processed = ''.join(char.upper() for char in text if char.isalpha())
        return processed
    
        
    def encrypt(self):
        encrypted = ''
        matrix = self.mat()
        
        working_text = ''
        for i in range(len(self.text)):
            if self.text[i].isalpha():
                working_text += self.text[i]
        
        if matrix is None:
            return "Error: Invalid matrix input"
        
        if not self.is_valid_mat(matrix):
            return "Error: Enter valid matrix"
        
        while len(working_text) % self.n != 0:
            working_text += 'X'
        
        for i in range(0, len(working_text),self.n):
            plaintext = working_text[i:i+self.n]
            lst = [-1]*len(plaintext)
            for j in range(len(plaintext)):
                if plaintext[j].isupper():
                    lst[j] = ord(plaintext[j]) - ord('A')
                elif plaintext[j].islower():
                    lst[j] = ord(plaintext[j]) - ord('a')
                else:
                    return "Please enter only alphabetic character"
             
            cipherd_list = self.mul(lst,matrix)
            
            for j in range(self.n):
                encrypted += chr(cipherd_list[j] + ord('A'))
                
        return 'Encrypted text: ' + encrypted
        
        
    def decrypt(self):
        matrix = self.mat()
        
        if matrix is None:
            return "Error: Invalid matrix input"
        
        if not self.is_valid_mat(matrix):
            return f"Error: Please enter {self.n} x {self.n} matrix as input"
        
        try:
            inverse_matrix = self.matrix_inverse(matrix)
            if inverse_matrix is None:
                return "Error: Matrix is not invertible (determinant = 0 or no inverse mod 26)"
        except NotImplementedError:
            return f"Error: Decryption for {self.n}x{self.n} matrices not yet implemented"
        
        working_text = self.preprocess_text(self.text)
        
        if len(working_text) % self.n != 0:
            return f"Error: Ciphertext length must be multiple of {self.n}"
        
        decrypted = ''
        for i in range(0, len(working_text), self.n):
            # Get block of n characters
            block = working_text[i:i+self.n]
            
            # Convert to numbers
            vector = [ord(char) - ord('A') for char in block]
            
            # Multiply by inverse matrix
            decrypted_vector = self.mul(vector, inverse_matrix)
            
            # Convert back to letters
            for num in decrypted_vector:
                decrypted += chr(num + ord('A'))
        
        return f'Decrypted text: {decrypted}'        
        
        
def main():
    parser = argparse.ArgumentParser(description = 'Hill Cipher encryption and dectryption')
    
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    
    parser.add_argument('text', type=str, help = 'Text to process')    
    
    parser.add_argument('-n', type=int, help='Dimension of the square matrix (n x n)')
        
    
    args = parser.parse_args()
    
    if not (args.encrypt or args.decrypt):
        parser.error("You must specify whether to encrypt or decrypt")
        
    cipher = HillCipher(args.n, args.text)
    
    if args.encrypt:
        result = cipher.encrypt()
        print(f'{result}')
    elif args.decrypt:
        result = cipher.decrypt()
        print(f'{result}')
        
if __name__ == '__main__':
    main()