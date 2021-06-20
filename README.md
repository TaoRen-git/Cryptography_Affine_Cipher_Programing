# Cryptography

## Description
This is an affine cipher program that allows users to encrypt, decrypt, or decipher plaintext files containing ASCII text which may include symbols. The program will utilize the Python3 to achieve all core functions which base on Bezout’s theorem and the extended Euclidean algorithm. For an affine cipher, users select two integers a and b as the key pair, and the program invokes them from the command line. As with the Caesar and shift ciphers, the program encrypt the message character by character. Given a character of the plaintext message m, the encryption function E(m, a, b) is given by E(m, a, b) = (a · m + b) mod 128.

---
## Getting Started

### Dependencies

1. Download and install [python3](https://www.python.org/downloads/)
2. Open terminal and access the **Cryptography** folder

### Running the encrypt program
1. There is a example in the input file ```input/input_word.txt```
2. If you want to use other numbers, you can open and edit ```input/input_word.txt```. There is no special format of message, it just need to end with no space
3. Choose any number for encrypt key pair ({a}, {b})
4. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py encrypt input/input_word.txt output/output_number.txt [a] [b]
    ```
5. If ({a}, {b}) is a valid key, then the output number will store in the ```output/output_number.txt```, which should be printed out in terminal in the same time
6. If ({a}, {b}) is not a valid key, then the program should print the following message:
    ```
    The key pair ({a}, {b}) is invalid, please select another key.
    ```

### Running the decrypt program
1. There is a example in the input file ```input/input_number.txt```
2. If you want to use other numbers, you can open and edit ```input/input_number.txt```. Format of numbers should be like [number][space][number], and end with no space
3. Choose any number for decrypt key pair ({a}, {b})
4. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py decrypt input/input_number.txt output/output_word.txt [a] [b]
    ```
5. If ({a}, {b}) is a valid key, then the output word will store in the ```output/output_word.txt```, which should be printed out in terminal in the same time
6. If ({a}, {b}) is not a valid key, then the program should print the following message:
    ```
    The key pair ({a}, {b}) is invalid, please select another key.
    ```


### Running the decipher program
1. There is a example in the input file ```input/input_number.txt```
2. If you want to use other numbers, you can open and edit ```input/input_number.txt```. Format of numbers should be like [number][space][number], and end with no space
3. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py decipher input/input_number.txt output/output_word.txt dictionary.txt
    ```
4. Decipher will search all the possible set of key pairs ({a}, {b}). If ```dictionary.txt``` contains some words in a result, it will printed out the key pairs and message:
    ```
    [a] [b]
    DECIPHERED MESSAGE:
    These are some words that have been decrypted. Note the punctuation!
    ```
5. All possible results will be stored in ```output/output_word.txt```