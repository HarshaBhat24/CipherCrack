Contributing to CipherCrack
Thank you for your interest in contributing to CipherCrack, a professional suite of command-line tools for solving cryptographic challenges in Capture The Flag (CTF) competitions and beyond. We welcome contributions from the community to enhance our toolkit, add new ciphers, improve performance, or refine documentation. This guide outlines how to contribute effectively to ensure a smooth and collaborative process.
How to Contribute
1. Getting Started

Read the README: Familiarize yourself with the project’s goals, structure, and existing tools in the README.md.
Check Issues: Browse the Issues page for bugs, feature requests, or tasks labeled good first issue or help wanted.
Join the Discussion: Propose new ciphers, features, or improvements by opening an issue before starting work to align with the project vision.

2. Setting Up the Project

Fork the Repository: Fork the CipherCrack repository to your GitHub account.
Clone Your Fork:git clone https://github.com/your-username/ciphercrack.git
cd ciphercrack

Create a Branch:git checkout -b feature/your-feature-name

3. Contribution Types
We welcome contributions in the following areas:

New Cipher Tools: Add support for ciphers like Playfair, Rail Fence, or modern algorithms.
Bug Fixes: Improve existing tools (e.g., tools/hill/, tools/vignere/) for performance or accuracy.
Cryptanalysis Features: Implement frequency analysis, key guessing, or scoring mechanisms for English text.
Documentation: Enhance tool-specific READMEs, add examples, or improve this CONTRIBUTION.md.
Testing: Add CTF-style test cases.
Performance Optimizations: Optimize algorithms (e.g., use str.translate for substitutions) or reduce memory usage.

4. Coding Guidelines
To maintain consistency across CipherCrack, please follow these Python-specific guidelines:

Code Style: Adhere to PEP 8. Use tools like flake8 or black for formatting.
File Structure:
Place new cipher tools in tools/<cipher_name>/ (e.g., tools/playfair/).
Include a README.md in each tool directory with usage instructions and examples.
Example structure for a new tool:tools/playfair/
├── playfair.py
├── README.md

CLI Interface: Use argparse for consistent command-line interfaces. Support --help, input text, and optional parameters (e.g., --key).
Example: python playfair.py "BMODZ" --key "MONARCHY"

Modularity: Write reusable functions (e.g., encrypt, decrypt, analyze) in each tool.
Error Handling: Include robust input validation and clear error messages.
Performance: Optimize for CTF-style inputs (short texts).Avoid nested loops where possible.
Dependencies: Prefer standard libraries.
Testing: Add unit tests in tools/<cipher_name>/tests/ using pytest. Test edge cases (e.g., empty input, invalid keys).

5. Submitting a Pull Request

Commit Changes:
Use clear, concise commit messages (e.g., Add Playfair cipher solver with cryptanalysis).
Group related changes into logical commits.

Update Documentation:
Update the main README.md to list new tools or features.
Include a README.md for new tools with usage examples.

Run Tests:pytest tools/<cipher_name>/tests/

Push to Your Fork:git push origin feature/your-feature-name

Open a Pull Request:
Submit a PR to the main branch of the main repository.
Include a detailed description of your changes, referencing related issues (e.g., Fixes #123).

Code Review: Respond to feedback promptly. Maintainers may request changes to align with project standards.

6. Reporting Issues

Use the Issues page to report bugs or suggest features.
For bugs, include:
Tool name (e.g., tools/vignere).
Input, expected output, and actual output.
Steps to reproduce.


For feature requests, describe:
The proposed cipher or feature.
Its relevance to CTF or cryptography.
Example use case.



7. Community Guidelines

Be respectful and inclusive in all interactions.
Provide constructive feedback during code reviews.
Acknowledge contributions from others (e.g., credit prior work in PR descriptions).

8. Roadmap Ideas
Check the README.md for the project roadmap. Some ideas for contributions include:

Implementing ciphers like Playfair, Rail Fence, or Columnar Transposition.
Adding frequency analysis tools for substitution ciphers.
Supporting batch processing (e.g., decrypt multiple inputs from a file).
Integrating with CTF platforms (e.g., parsing CryptoHack challenge formats).

9. Getting Help

Join discussions on the Issues page.
Reach out to maintainers via GitHub for guidance on complex contributions.
Refer to CTF resources like CryptoHack for cipher examples and test cases.

Thank You!
Your contributions help make CipherCrack a better tool for CTF enthusiasts and cryptographers. Let’s break those ciphers together!
CipherCrack: For hackers, by hackers.
