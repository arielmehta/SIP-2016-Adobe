import random

word_list = ["meera", "nature", "coding", "girls who code", "san francisco"]

random_number = random.randint(0, len(word_list)-1)

chosen_word= word_list[random_number]

def print_spaces_for_word ():
    print("*" * len(chosen_word))

print_spaces_for_word()

user_input= input("Choose a letter: ")

