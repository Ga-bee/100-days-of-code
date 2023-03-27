import random

def menu():
    print('''_____   __                 ______                                                   _____                                                   
___  | / /___  ________ ______  /______________   _______ ____  _______________________(_)_____________ _   _______ ______ _______ ________ 
__   |/ /_  / / /_  __ `__ \_  __ \  _ \_  ___/   __  __ `/  / / /  _ \_  ___/_  ___/_  /__  __ \_  __ `/   __  __ `/  __ `/_  __ `__ \  _ \
_  /|  / / /_/ /_  / / / / /  /_/ /  __/  /       _  /_/ // /_/ //  __/(__  )_(__  )_  / _  / / /  /_/ /    _  /_/ // /_/ /_  / / / / /  __/
/_/ |_/  \__,_/ /_/ /_/ /_//_.___/\___//_/        _\__, / \__,_/ \___//____/ /____/ /_/  /_/ /_/_\__, /     _\__, / \__,_/ /_/ /_/ /_/\___/ 
                                                  /____/                                        /____/      /____/                          ''')
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return level
computers_choice = random.randint(0,101)
level = menu()
if level == 'hard':
        lifes = 5
        
elif level == 'easy':
    lifes = 10
while True:

    guess = int(input("Guess the number I'm thiking of: "))

    if guess == computers_choice:
        print(f"You win! The number is {computers_choice}")
        break

    if guess > computers_choice:
        lifes -=1
        if lifes == 0:
            print(f"You loose. The number is {computers_choice}")
            break
        print(f'{guess} is too high, you now have {lifes} chances')
        continue

    if guess < computers_choice:
        lifes -=1
        if lifes == 0:
            print(f"You loose. The number is {computers_choice}")
            break
        print(f'{guess} is too low, you now have {lifes} chances')
        continue
