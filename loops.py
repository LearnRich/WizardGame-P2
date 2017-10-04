# Loops!
# Allow us to repeat a set of instruction over and over until
# a condition is met.

# For loop is very good when you know how many times
# you want to repeat something.

for counter in range(10, 0, -1):
    print(counter)
print("Blast off!")

# While loop is very good if you don't know how many times
# you want to repeat something.
# Be careful with the condition not to create an
# infinite loop!
choice = "y"
while choice != "n" and choice != "no" and choice != "No" and choice != "N":
    print("This is the song that never ends!")
    choice = input("Would you like to continue?(y/n): ")

'''
Truth Table

  A  |  B  |  AND  |  OR  |  NOT(A)
-----------------------------------
  T  |  T  |   T   |  T   |   F
  T  |  F  |   F   |  T   |   F
  F  |  T  |   F   |  T   |   T
  F  |  F  |   F   |  F   |   T

'''

import random

random_num = random.randrange(1, 21)
guess = 0
while guess != random_num:
    guess = input("Enter the number I am thinking of: ")
    guess = int(guess)
    if guess == random_num:
        print("You Got It!\nWay to go!")
