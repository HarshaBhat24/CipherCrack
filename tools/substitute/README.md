# Substitution Cipher Tool

This tool provides encryption and decryption for monoalphabetic substitution ciphers using a custom 26-letter key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features
- Encrypt or decrypt text using a user-supplied key
- Supports any valid 26-letter permutation as the key

## Quick Start (Interactive Mode)

You can access this cipher through the main CipherCrack menu:

```zsh
# From the CipherCrack root directory
python main.py
# Then select option 7 for Substitution Cipher
```

## Installation (Standalone)

```zsh
# Make the script executable and copy to bin directory
sudo chmod +x substitute.py
sudo cp substitute.py /usr/local/bin/substitute
```

## Usage

```zsh
# Decrypt text with a custom key
substitute -k QWERTYUIOPASDFGHJKLZXCVBNM -t "itssg"
```

## Arguments
- `-k`, `--key`  : Substitution key (26 unique alphabetic characters)
- `-t`, `--text` : Text to process

## Example
```zsh
substitute -k QWERTYUIOPASDFGHJKLZXCVBNM -t "hello"
```

## Notes
- The key must be exactly 26 unique alphabetic characters.
- For more details, use `substitute --help`.

