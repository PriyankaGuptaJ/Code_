
var_1 = input("are you ready? (Type yes/no) ").lower()

if var_1 != "yes":
    quit()

print("Great, Lets start! ")

adjective1 = input("enter an adjective: ")
place = input("a place: ")
animal = input("a animal: ")
emotion = input("an emotion: ")
emotion2 = input("another emotion: ")
object = input("an object: ")
character = input("your favourite superhero/movie character : ")
weather_condition = input("Name a weather condition: ")
place2 = input("another fav. place: ")
adverb = input("an adverb: ")


madlibs   =   f"In the {adjective1} land of {place}, a {animal} was feeling {emotion}. The {animal} had lost its {object}. Suddenly, a {character} appeared. 'I will help you find your {object},' they said. \
Together, they journeyed and faced the {weather_condition}. Finally, they found the {object} in a {place2}. The {animal} was so {emotion2} and thanked the {character}.They lived {adverb} ever after."


print(madlibs)

