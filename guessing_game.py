#!bin/usr/env python
import random

print("What is your name?")
name = input()
print("Hey! " + name + ", Guess a number 1 to 20")
random_numbers = random.randint(1, 20)

for guessing_number in range(1, 7):
    guess = int(input())
    if guess < random_numbers:
        print("its too low")
    elif guess > random_numbers:
        print("its to high")
    else:
        break
if random_numbers == guess:
    print("Yes you got it, my guessing number is " + str(random_numbers))
else:
    print("Try again, my gussing number is " + str(random_numbers))