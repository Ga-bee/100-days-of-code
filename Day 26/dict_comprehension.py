from random import randint

names = ['Ana', "Bia", "Clara", "Carlos","Gabriela", 'Jorge', "Marcos", "Davi", 'João',"Pedro"]

students_score = { student: randint(1,100) for student in names}

passed = {student: nota for student, nota in students_score.items() if nota >= 70}

print(f'Passed {passed}')
print(students_score)