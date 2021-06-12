#!usr/bin/env/ python
import subprocess
import time
import os
from pathlib import Path
import pyinputplus as pyip
import re
from prettytable import PrettyTable
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

subprocess.call(["clear"])

prLightPurple( '''

╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╭━╮╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮╭╮╭━╮╭╮
┃╭━━╯╱╱┃┃╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱┃╭━╮┃┃╭╯┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃┃┃┃╭╋╯╰╮
┃╰━━┳━━┫╰━┳━┳┳━━┳━┻╮╭╋┳━━┳━╮╱┃┃╱┃┣╯╰╮┃┃╱╱╭┳━╮╭╮╭┳╮╭╮╰╯┃┃┣┻━┳━━┫┃┃╰╯╯┣╮╭╯
┃╭━━┫╭╮┃╭╮┃╭╋┫╭━┫╭╮┃┃┣┫╭╮┃╭╮╮┃┃╱┃┣╮╭╯┃┃╱╭╋┫╭╮┫┃┃┣╋╋╯╱╱┃┃┃╭╮┃╭╮┃┃┃╭╮┃┣┫┃
┃┃╱╱┃╭╮┃╰╯┃┃┃┃╰━┫╭╮┃╰┫┃╰╯┃┃┃┃┃╰━╯┃┃┃╱┃╰━╯┃┃┃┃┃╰╯┣╋╋╮╱╱┃┃┃╰╯┃╰╯┃╰┫┃┃╰┫┃╰╮
╰╯╱╱╰╯╰┻━━┻╯╰┻━━┻╯╰┻━┻┻━━┻╯╰╯╰━━━╯╰╯╱╰━━━┻┻╯╰┻━━┻╯╰╯╱╱╰╯╰━━┻━━┻━┻╯╰━┻┻━╯
''')

prYellow("---------------------------------------------------------------------------------------------------")

