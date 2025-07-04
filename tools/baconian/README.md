# Baconian Cipher Tool

This tool provides encryption and decryption for Baconian Cipher for standard(24 letters) and full alphabetic version. It is part of the CipherCrack suite for CTF and cryptography challenges.

## Features

- Encrypt the plaintext for either standard or full alphabetic keys
- Decrypt the plaintext for either standard or full alphabetic keys 

## Insrallation 

```zsh
# Make the script executable and copy to bin directory
sudo chmod +x baconian_cipher.py
sudo cp baconian_cipher.py /usr/local/bin/baconian
```

## Usage

``` 
# Encrypt the text
baconian -e "Text to encrypt" -t <type>

# Decrypt the text
baconian -d "Text to decrypt" -t <type>
```

## Arguments

### Positional Arguments
- 'text' -  Text to process

### Options 
-  `-h`, `--help`        : Show this help message and exit
-  `-e`, `--encrypt`    : Encrypt the text
-  `-d`,`--decrypt`   : Decrypt the text
-  `-t`, `--type` : Type of encryption or decryption (24 for standard,26 for full)

## Example

```zsh
baconian -e "The best revenge is not to be like your enemy" -t 24

Encrypted text: BAABA AABBB AABAA  AAAAB AABAA BAAAB BAABA  BAAAA AABAA BAABB AABAA ABBAA AABBA AABAA  ABAAA BAAAB  ABBAA ABBAB BAABA  BAABA ABBAB  AAAAB AABAA  ABABA ABAAA ABAAB AABAA  BABBA ABBAB BAABB BAAAA  AABAA ABBAA AABAA ABABB BABBA 

baconian -d "BAABA AABBB AABAA  AAAAB AABAA BAAAB BAABA  BAAAA AABAA BAABB AABAA ABBAA AABBA AABAA  ABAAA BAAAB  ABBAA ABBAB BAABA  BAABA ABBAB  AAAAB AABAA  ABABA ABAAA ABAAB AABAA  BABBA ABBAB BAABB BAAAA  AABAA ABBAA AABAA ABABB BABBA " 

Decrypted text : THEBESTREVENGEISNOTTOBELIKEYOVRENEMY
```

## Notes
- Non - alphabetic characater inputs are printed as they are 
- This cipher needs to enhaced and contributors are welcome to do any helpful contribution as per the contribution policy()
- Contributors please look at CONTRIBUTION.md file 
- Currently encryption and decryption is available for A/B and 0/1 translation
