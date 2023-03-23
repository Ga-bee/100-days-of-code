import random
print('Welcome to the Pypassword Generator!')
letters_list = ['a','b', 'c','d','e','f','g','h','i','j','k','l','m','n', 'o', 'p', 'q','r', 's','t','u', 'v','w', 'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols_list = ['!','@','$','%','&','*','(',')']
numbers = int(input('How many numbers would you like in your password. \n'))
symbol = int(input('How many symbols would you like in your password. \n'))
letters = int(input('How many letters would you like in your password. \n'))
password = []

for letter in range(letters):
    random_letter = random.choice(letters_list)
    password.append(random_letter)
for sym in range(symbol):
    random_symbol = random.choice(symbols_list)
    password.append(random_symbol)
for number in range(numbers):
    n = str(random.randint(0,10))
    password.append(n)
random.shuffle(password)

list_to_string = ''.join(password)
print(f'Here is your password:', end='')
print(list_to_string)
# print(random.shuffle(password))