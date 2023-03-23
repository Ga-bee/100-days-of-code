##### Terminar e deixar mais bonitin
from word_list import words_list
from ascii_hangman import HANGMANPICS
import random
chosen_word = random.choice(words_list)

display =[]

for c in range(len(chosen_word)):
    display += '_'

lifes = 6

def hanged(life):
    print('')
    for i in range(life):
            print('''<3''', end ='')
    print(f'\n\nLifes: {lifes}')
    if life == 6:
        print(HANGMANPICS[0])
    if life == 5:
        print(HANGMANPICS[1])
    if life == 4:
        print(HANGMANPICS[2])
    if life == 3:
        print(HANGMANPICS[3])
    if life == 2:
        print(HANGMANPICS[4])
    if life == 1:
        print(HANGMANPICS[5])
    if life == 0:
        print(HANGMANPICS[6], '_' * 30)

print('''                                                                                           
▀████▀  ▀████▀▀     ██     ▀███▄   ▀███▀ ▄▄█▀▀▀█▄█▀████▄     ▄███▀     ██     ▀███▄   ▀███▀
  ██      ██       ▄██▄      ███▄    █ ▄██▀     ▀█  ████    ████      ▄██▄      ███▄    █  
  ██      ██      ▄█▀██▄     █ ███   █ ██▀       ▀  █ ██   ▄█ ██     ▄█▀██▄     █ ███   █  
  ██████████     ▄█  ▀██     █  ▀██▄ █ ██           █  ██  █▀ ██    ▄█  ▀██     █  ▀██▄ █  
  ██      ██     ████████    █   ▀██▄█ ██▄    ▀████ █  ██▄█▀  ██    ████████    █   ▀██▄█  
  ██      ██    █▀      ██   █     ███ ▀██▄     ██  █  ▀██▀   ██   █▀      ██   █     ███  
▄████▄  ▄████▄▄███▄   ▄████▄███▄    ██   ▀▀███████▄███▄ ▀▀  ▄████▄███▄   ▄████▄███▄    ██  
                                                                                           
                                                                                           
''')

while True:
    hanged(lifes)
    guess = input('Guess a letter:\n').lower()

    if guess not in chosen_word:
        lifes -= 1
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter


        if display[position] != '_':
            display[position] = display[position]
    answer = ''.join(display)        
    print(answer)
    if lifes == 0:
        print(''' ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
█  █ █  █       █  █ █  █  █   █   █       █       █       █       █
█  █▄█  █   ▄   █  █ █  █  █   █   █   ▄   █   ▄   █  ▄▄▄▄▄█    ▄▄▄█
█       █  █ █  █  █▄█  █  █   █   █  █ █  █  █ █  █ █▄▄▄▄▄█   █▄▄▄ 
█▄     ▄█  █▄█  █       █  █   █▄▄▄█  █▄█  █  █▄█  █▄▄▄▄▄  █    ▄▄▄█
  █   █ █       █       █  █       █       █       █▄▄▄▄▄█ █   █▄▄▄ 
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█
''')
        print(f'The word is: {chosen_word}!')
        break
    if len(display) > 0 and '_' not in display:
        print(''' ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄     ▄ ▄▄▄ ▄▄    ▄ 
█  █ █  █       █  █ █  █  █ █ ▄ █ █   █  █  █ █
█  █▄█  █   ▄   █  █ █  █  █ ██ ██ █   █   █▄█ █
█       █  █ █  █  █▄█  █  █       █   █       █
█▄     ▄█  █▄█  █       █  █       █   █  ▄    █
  █   █ █       █       █  █   ▄   █   █ █ █   █
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄▄▄█▄█  █▄▄█
''')
        print(f'The word is {chosen_word}')
        break

# while True: #len(display) != len(chosen_word):    
#     guess = input('Guess a letter:\n').lower()
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if guess == chosen_word[position]:
#             display[position] = letter
            
#         if guess!= chosen_word[position]:
#             display += '_'
        
#     if '-' not in display:
#         break

# print('')
# print(display)
# # while finished == 0:
#     guess = input('Guess a letter\n')

#     for c in range(len(choosen_word)):
#         if guess == choosen_word[c]:
#             word += guess
#             print(word, end='')
#         if guess!= choosen_word[c]:
#             print('_', end='')
    
#     print('')

# # print('')