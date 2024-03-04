import word_list
import random
print("Welcome to the Band Name Generator.")
# accepts the city where the user grew up in.
city_name = list(input("What's the name of the city you grew up in?\n"))
# accepts what the users pet name is .
pet_name = input("What's your pet's name?\n")

def namer(name):
    name = name[0]
    word = word_list.word_dict[name][random.randint(0,25)]
    return word

band_name = f"Your band name should be '{namer(city_name)} {namer(pet_name)}'"

print(band_name)