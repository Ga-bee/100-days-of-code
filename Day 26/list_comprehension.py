numbers = [1,2,3]

new_list = [n+1 for n in numbers]

print(f'Adding a number list:\n{new_list}\n')

my_name = 'Gabee'

list_letter = [letter for letter in my_name]

print(f'List of letters in name:\n{list_letter}\n')

# doubled_list = [for item in range(1,5) item*2]
doubled_list = [item*2 for item in range(1,5) ]
print(f'Doubled list:\n{doubled_list}\n')

names = ['Ana', "Bia", "Clara", "Carlos","Gabriela", 'Jorge', "Marcos", "Davi", 'João',"Pedro"]
short_names = [name for name in names if len(name)<=4]
long_names = [name.upper() for name in names if len(name)>4]
print(f'Short names:\n{short_names}\n')
print(f'Long names:\n{long_names}\n')