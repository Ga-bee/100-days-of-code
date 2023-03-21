from random import randint

computer = randint(0,2)
ascii_art = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', ''''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
print("What do you choose", end = ' ')
person = int(input("Type 0 for rock, 1 for paper, and 2 for scisor "))

print(f'You chose: \n{ascii_art[person]} \n\nComputer chose:\n {ascii_art[computer]}')

if  computer > person:
    if person == 0 and computer == 2:
        winner = 'Player'
    else:
        winner = 'Computer'
elif computer == person:
    print('Both')
else:
    winner = 'Player'

print(f'{winner} wins!')

    # rock = 0
    # paper = 1
    # scisor = 2

 # 1>0
 # 2>1
 # 0>2
   
