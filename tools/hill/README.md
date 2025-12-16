# Hill Cipher Tool

This tool provides encryption and decryption for Hill Cipher using N x N matrix input as key. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features

- Encrypt plaintext using N x N matrix input while ignoring whitespaces 
- Decrypt plaintext using N x N matrix input while ignoring whitespaces(Upto 2x2 matrix input as key)

## Quick Start (Interactive Mode)

You can access this cipher through the main CipherCrack menu:

```zsh
# From the CipherCrack root directory
python main.py
# Then select option 5 for Hill Cipher
```

## Installation (Standalone)

```zsh 
# Make the script executable and copy to bin directory
sudo chmod +x hill_cipher.py
sudo cp hill_cipher.py /usr/local/bin/hill
```

## Usage

```
# Encrypt text with the matrix
hill -e "text-to-encrypt" -n <dimension>

# Decrypt text with the matrix
hill -d "text-to-decrypt" -n <dimension>
```

## Arguments

### Positional Arguments:
-  'text' - Text to process

### Options:
-  `-h`, `--help`        : Show this help message and exit
-  `-e`, `--encrypt`    : Encrypt the text
-  `-d`,`--decrypt`   : Decrypt the text
-  `-n`, `N`          : Dimension of the square matrix (n x n)

## Example

```zsh
hill -e "if not now then when" -n 4
```
Enter the key matrix (row-wise):<br>
1 5 9 6<br>
3 2 4 8<br>
7 1 0 5<br>
1 1 1 1<br>
Encrypted text: YZCLWBLYDWEVGLFN

```
hill -d "CPRSTZYIVVEVYBEV" -n 2
```
Enter the key matrix (row-wise):<br>
1 2 <br>
4 5 <br>
Decrypted text: IFNOTNOWTHENWHEN

## Notes

- Enter only alphabetic characters for encryption and decryption
- Do not enter anything other than integer for matrix
- Follow the format for matrix input
- Currently decryption allowed only upto 2x2 matrix