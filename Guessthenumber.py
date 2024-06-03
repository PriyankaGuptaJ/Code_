

import random

correct = random.randint(1,70)


while True:
    guess = input("guess the number (b/w 1 & 70) ")
    if guess.isdigit():
        guess = int(guess)
        if guess>correct:
            print("too high")
        elif guess<correct:
            print("too low")
        else:
            print("Correct, You got it right!")
            break





