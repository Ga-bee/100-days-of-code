from art import logo, vs
from data import data
import random

person_a = random.choice(data)
person_b = random.choice(data)

score = 0

def checking(a,b,guess):
    if a['follower_count'] > b['follower_count']:
        if guess == 'b':
            print(f"You loose. {b['name']}, has {b['follower_count']} while, {a['name']}, has {a['follower_count']}")
            return False
        elif guess == 'a':
            print("correct")
            return True
    if a['follower_count'] < b['follower_count']:
        if guess == 'a':
            print(f"You loose. {b['name']}, has {b['follower_count']} while, {a['name']}, has {a['follower_count']}")
            return False
        elif guess == 'b':
            print("correct")
            return True
        
while True:
    print(logo)
    print("Who has the most followers?\n")
    print(f"Personality A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Personality B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

    guess = input("Select 'a' or 'b' ").lower()

    check = checking(person_a, person_b, guess)

    if check:
        score += 1
        
        if person_a['follower_count'] > person_b['follower_count']:
            
            person_b = random.choice(data) 


        elif person_a['follower_count'] < person_b['follower_count']:
               
            person_a = person_b
            person_b = random.choice(data)
        continue
    else:
        print(f"Your scor was {score}")
        break



