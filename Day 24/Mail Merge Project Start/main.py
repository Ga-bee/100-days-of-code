#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
dir = os.getcwd()
dirs  = os.listdir()
os.chdir(dir)

with open('./Input/Names/invited_names.txt', mode= 'r') as  name:
    names = name.readlines()
    print(names)


with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
    letters = letter.read()
    print(letters)
    for i in names:
        striped_name = i.strip()
        new_letter = letters.replace('[name]', striped_name)
        with open(f'./Output/ReadyToSend/letter_to_{striped_name}', mode= 'w') as send:
            send.write(new_letter)