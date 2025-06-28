# Affine Cipher Tool

This tool provides encryption and decryption for the Affine cipher using a repeating key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features

- Encrypt plaintext using two integer variables between 1 and 25 (only odd numbers except 13)
- Decrypt ciphertext using two integer variables between 1 and 25 (only odd numbers except 13)
- Handles non-alphabetic characters by leaving them unchanged

## Installation

```zsh
# Make the script executable and copy to bin directory
sudo chmod +x affine_cipher.py
sudo cp affine_cipher.py /usr/local/bin/affine
```

## Usage

```zsh
# Encrypt text with a key
affine -e "text-to-encrypt" <a> <b>

# Decrypt text with a key
affine -d "text-to-decrypt" <a> <b>
```

## Arguments

- `-e`, `--encrypt` : Encrypt the input text
- `-d`, `--decrypt` : Decrypt the input text
- `text`            : Text to process
- `a`               : Co - prime integer with 26
- `b`               : Integer number (0<=b<=26) 

## Example

```zsh
affine -e "we are men,we must win" 11 7
vignere -d "pz hmz jzu,pz jtxi pru" 11 7
```

## Notes

- Only alphabetic characters are encrypted; other characters remain unchanged.
- For more details about the usage of tool, use `affine --help`.
