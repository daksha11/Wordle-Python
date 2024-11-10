import pandas as pd
import random
from nltk.corpus import wordnet

df = pd.read_csv('./5_letters.csv')
random_number = random.randint(0, len(df))
word = ""
for i in range(5):
    word = word + df.iloc[random_number][i]
word = word.upper()
word_array = list(word)
chances = 6

def is_valid_english_word(word):
    return bool(wordnet.synsets(word))

while (chances > 0):
    word_dict = {}
    for i in range(5):
        if (word_dict.get(word_array[i]) == None):
            word_dict.setdefault(word_array[i], 1)
        else:
            word_dict.update({word_array[i] : word_dict.get(word_array[i]) + 1})

    string = input("Enter a word: ").upper()
    
    if (len(string) != 5):
        print("Enter a 5 letter word.")
        print()
        continue
    elif (is_valid_english_word(string) != True):
        print("The word is not found in our dictionary, please enter another word.")
        print()
        continue

    print()
    string_array = list(string)
    print(string_array)

    check = []
    correct_count = 0
    for i in range(5):
        if (word_array[i] == string_array[i]):
            check.append('✔')
            correct_count = correct_count + 1
            word_dict.update({word_array[i] : word_dict.get(word_array[i]) - 1})
        else:
            check.append('X')

    for i in range(5):
        if (check[i] == 'X'):
            if (string_array[i] not in word_dict):
                check[i] = "X"
            else:
                count = word_dict.get(string_array[i]) - 1

                if (count < 0):
                    check[i] = "X"
                else:
                    check[i] = "O"
                    word_dict.update({string_array[i] : count})
    print(check)

    if (correct_count == 5):
        break

    chances = chances - 1
    print("Chances Remaining:", chances)
    print()

if(chances == 0):
    print(word)
    print("You Lose.")
else:
    print()
    print("You Win.")