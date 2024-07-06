
import random

user_score = 0
computer_score = 0

a = input("Are you ready to play?(Yes/No) ").title()
if a != "Yes":
    quit()

print("Great, Lets Start!")

alternatives = ["rock","paper","scissors"]

while True:
    User_Game = input("type rock/paper/scissors (press 'e' to exit): ")
    if User_Game == 'e':
        break

    elif User_Game not in alternatives:
        print("not a valid response!")
        continue

    random_number = random.randint(0, 2)
    computer_Game = alternatives[random_number]
    print(f"computer chose {computer_Game}.")

    if User_Game == "rock" and computer_Game == "scissors":
        print("you won")
        user_score += 1

    elif User_Game == "paper" and computer_Game == "rock":
        print("you won")
        user_score += 1

    elif User_Game == "scissors" and computer_Game == "paper":
        print("you won")
        user_score += 1

    elif User_Game == computer_Game:
        print("it's a tie!")

    else:
        print("you lost!")
        computer_score += 1

print(f"you won {user_score} times!")
print(f"I won {computer_score} times!")









