#EX01 squared numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [num**2 for num in numbers]


#Write your code 👆 above:

print(squared_numbers)



#EX02 even numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number%2 ==0]

#Write your code 👆 above:

print(result)

#EX03 SLA PARCEIRO

with open('file1.txt') as file1:
    file1 = file1.readlines()

with open('file2.txt') as file2:
    file2 = file2.readlines()
# file1 = open('file1.txt')
# file2 = open('file2.txt')

combined = file1 + file2

result = [int(num) for num in file1 if num in file2 ]

# Write your code above 👆

print(result)
