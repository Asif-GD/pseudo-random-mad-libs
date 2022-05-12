# mad libs
# I will export a random mab lib from a file and ask the user to input words for it.

from random import randint


def get_user_input():
    noun_1 = input("a noun (plural): ").upper()
    noun_2 = input("another noun (place/location): ").upper()
    noun_3 = input("and another noun (food): ").upper()
    noun_4 = input("and yet another noun (a proper noun): ").upper()
    noun_5 = input("and another noun (animal): ").upper()
    verb_1 = input("a verb (past tense): ").upper()
    verb_2 = input("another verb (past tense): ").upper()
    verb_3 = input("and another verb (ed!): ").upper()
    verb_4 = input("and another verb (-ing): ").upper()
    adjective_1 = input("an adjective (color): ").upper()
    adjective_2 = input("another adjective: ").upper()
    adjective_3 = input("another adjective (superlative): ").upper()
    adjective_4 = input("and another adjective: ").upper()

    print("...and we are done. I hope you enjoy your story. \n")

    user_inputs = {
        "noun_1": noun_1,
        "noun_2": noun_2,
        "noun_3": noun_3,
        "noun_4": noun_4,
        "noun_5": noun_5,
        "verb_1": verb_1,
        "verb_2": verb_2,
        "verb_3": verb_3,
        "verb_4": verb_4,
        "adjective_1": adjective_1,
        "adjective_2": adjective_2,
        "adjective_3": adjective_3,
        "adjective_4": adjective_4,

    }
    return user_inputs


random_story = randint(1, 3)

if random_story == 1:
    print(f"A Day At The Zoo!")
    file = open("01_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()
elif random_story == 2:
    print(f"A Day At The Amusement Park!")
    file = open("02_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()
elif random_story == 3:
    print(f"First Day At School.")
    file = open("03_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()

inputs = get_user_input()
print(mad_libs.format(**inputs))
