
Welcome = input("Are you ready to guess the number? (type 'Yes' or 'No') ")

if Welcome.lower() != "yes":
    quit()

print("alright,let's play")

number = input("enter any +ve number ")

if not number.isdigit():
    print("not a valid number!")
    quit()
else:
    number = int(number)

import random

random_number = random.randint(0, number)

while True:
    Guess_number = input("Guess the number b/w 0 " + "and " + str(number) + " ")
    if Guess_number.isdigit():
        Guess_number = int(Guess_number)

        if Guess_number < random_number:
            print("too low")
        elif Guess_number > random_number:
            print("too high")
        else:
            print("Correct! You got it right:)")
            print("YAY!!!")
            break
    else:
        print("not a valid number","try next time!")

