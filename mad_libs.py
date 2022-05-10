# mad libs
# I will export a random mab lib from a file and ask the user to input words for it.

# name = input("May I know your name please? ")
# verb_1 = input("a verb: ")
# adjective_1 = input("an adjective: ")
#
# sample_mad_lib = f"Hi {name}, you are here to {verb_1}. Do not give up for you are {adjective_1}."
# print(sample_mad_lib)

def get_user_input():
    noun_1 = input("a noun (animal): ")
    noun_2 = input("another noun (place/location): ")
    noun_3 = input("and another noun (food): ")
    noun_4 = input("and yet another noun (an animal, last one, I promise!): ")
    verb_1 = input("a verb (past tense): ")
    verb_2 = input("another verb: ")
    adjective_1 = input("an adjective: ")
    adjective_2 = input("another adjective: ")
    adjective_3 = input("another adjective: ")
    adjective_4 = input("and another adjective: ")

    print("\n and we are done. Enjoy your story.")

    user_inputs = {
        "noun_1": noun_1,
        "noun_2": noun_2,
        "noun_3": noun_3,
        "noun_4": noun_4,
        "verb_1": verb_1,
        "verb_2": verb_2,
        "adjective_1": adjective_1,
        "adjective_2": adjective_2,
        "adjective_3": adjective_3,
        "adjective_4": adjective_4,

    }
    return user_inputs


inputs = get_user_input()
# random_story = randint(1, 5)
random_story = 1

if random_story == 1:
    file = open("01_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()

print(mad_libs.format(**inputs))
