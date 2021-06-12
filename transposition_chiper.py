#!usr/bin/env python

import pyperclip
import pyinputplus as pyin

def main():
    message = input("Enter a message: ")
    key = pyin.inputNum("Enter a key: ")
    chipertext = encrypt_message(key, message)
    print(chipertext + '|')
    pyperclip.copy(chipertext)

def encrypt_message(key, message):
    chipertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            chipertext[col] += message[pointer]
            pointer += key
    return ''.join(chipertext)

if __name__ == '__main__':
    main()