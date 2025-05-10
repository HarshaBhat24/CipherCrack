# CTF Tools

A collection of command line tools designed to help solve Capture The Flag (CTF) challenges more efficiently.

## Available Tools

- **Caesar Cipher** - A tool for encrypting and decrypting using the Caesar shift cipher
- **ROT13 Decoder** - Tool similar to Caesar cipher to solve rot13 

## Coming Soon

More cryptographic tools and utilities will be added one by one to expand this toolkit.

## Purpose

This project was created to enhance the CTF solving experience by providing quick and efficient command line tools that can be easily integrated into your workflow. Instead of jumping between various websites or building one-off scripts, these tools offer consistent interfaces and can be chained together for complex CTF challenges.

## Installation

```bash
# Clone the repository
git clone https://github.com/HarshaBhat24/CipherCrack.git
cd CipherCrack

# Copy the files to bin directory
sudo cp ./tools/<cipher_cracker>.py /usr/local/bin/caesar 
```

## Usage

Once installed, you can use the tools directly from your command line

```bash
# Get help for any tool
caesar --help 

# Decrypt the text by bruteforce example
caesar -b -c "xbs"
```

Documentation for each individual tool can be found in their respective directories.

## Contribution

Feel free to contribute by opening issues or submitting pull requests.
