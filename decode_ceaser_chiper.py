#!usr/bin/env python
import pyperclip
message = input("Message u want to decode: ")
LETTERS = "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~"


for i in range(len(LETTERS)):
    decode = ""

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - i

            if num < 0:
                num = num + len(LETTERS)
            decode = decode + LETTERS[num]
        else:
            decode = decode + symbol


    print(f"key {i} : {decode}")

