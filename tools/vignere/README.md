# Vigenère Cipher Tool

This tool provides encryption and decryption for the Vigenère cipher using a repeating key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features

- Encrypt plaintext using a repeating keyword
- Decrypt ciphertext using a known keyword
- Handles non-alphabetic characters by leaving them unchanged

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
vignere -e "attack at dawn" "LEMON"
vignere -d "LXFOPV EF RNHR" "LEMON"
```

## Notes

- Only alphabetic characters are encrypted; other characters remain unchanged.
- The key is repeated cyclically to match the length of alphabetic characters.
- For more details, use `vignere --help`.
