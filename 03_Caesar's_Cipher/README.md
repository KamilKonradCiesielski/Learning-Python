# 🔐 Caesar Cipher Tool

A terminal-based implementation of the classic encryption algorithm, focusing on ASCII character manipulation and procedural logic.

## 🛠️ Logic Overview

The program follows these key steps:
* **User Input:** Accepts a plain text message and a shift key (integer).
* **Character Mapping:** Uses `ord()` to convert characters into their ASCII numeric values for mathematical shifting.
* **Smart Filtering:** Implements a `continue` guard clause to detect spaces, ensuring they remain unencrypted and the message remains readable.
* **Overflow Handling:** Includes boundary logic (`if znak_na_numer > 122`) to wrap lowercase letters back to the start of the alphabet (a-z).
* **Result Assembly:** Collects processed characters into a list and uses `.join()` for efficient string reconstruction.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Run: `python main.py`
3. Enter your shift key and the message you want to encrypt.

## 📈 Future Improvements
* Add support for uppercase letters (A-Z).
* Implement a decryption mode.
* Add input validation for non-integer keys.
