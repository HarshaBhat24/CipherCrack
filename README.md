# CTF Tools: CipherCrack

CipherCrack is a professional suite of command-line tools designed for Capture The Flag (CTF) participants, cryptography practitioners, and puzzle solvers. The toolkit provides modular, extensible, and efficient utilities for working with classic ciphers and cryptographic techniques directly from the terminal. CipherCrack streamlines the process of solving cryptographic challenges by offering reliable, scriptable, and well-documented tools.

## Quick Start

Run the interactive menu from the root directory:

```bash
python main.py
```

This launches an interactive menu where you can select any cipher and perform encryption/decryption operations.

## Installation (System-wide Command)

To use CipherCrack as a command-line tool from anywhere:

```bash
# Make the script executable
chmod +x main.py

# Create a symbolic link (replace the path with your actual path)
sudo ln -s /home/YOUR_USERNAME/path/to/CipherCrack/main.py /usr/local/bin/ciphercrack
```

Now you can run `ciphercrack` from anywhere in your terminal.

## Features

- **Interactive Menu:** User-friendly interface via `main.py` for easy access to all ciphers.
- **Modular Architecture:** Each cipher tool is organized in its own directory for clarity and maintainability.
- **Command-Line Interface:** All tools are optimized for terminal usage, supporting scripting and automation.
- **Consistent User Experience:** Unified interfaces and robust error handling across all tools.
- **Open Source & Extensible:** Contributions are encouraged to expand the toolkit and improve existing features.

## Available Tools

| Cipher | Location | Features |
|--------|----------|----------|
| **Caesar Cipher** | `tools/caesar/` | Encrypt, Decrypt, Break (brute-force all 26 shifts) |
| **Affine Cipher** | `tools/affine/` | Encrypt, Decrypt with keys a & b |
| **ROT13 Decoder** | `tools/rot13/` | Symmetric encode/decode |
| **Vigenère Cipher** | `tools/vignere/` | Encrypt, Decrypt with keyword |
| **Hill Cipher** | `tools/hill/` | Encrypt, Decrypt with n×n matrix |
| **Baconian Cipher** | `tools/baconian/` | Encrypt, Decrypt (24 or 26 letter alphabet) |
| **Substitution Cipher** | `tools/substitute/` | Encrypt, Decrypt with 26-letter key |

Each tool includes its own README with detailed usage instructions and examples.

## Roadmap

- Additional ciphers (Hex, rc2, etc.)
- Frequency analysis tools
- Interactive and batch processing modes
- Integration with other CTF utilities

## Project Vision

CipherCrack is built on the principles of speed, reliability, and community collaboration. The goal is to provide a dependable toolkit that enables users to solve cryptographic challenges efficiently, without leaving the command line.

## Contribution

Contributions are welcome. Please open issues, suggest features, or submit pull requests to help improve CipherCrack.---

*CipherCrack: For hackers, by hackers. May your flags be plentiful and your ciphers be weak.*
