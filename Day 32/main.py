import smtplib

my_gmail = 'zeruiy@gmail.com'
password = 'qljvpyxsycokpjft'

my_hmail = 'gabrieladealmeidajorge@hotmail.com'
# password = 'jzjffwhouknfillm'

with smtplib.SMTP("smtp.gmail.com", port= 587,timeout=300) as connection:
    # connection =smtplib.SMTP("smtp.live.com", port=587)

    connection.starttls()
    connection.login(user=my_gmail,password=password)
    connection.sendmail(from_addr=my_gmail,to_addrs=my_hmail, msg='Subject: Hello 3\n\n testing')
    connection.close()