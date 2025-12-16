#!/usr/bin/env python3

import sys
sys.path.insert(0, './tools')

from tools.caesar.caesar_cipher import CaesarCipher
from tools.affine.affine_cipher import AffineCipher
from tools.baconian.baconian_cipher import BaconianCipher
from tools.hill.hill_cipher import HillCipher
from tools.rot13.rot13 import Rot13Cipher
from tools.substitute.substitute import SubstitutionCipher
from tools.vignere.vignere import VigenereCipher


def display_menu():
    print("\n" + "="*50)
    print("         CipherCrack - Cipher Tool")
    print("="*50)
    print("\nAvailable Ciphers:")
    print("  1. Caesar Cipher")
    print("  2. Affine Cipher")
    print("  3. ROT13")
    print("  4. Vigenere")
    print("  5. Hill")
    print("  6. Baconian")
    print("  7. Substitution")
    print("  0. Exit")
    print("="*50)

def caesar_menu():
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Break Cipher (try all shifts)")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    
    cipher = CaesarCipher()
    
    if choice == '1':
        shift = int(input("Enter shift value (0-25): "))
        result = cipher.encrypt(text, shift)
        print(f"\nEncrypted text: {result}")
    elif choice == '2':
        shift = int(input("Enter shift value (0-25): "))
        result = cipher.decrypt(text, shift)
        print(f"\nDecrypted text: {result}")
    elif choice == '3':
        print("\nAll possible decryptions:")
        solutions = cipher.break_cipher(text)
        for shift, solution in solutions:
            print(f"  Shift {shift:2d}: {solution}")
    else:
        print("Invalid choice!")

def affine_menu():
    print("\n--- Affine Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    a = int(input("Enter key 'a' (must be coprime to 26, e.g., 1,3,5,7,9,11,15,17,19,21,23,25): "))
    b = int(input("Enter key 'b' (0-25): "))
    
    cipher = AffineCipher(text, a, b)
    
    if choice == '1':
        result = cipher.encrypt()
        print(f"\nEncrypted text: {result}")
    elif choice == '2':
        result = cipher.decrypt()
        print(f"\nDecrypted text: {result}")
    else:
        print("Invalid choice!")

def baconian_menu():
    print("\n--- Baconian Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    bacon_type = input("Enter type (24 for standard I=J/U=V, 26 for full alphabet) [default: 24]: ").strip()
    if bacon_type not in ['24', '26']:
        bacon_type = '24'
    
    cipher = BaconianCipher(text, bacon_type)
    
    if choice == '1':
        result = cipher.encrypt()
        print(f"\n{result}")
    elif choice == '2':
        result = cipher.decrypt()
        print(f"\n{result}")
    else:
        print("Invalid choice!")
        
def hill_menu():
    print("\n--- Hill Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    n = int(input("Enter matrix dimension n (for n x n matrix): "))
    
    cipher = HillCipher(n, text)
    
    if choice == '1':
        result = cipher.encrypt()
        print(f"\n{result}")
    elif choice == '2':
        result = cipher.decrypt()
        print(f"\n{result}")
    else:
        print("Invalid choice!")
        
def rot13_menu():
    print("\n--- ROT13 Cipher ---")
    print("(ROT13 is symmetric - encrypt and decrypt are the same)")
    text = input("Enter text: ").strip()
    
    cipher = Rot13Cipher()
    result = cipher.encrypt(text)
    print(f"\nResult: {result}")
    
def substitution_menu():
    print("\n--- Substitution Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    key = input("Enter substitution key (26 unique letters, e.g., QWERTYUIOPASDFGHJKLZXCVBNM): ").strip()
    
    if len(key) != 26 or not key.isalpha() or len(set(key.lower())) != 26:
        print("Error: Key must be 26 unique alphabetic characters!")
        return
    
    key_map = {chr(i + 97): key[i].lower() for i in range(26)}
    cipher = SubstitutionCipher(key_map)
    
    if choice == '1':
        result = cipher.encrypt(key, text)
        print(f"\nEncrypted text: {result}")
    elif choice == '2':
        result = cipher.decrypt(key, text)
        print(f"\nDecrypted text: {result}")
    else:
        print("Invalid choice!")
        
def vignere_menu():
    print("\n--- Vigenere Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("\nSelect operation: ").strip()
    text = input("Enter text: ").strip()
    key = input("Enter key: ").strip()
    
    cipher = VigenereCipher(text, key)
    
    if choice == '1':
        result = cipher.encrypt()
        print(f"\nEncrypted text: {result}")
    elif choice == '2':
        result = cipher.decrypt()
        print(f"\nDecrypted text: {result}")
    else:
        print("Invalid choice!")
        

def main():
    while True:
        display_menu()
        choice = input("\nSelect a cipher (0-7): ").strip()
        
        if choice == '0':
            print("\nGoodbye!")
            break
        elif choice == '1':
            caesar_menu()
        elif choice == '2':
            affine_menu()
        elif choice == '3':
            rot13_menu()
        elif choice == '4':
            vignere_menu()
        elif choice == '5':
            hill_menu()
        elif choice == '6':
            baconian_menu()
        elif choice == '7':
            substitution_menu()
        else:
            print("\nInvalid choice! Please select a valid option.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