def options():
    try:

        while True:
            list1=("\n\n 0. Exit\t 1. Add User \t 2. Update System\t 3. Upgrade System \t 4. System architecture \t 5. Calender \t 6. Date \t 7.Basic Calculator\n 8. Storage Usage \t 9.Hardware Information \t 10. Ping \t 11.Create File \t 12. Remove file \t 13.Read file \t  14. Make Directory ")
            list2=("15.Shutdown \t 16.Install Package \t 17.Uninstall Package \t 18.Show installed Packages \t 19.hardware clock \t 20.IP Configuration \t 21.Change Password \n 22.Wikipedia\(Get Quick Info\) \t 23.Youtube Downloader \t 24.Combile two Files \t 25.Different between two file \t 26.Dns Lookup \n 27.Get information about Websites \t 28.StopWatch \t 29.Mac address changer \t 30.Display Running Process \t 31.Create Simple Web server \n 32.Reboot System \t 33.Remove Directory \t 34.Change IP Address \t 35.Check RAM Usage \t 36.Compress File")
            prCyan("---------------------------------------------------------------------------------------------------")
            prYellow(list1)
            prYellow(list2)
            prGreen("\n[+] Enter a Value -- > ")
            #value= int(input())
            value = pyip.inputNum("", lessThan=50)

            prCyan("---------------------------------------------------------------------------------------------------")

            if value == 0:
                subprocess.call(["clear"])
                break
            elif value == 1:
                user = input("[+] Enter a user name you want to add -- > ")
                subprocess.call(["adduser", user])
            elif value == 2:
                subprocess.call(["apt", "update"])
            elif value == 3:
                try:
                    subprocess.call(["apt-get", "upgrade"])
                except:
                    prRed("[-] Upgrade Canceled...")
            elif value == 4:
                subprocess.call(["arch"])
            elif value == 5:
                year = int(input("Enter a year --> "))
                subprocess.call(["cal", str(year)])
            elif value == 6:
                subprocess.call(['date'])
            elif value == 7:
                def add(num1, num2):
                    return num1 + num2
                def subtract(num1, num2):
                    return num1 - num2
                def multiply(num1, num2):
                    return num1 * num2
                def divide(num1, num2):
                    return num1 / num2
                print("Please select operation -\n"
                      "1. Add\n"
                      "2. Subtract\n"
                      "3. Multiply\n"
                      "4. Divide\n")

                # Take input from the user
                select = int(input("Select operations form 1, 2, 3, 4 :"))

                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))

                if select == 1:
                    print(number_1, "+", number_2, "=",
                          add(number_1, number_2))

                elif select == 2:
                    print(number_1, "-", number_2, "=",
                          subtract(number_1, number_2))

                elif select == 3:
                    print(number_1, "*", number_2, "=",
                          multiply(number_1, number_2))

                elif select == 4:
                    print(number_1, "/", number_2, "=",
                          divide(number_1, number_2))
                else:
                    print("Invalid input")
            elif value == 8:
                subprocess.call(["df","-h"])
            elif value == 9:
                subprocess.call(["sudo","dmidecode","--type","system"])
            elif value == 10:
                try:
                    ip = input("Enter a Ip address --> ")
                    subprocess.call(["ping", ip])
                except:
                    prRed("[-] Abort.........")
            elif value == 11:
                file = input("[+] Enter a File Name (example.txt) --> ")
                #home = Path.home()
                os.chdir("/home/apple/Desktop/")
                prGreen("[+] File Sucesfully Created to the Home directory...")
                subprocess.call(["touch", file])
            elif value == 12:
                file = input("[+] Enter a File Name you want to remove --> ")
                #home = Path.home()
                os.chdir("/home/apple/Desktop/")
                subprocess.call(["rm", file])
            elif value == 13:
                file = input("[+] Enter a File Name you want to read --> ")
                #home = Path.home()
                os.chdir("/home/apple/Desktop/")
                subprocess.call(["cat", file])
            elif value == 14:
                file = input("[+] Enter a Directory Name --> ")
                #home = Path.home()
                os.chdir("/home/apple/Desktop/")
                subprocess.call(["mkdir", file])
            elif value == 15:
                print("1.Shutdown within minute\n 2.Shutdown Now ")
                option=int(input())
                if option == 1:
                    subprocess.call(["shutdown"])
                elif value == 2:
                    subprocess.call(["shutdon", "now"])
                else:
                    prRed("[-] Please enter a valid option")
            elif value == 16:
                package = input("Enter a package Name --> ")
                subprocess.call(["apt-get", "install", package])
            elif value == 17:
                uninstall = input("Enter a Package name to unintall --> ")
                subprocess.call(["dpkg", "--purge",uninstall])
            elif value == 18:
                subprocess.call(["dpkg", "--get-selections"])
            elif value == 19:
                subprocess.call(["hwclock"])
            elif value == 20 :
                subprocess.call(["ifconfig"])
            elif value ==21 :
                subprocess.call(["passwd"])
            elif value ==22 :
                wiki = input("Search Something: ")
                subprocess.call(["wikit", wiki])
            elif value == 23:
                link=input("Enter a Youtube link here -->")
                subprocess.call(["youtube-dl",link])
            elif value == 24:
                prCyan("Files must be in same folder")
                file1=input("Enter a file 1 name --> ")
                file2=input("Enter a file 2 name --> ")
                os.chdir("/home/apple/Desktop/")
                subprocess.call(["cat", file1 , file2])
            elif value == 25:
                file1 = input("Enter a file 1 name --> ")
                file2 = input("Enter a file 2 name --> ")
                os.chdir("/home/apple/Desktop/")
                subprocess.call(["diff", file1, file2])
            elif value ==26:
                domain=input("Enter a Domain name -- >")
                subprocess.call(["nslookup", domain])
            elif value ==27 :
                website=input("Enter a website name --> ")
                subprocess.call(["whois", website])
            elif value==28 :
                try:
                    second,minute,hours=0,0,0
                    while(True):
                        print(hours,":",minute,":",second)
                        time.sleep(1)
                        second+=1
                        if(second == 60):
                            second = 0
                            minute+=1
                        if(minute == 60):
                            minute=0
                            hours+=1
                except:
                    prRed("[-] Stopwatch stop")
            elif value == 29:
                network=input("Enter a Inferface --> ")
                mac=input("Enter a MAC Address -->")
                print(f"your changing mac address {mac} to the interface {network}")
                subprocess.call(["ifconfig", network, "down"])
                subprocess.call(["ifconfig", network, "hw", "ether", mac])
                subprocess.call(["ifconfig", network, "up"])
                subprocess.call(["ifconfig",network])
            elif value == 30:
                try:
                    subprocess.call(["top"])
                except:
                    prRed("[-] Exit")
            elif value == 31:
                try:
                    subprocess.call(["service", "apache2", "start"])
                    subprocess.call(["python", "-m", "SimpleHTTPServer"])
                except:
                    prRed("[-] Server Stopped")
            elif value == 32:
                prCyan("Are you sure you want to reboot system? yes/no")
                confirmatiom = input()
                confirmatiom.lower()
                if (confirmatiom == "yes"):
                    subprocess.call(["reboot"])
                else:
                    prRed("[-] Reboot Cancel")
            elif value == 33:
                file = input("[+] Enter a Directory you want to Remove --> ")
                home = Path.home()
                os.chdir(home)
                subprocess.call(["rmdir", file])
            elif value == 34:
                try:
                    interface = input("[+] Enter a Interface -->")
                    print()
                    subprocess.call(["ifconfig", interface])
                    print()
                    new_ip = input("[+} Enter a New IP Address -->")
                    subprocess.call(["ifconfig", interface, new_ip])
                    print()
                    subprocess.call(["ifconfig", interface])
            
                except:
                    prRed("[-] Please Enter a Valid IP Address.....")
            elif value == 35:
                subprocess.call(["free"])
            elif value == 36:
                os.chdir("/home/apple/Desktop/")
                compress = input("Enter a file/directory ---> ")
                zip_name = input("Enter a zip folder name with extension(example.tar.gz) -- >")
                subprocess.call(["tar", "-czvf", zip_name, compress])

            else:
                print("[-] Enter a Valid option")
    except:
        prRed("\n[-] Please enter a valid number")


options()