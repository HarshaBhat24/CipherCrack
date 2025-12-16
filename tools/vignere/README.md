# Vigenère Cipher Tool

This tool provides encryption and decryption for the Vigenère cipher using a repeating key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features

- Encrypt plaintext using a repeating keyword
- Decrypt ciphertext using a known keyword
- Handles non-alphabetic characters by leaving them unchanged

## Quick Start (Interactive Mode)

You can access this cipher through the main CipherCrack menu:

```zsh
# From the CipherCrack root directory
python main.py
# Then select option 4 for Vigenère Cipher
```

## Installation (Standalone)

```zsh
# Make the script executable and copy to bin directory
sudo chmod +x vignere.py
sudo cp vignere.py /usr/local/bin/vignere
```

## Usage

```zsh
# Encrypt text with a key
vignere -e "hello world" "KEY"

# Decrypt text with a key
vignere -d "RIJVS AIDPH" "KEY"
```

## Arguments

- `-e`, `--encrypt` : Encrypt the input text
- `-d`, `--decrypt` : Decrypt the input text
- `text`            : Text to process
- `key`             : Keyword for encryption or decryption

## Example

```zsh
vignere -e "we are men, we must win" "stoic"
vignere -d "OX OZG EXB, EG ENGB YAG" "stoic"
```

## Notes

- Only alphabetic characters are encrypted; other characters remain unchanged.
- The key is repeated cyclically to match the length of alphabetic characters.
- For more details, use `vignere --help`.
