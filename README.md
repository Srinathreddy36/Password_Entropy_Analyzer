# 🔐 Garuda Sentinel - Password Entropy Analyzer

**Password Entropy Analyzer** is a part of the Garuda Sentinel cybersecurity mission. It analyzes the strength and entropy of a given password or key using information theory principles like Shannon entropy and bit entropy. The tool evaluates the guessability of the password and estimates the time required to crack it using brute force.

## 📘 Based On
This project is inspired by **Chapter 2** of the book _"Serious Cryptography"_ by Jean-Philippe Aumasson, which introduces entropy and randomness as core concepts in cryptographic security.

---

## 🚀 Features

- Calculates **Shannon Entropy** of the password
- Estimates **bit entropy** based on character sets used
- Classifies password strength as: **Weak**, **Medium**, or **Strong**
- Estimates **brute-force crack time** based on entropy
- Gives **human-readable feedback and suggestions** to improve weak passwords

---

## 📦 Dependencies

- Python 3.6+
- No external libraries needed (uses built-in modules)

---

## 🛠️ How It Works

1. User inputs a password or key
2. The script:
   - Measures password length
   - Identifies used character sets (lowercase, uppercase, digits, symbols)
   - Calculates:
     - Character pool size (entropy base)
     - Shannon entropy
     - Bit entropy (`log2(pool_size) * length`)
   - Estimates total combinations
   - Simulates brute-force crack time at `10^9 guesses/second`
3. Displays:
   - Entropy values
   - Estimated time to crack
   - Password strength category
   - Suggestions to strengthen weak passwords
  📈 Improvements & Suggestions
Increase password length

Use a mix of character types (uppercase, lowercase, digits, symbols)
Avoid dictionary words or common patterns

🔐 Mission Context
This tool is Project 8 under the Garuda Sentinel cybersecurity initiative, aiming to build real-world security tools based on fundamental cryptographic principles.

---

## 💻 Usage

```bash
$ python Password_Entropy_Analyzer.py
Enter a password/key to analyze: john@123A$121
Example output:
[+] Shannon Entropy: 3.23 bits/char
[+] Bit Entropy: 85.30 bits
[+] Crack Time Estimate: 203.45 million years
[+] Strength: STRONG ✅
