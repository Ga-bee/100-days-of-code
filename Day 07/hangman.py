import random
word_list = ['apple','pie','banana','word','piece','computer', 'run','dress','golf'] 
chosen_word = random.choice(word_list)

display =[]


while True: #len(display) != len(chosen_word):    
    guess = input('Guess a letter:\n').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == chosen_word[position]:
            display[position] = letter
            print(display)
        if guess!= chosen_word[position]:
            display += '_'
            print(display)
        
    if '-' not in display:
        break

print('')
print(display)
# while finished == 0:
#     guess = input('Guess a letter\n')

#     for c in range(len(choosen_word)):
#         if guess == choosen_word[c]:
#             word += guess
#             print(word, end='')
#         if guess!= choosen_word[c]:
#             print('_', end='')
    
#     print('')

# print('')
print(chosen_word)