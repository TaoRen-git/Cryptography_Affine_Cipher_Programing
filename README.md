# Cryptography

## Description
This is an affine cipher program. This program invokes from the command line to encrypt, decrypt, or decipher plaintext files containing ASCII text which may include symbols.


---
## File Structure
```
Cryptography
├───input                          
│   ├───input_number.txt       # numbers for decrypt
│   ├───input_word.txt         # words for encrypt
├───output                          
│   ├───output_number.txt      # encrypted numbers
│   └───output_word.txt        # decrypted words
├───affine.py                  # ASCII affine program
├───dictionary.txt             # dictionary for decipher
└───README.md                  # Read me doc
```
---

## Getting Started

### Dependencies

1. Download and install [python3](https://www.python.org/downloads/)
2. Open terminal and access the **Cryptography** folder

### Running the encrypt program
1. Open and edit ```input/input_word.txt```
2. Choose any number for encrypt key pair ({a}, {b})
3. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py encrypt input/input_word.txt output/output_number.txt [a] [b]
    ```
4. If ({a}, {b}) is a valid key, then the output number will store in the ```output/output_number.txt```, which should be printed out in terminal in the same time.
5. If ({a}, {b}) is not a valid key, then the program should print the following message ```"The key pair ({a}, {b}) is invalid, please select another key."```

### Running the decrypt program
1. Open and edit ```input/input_number.txt```
2. Choose any number for decrypt key pair ({a}, {b})
3. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py decrypt input/input_number.txt output/output_word.txt [a] [b]
    ```
4. If ({a}, {b}) is a valid key, then the output word will store in the ```output/output_word.txt```, which should be printed out in terminal in the same time
5. If ({a}, {b}) is not a valid key, then the program should print the following message ```"The key pair ({a}, {b}) is invalid, please select another key."```


### Running the decipher program
1. Open and edit ```input/input_number.txt```
2. Run this command under **Cryptography** folder
    ```bash
    python3 affine.py decipher input/input_number.txt output/output_word.txt dictionary.txt
    ```
3. Decipher will search all the possible set of key pairs ({a}, {b}). If ```dictionary.txt``` contains some words in a result, it will printed out the key pairs and message:
    ```
    [a] [b]
    DECIPHERED MESSAGE:
    These are some words that have been decrypted. Note the punctuation!
    ```
4. All possible results will be stored in ```output/output_word.txt```