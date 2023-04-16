##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

lista = pd.read_csv('./birthdays.csv')

models = ['./letter_templates/letter_1.txt','./letter_templates/letter_2.txt','./letter_templates/letter_3.txt']
today =dt.datetime.now()

# print(lista)

def check():
    today_day = float(today.day)
    today_month = float(today.month)
    today_year = today.year
    for index,rows in lista.iterrows():
        if today_day == rows['day'] and today_month == rows['month']:
            name = rows['name']
            email = rows.email
            # print(name,email)
            letter = random.choice(models)
            with open(letter,'r') as file:
                reader = file.read()
                new_letter = reader.replace('[NAME]',name)
                
                with smtplib.SMTP('smtp.gmail.com',port= 587,timeout=600) as connection:
                    connection.starttls()
                    connection.login(user='zeruiy@gmail.com',password='qljvpyxsycokpjft')
                    connection.sendmail(from_addr='zeruiy@gmail.com', to_addrs=email,msg=f'Subject: Happy Birthday! \n\n {new_letter}')

                print(f'name: {rows.name}\nemail: {rows.email}')

check()


