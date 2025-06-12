# Caesar Cipher Tool

This tool provides encryption, decryption, and brute-force breaking for the classic Caesar cipher. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features
- Encrypt plaintext using a specified shift
- Decrypt ciphertext using a specified shift
- Brute-force all possible shifts to break a Caesar cipher

## Usage

```zsh
# Encrypt text with a shift of 3
caesar -e 3 -c "hello"

# Decrypt text with a shift of 3
caesar -d 3 -c "khoor"

# Brute-force all possible shifts
caesar -b -c "xbs"
```

## Arguments
- `-e`, `--encrypt` : Encrypt the input text
- `-d`, `--decrypt` : Decrypt the input text
- `-b`, `--break`   : Brute-force all possible shifts
- `shift`           : Shift value (required for encrypt/decrypt)
- `-c`, `--ciphertext` : Text to process

## Example
```zsh
caesar -e 5 -c "flag"
caesar -d 5 -c "kqfl"
caesar -b -c "uryyb"
```

## Notes
- Only alphabetic characters are shifted; other characters remain unchanged.
- For more details, use `caesar --help`.

