import datetime as dt
import random
import smtplib

my_gmail = 'zeruiy@gmail.com'
password = 'qljvpyxsycokpjft'

my_hmail = 'gabrieladealmeidajorge@hotmail.com'
# password = 'jzjffwhouknfillm'

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
lsta = ['saulogoncalvessantiago@gmail.com','felipenamoralgabriel1@gmail.com','marcospaulo2001@gmail.com','kimnari014@gmail.com','marianappcf@gmail.com','apoloantena@gmail.com']
if weekday == 6:
    with open('./quotes.txt', 'r') as quotes:
        lines = quotes.readlines()
        quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", port= 587,timeout=300) as connection:
    # connection =smtplib.SMTP("smtp.live.com", port=587)
        connection.starttls()
        connection.login(user=my_gmail,password=password)
        for _ in lsta:
            connection.sendmail(from_addr=my_gmail,to_addrs=_, msg=f'Subject: Ola, ja ouviu a palavra da frase motivacional hj? \n\n aaa\n teste aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n {quote}\n Te amo')
            # connection.close()




