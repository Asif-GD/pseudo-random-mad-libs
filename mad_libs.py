# mad libs
# I will export a random mab lib from a file and ask the user to input words for it.

# name = input("May I know your name please? ")
# verb_1 = input("a verb: ")
# adjective_1 = input("an adjective: ")
#
# sample_mad_lib = f"Hi {name}, you are here to {verb_1}. Do not give up for you are {adjective_1}."
# print(sample_mad_lib)

from random import randint


def get_user_input():
    noun_1 = input("a noun (plural): ")
    noun_2 = input("another noun (place/location): ")
    noun_3 = input("and another noun (food): ")
    noun_4 = input("and yet another noun (last one, I promise!): ")
    verb_1 = input("a verb (past tense): ")
    verb_2 = input("another verb (past tense): ")
    verb_3 = input("and another verb (ed!): ")
    adjective_1 = input("an adjective (color): ")
    adjective_2 = input("another adjective: ")
    adjective_3 = input("another adjective (superlative): ")
    adjective_4 = input("and another adjective: ")

    print("...and we are done. I hope you enjoy your story. \n")

    user_inputs = {
        "noun_1": noun_1,
        "noun_2": noun_2,
        "noun_3": noun_3,
        "noun_4": noun_4,
        "verb_1": verb_1,
        "verb_2": verb_2,
        "verb_3": verb_3,
        "adjective_1": adjective_1,
        "adjective_2": adjective_2,
        "adjective_3": adjective_3,
        "adjective_4": adjective_4,

    }
    return user_inputs


random_story = randint(1, 2)

if random_story == 1:
    print("A Day At The Zoo!")
    file = open("01_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()
elif random_story == 2:
    print("A Day At The Amusement Park!")
    file = open("02_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()

inputs = get_user_input()
print(mad_libs.format(**inputs))
