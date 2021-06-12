#!usr/bin/env/ python

import sys
import pyperclip
import os
import pyperclip

argument = sys.argv[1]
# creating a file
os.chdir("/home/stan/Desktop/shwe_project")
f = open(argument, "a")
paste = pyperclip.paste()
f.write(str(paste))
f.close()
print("[+] File created succesfully")

