# Substitution Cipher Tool

This tool provides encryption and decryption for monoalphabetic substitution ciphers using a custom 26-letter key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features
- Encrypt or decrypt text using a user-supplied key
- Supports any valid 26-letter permutation as the key

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

