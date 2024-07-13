
Name = input("What's your name: ").title()
while Name.isdigit():
    print("Not a valid name")
    Name = input("Enter your name: ").title()

Age = input("Enter your age ")
if not Age.isdigit():
    quit()
else:
    play = input("Do you want to play the Adventure Game? (Yes/No) ").title()
    if play != "Yes":
        quit()
    else:
        print("Great, Let's play the exciting Game! ")

choice = input("It's raining today. Do you want to have pakoras and enjoy the rain, \
or do you want to study for your exam tomorrow? ('P' for pakoras or 'S' for Study:) ").upper()

if choice == 'P':
    print("Congratulations! You picked a picked a plate of pakoras over a pile of notes. I'm sure that \
decision will taste great on exam day!")
    print("Do you want to go outside and sit by the balcony while enjoying the \
rain and snacks? or do you want to watch Netflix with snacks?")
    choice = input("('G' for Go outside or 'N' for Netflix:) ").upper()

    if choice == "G":
        choice = input("Pick: Video Game ('V') or outing with friends ('O')? ").upper()

        if choice == 'V':
            print("oops! Bad choice! You are stuck home for the next five days with no wifi")
            print("Since there is no Wifi, hence 'Goodbye':")
            quit()

        elif choice == 'O':
            print("Wow, You just earned an icecream treat for you and your friends!")
            print("Enjoy!")
            print("SEE YA!")

        else:
            quit()

    elif choice == "N":
        print("oops, Sorry!")
        quit()


elif choice == 'S':
    print("Awesome!",end = " ")
    print("I applaud you!")
    print("What if told you, that you have caught the attention of a Genie?")
    print("Instead of you choosing three wishes, this genie has three \
choices ready for you.")
    print("Each choice would open a hidden door for you. \
That door could be a dream come true or a total disaster.")

    choice = input("Are you ready? (Yes/No) ").title()

    if choice == "Yes":
        print("The 1st wish is knowledge.")
        print("Choice A: Instantly master any skill or subject of your choice.")
        print("Choice B: Gain the ability to read 10 times faster and retain all information.")
        print("Choice C: Learn one new fact every day, but it's always something trivial.")
        choice = input("'A'/'B'/'C': ").upper()


        if choice == "C":
            print("Granted!",end = " ")
            print("Congratulations!You've won a 1-2 week getaway to the \
destination of your dreams at no cost!")
            print("Goodbye!")

        elif choice == "B":
            print("Granted!")
            print("Oops! You are stranded in a jungle for the next two days with no phone, food, or survival kit.")

        else:
            print("Bad choice! goodbye")
            quit()
    else:
        quit()

else:
    print("not valid!")
    quit()
