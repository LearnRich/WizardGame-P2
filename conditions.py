# generic form of an if statment
# if condition statment:
#   Runs when conditional statement is true
#   These lines must be indented

# conditional statements are made up of
# a value that is compared using a
# conditional operator and evaluated
# to either true or false
# ==  equal
# !=  not equal to
# <   less than
# <=  less than or equal to
# >   greater than
# >=  greater or equal to


print(5 < 5)
print(5 <= 5)

running = True
while running:
    age = int(input("Please enter age: "))

    if age == 12:
        print("The average age of a grade 8")
        print("you must be a grade 8, or youthful grade 9")
    elif age == 13:
        print("GRAD 2021 YER!")
    elif age > 13 and age < 18:
        print("You are a senior student")
        if age > 16:
            print("Could be the final year!")
    elif age == 18 or age == 19:
        print("Last year grad came to visit")
    elif age == 36:
        print("G'Day Richardson.")
    else:
        print("That is pretty old... ")
        print("are you sure you are a high school student?")
    choice = input("Do you want to continue?: ")
    if choice == "n" or choice == "N" or choice == "no" or choice == "No":
        running = False


'''










elif check_var == 5:
    print("EQUAL!!")
elif check_var < 10:
    print("LESS THAN 10, GREATER THAN 5")

user_choice = input("What is your name: ")

if user_choice.lower() == "ben":
    print("Welcome", user_choice, " to the super system")
    if len(user_choice) > 8:
        print("Wow, you have a long name!")
else:
    print("Get out, you don't have permission!")

user_age = input("Please enter age")
if user_choice.lower() == "ben" and user_age == "36":
    print("Welcome", user_choice, " to the super system")
else:
    print("Get out, you don't have permission!")

username = input("Please enter username: ")
password = input("Please enter password: ")
if username == "Ben" or username == "ben":
    if password == "12345678r":
        print("Valid user! Welcome")
    else:
        print("Incorrect password :(")
else:
    print("Incorrect username :(")












'''
