# mad libs
# I will export a random mab lib from a file and ask the user to input words for it.

# name = input("May I know your name please? ")
# verb_1 = input("a verb: ")
# adjective_1 = input("an adjective: ")
#
# sample_mad_lib = f"Hi {name}, you are here to {verb_1}. Do not give up for you are {adjective_1}."
# print(sample_mad_lib)

# random_story = randint(1, 5)

random_story = 1

adjective_1 = input("an adjective: ")
noun_1 = input("a noun (animal): ")
verb_1 = input("a verb (past tense): ")
adverb_1 = input("an adverb: ")
adjective_2 = input("an adjective: ")
noun_2 = input("a noun (place/location): ")
noun_3 = input("a noun (food): ")
noun_4 = input("a noun (animal): ")
adjective_3 = input("an adjective: ")
verb_2 = input("a verb: ")
adverb_2 = input("an adverb: ")
verb_3 = input("a verb (past tense): ")
adjective_4 = input("an adjective: ")

user_inputs = {
    "adjective_1": adjective_1,
    "noun_1": noun_1,
    "verb_1": verb_1,
    "adverb_1": adverb_1,
    "adjective_2": adjective_2,
    "noun_2": noun_2,
    "noun_3": noun_3,
    "noun_4": noun_4,
    "adjective_3": adjective_3,
    "verb_2": verb_2,
    "adverb_2": adverb_2,
    "verb_3": verb_3,
    "adjective_4": adjective_4,
}

if random_story == 1:
    file = open("01_mad_libs.txt", "r")
    mad_libs = file.read()
    file.close()

print(mad_libs.format(**user_inputs))
