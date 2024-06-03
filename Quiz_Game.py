
lets_Start = input("Are you Ready to play? ")

if lets_Start.title() != "Yes":
    print("oops!")
    quit()

print("That's the energy! ")
score = 0

question = input("What is the capital city of France? ")
if question.title() == "Paris":
    print("Correct Answer")
    score += 2
else:
    print("Incorrect Answer")


question = input("Who wrote the play 'Romeo and Juliet'? ")
if question.title() == "William Shakespeare":
    print("Correct Answer")
    score += 2
else:
    print("Incorrect Answer")


question = input("How many continents are there on Earth? ")
if question == 7 or "Seven.title()":
    print("Correct Answer")
    score += 2
else:
    print("Incorrect Answer")


question = input("What is the largest planet in our solar system? ")
if question.title() == "Jupiter":
    print("Correct Answer")
    score += 2
else:
    print("Incorrect Answer")


question = input("Who was the first President of the United States? ")
if question.title() == "George Washington":
    print("Correct Answer")
    score += 2
else:
    print("Incorrect Answer")


print("Your total score is", score, "out of",10,"!")