# This is an affine cipher utility.
# The utility invokes from the command line to encrypt, decrypt,
# or decipher plaintext files containing ASCII text which may include symbols.

# Author: Tao Ren
# Version: Mar 2 2021

import sys
import math    

# encrypt helper
def ascii_encrypt(word, a, b):
    return " ".join(str(
        pow(a * ord(char) + b, 1, 128)) 
        for char in word)

def encrypt(a, b):

    if math.gcd(a, 128) == 0:
        print('The key pair ({', a)
        print('}, {', b)
        print('}) is invalid, please select another key.')
        return

    # read words from input file
    fr = open(in_file, "r")
    in_words = list(fr.read())

    # print(in_words)

    # empty out file
    fw = open(out_file, "w")
    fw.close()

    # encrypt input words to numbers
    fa = open(out_file, "a")
    for word in in_words:
        fa.write(ascii_encrypt(word, a, b))
        if word != in_words[len(in_words) - 1]:
            fa.write(' ')
    fa.close()

    # print outupt check
    fr = open(out_file, "r")
    out_numbers = fr.read().split(' ')
    print(out_numbers)

# decrypt helper
def ascii_decrypt(number, a, b):
    return " ".join(str(chr(int (number) * pow (a, -1, 128) - b)))

# decrypt input number to words
def decrypt(a, b):

    if math.gcd(a, 128) == 0:
        print('The key pair ({', a)
        print('}, {', b)
        print('}) is invalid, please select another key')
        return

    # read numbers from input file
    fr = open(in_file, "r")
    in_numbers = fr.read().split(' ')

    print(in_numbers)

    fw = open(out_file, "w")
    fw.close()

    fa = open(out_file, "a")

    for number in in_numbers:
        fa.write(ascii_decrypt(number, a, b))
    fa.close()

    # print outupt check
    fr = open(out_file, "r")
    out_numbers = fr.read()
    print(out_numbers)

# decipher input number to all possible words
def decipher(dictionary_file):

    fr = open(in_file, "r")
    in_numbers = fr.read().split(' ')

    fr = open(dictionary_file, "r")
    dictionary = fr.read().split('\n')

    a = 0
    b = 0
    i = 1
    j = 0
    count = 0
    record = 0

    for i in range(3):
        # if math.gcd(i, 128) != 0:
        if i != 0:
            for j in range(3):
                # decrypt all number and split the string to word, then check
                decryptString = ""
                for number in in_numbers: 
                    print('i: ', i, ' j: ', j)
                    letter = ascii_decrypt(number, i, j)
                    decryptString = decryptString + letter
                print(decryptString + '\n')
                #     if word in dictionary:
                #         count = count + 1

                # if count > record:
                #     record = count
                #     a = i
                #     b = j

                # count = 0
            
    print(a, b, '\nDECIPHERED MESSAGE:\nThese are some words that have been decrypted. Note the punctuation!\n')

call = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]

# affine encrypt
if call == 'encrypt':
    encrypt(int(sys.argv[4]), int(sys.argv[5]))
# affine decrypt
elif call == 'decrypt':
    decrypt(int(sys.argv[4]), int(sys.argv[5]))
# affine decipher
elif call == 'decipher':
    decipher(sys.argv[3])