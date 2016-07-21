adjective_1= ['sweet', 'sour', 'creamy', 'umami', 'soft', 'fluffy', 'warm', 'salty', 'thick', 'rich']
word_2= ['grilled', 'baked', 'panfried', 'stirfried', 'fried', 'tossed', 'microwaved', 'boiled', 'moist', 'tender']
main_food= ['chicken', 'vegetable mix', 'salad', 'shirmp', 'salmon', 'beef', 'steak', 'eggs', 'potatoes', 'venison']
number_list= ['1.', '2.','3.','4.','5.','6.','7.','8.','9.','10.']

import random

print("MENU: ")
for n in range(len(number_list)) :
    first= random.choice(adjective_1)
    second= random.choice(word_2)
    third= random.choice(main_food)
    food_stuff= [first, second, third]
    print(number_list[n] + " " + food_stuff[0] + " " + food_stuff[1] + " " + food_stuff[2])

articles= ['The']
adjectives= ['rolling', 'rocking', 'singing', 'harmonious', 'rapping', 'amazing']
nouns= ['divas', 'beings', 'girls', 'boys', 'people', 'eagles', 'hyenas', 'harmonizers']
number_list_2= ['1.', '2.','3.','4.','5.','6.','7.','8.','9.','10.']

print("   ")

print("BAND NAMES: ")
for n in range(len(number_list_2)) :
    first= random.choice(articles)
    second= random.choice(adjectives)
    third= random.choice(nouns)
    band_name= [first, second, third]
    print(number_list_2[n] + " " + band_name[0] + " " + band_name[1] + " " + band_name[2])



word_1 = "coding"
word_2 = "nature"
word_3 = "fremont"
word_4 = "Meera"
word_5 = "Girls Who Code Rocks"










    
    





