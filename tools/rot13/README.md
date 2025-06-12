# ROT13 Cipher Tool

This tool provides encoding and decoding for the ROT13 cipher. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features
- Encode or decode text using the ROT13 cipher
- Simple, stateless transformation (same operation for encode/decode)

## Usage

```zsh
# Encode text
rot13 --encrypt "hello"

# Decode text
rot13 --decrypt "uryyb"
```

## Arguments
- `-e`, `--encrypt` : Encode the input text
- `-d`, `--decrypt` : Decode the input text
- `text`            : Text to process

## Example
```zsh
rot13 --encrypt "flag"
rot13 --decrypt "synt"
```

## Notes
- Only alphabetic characters are shifted; other characters remain unchanged.
- For more details, use `rot13 --help`.

