print([1,2,3] * 3)


# import requests
# from datetime import datetime
# import smtplib
# import time

# lat = str(-22.878679)
# lng = str(-42.019878)


# MY_LAT = -22.878679 # Your latitude
# MY_LONG = -42.019878 # Your longitude

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# station = response.json()


# iss_latitude = float(station["iss_position"]["latitude"])
# iss_longitude = float(station["iss_position"]["longitude"])

# def check(data):
#     if iss_latitude > -27 and iss_latitude < -17:
#     # if float(data['iss_position']['latitude'])< -35.0 and float(data['iss_position']['latitude']) > -30.0:
#         if iss_longitude > -47 and iss_longitude < -37:
#         # if float(data['iss_position']['longitude']) > 78.0 and float(data['iss_position']['longitude']) < 85.0:
#             print('ja chegou o disco voador')
#             return True
#         return False
#     return False



# #Your position is within +5 or -5 degrees of the ISS position.


# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# time_now = datetime.now()
# hour = time_now.hour
# # print(hour, sunrise, sunset)

# count = 0
# while True:
#     count += 1
#     if check(station):
#         if hour > sunset or hour < sunrise:
#             with smtplib.SMTP('smtp.gmail.com', port=587, timeout=600) as connection:
#                 connection.starttls()
#                 connection.login(user='zeruiy@gmail.com', password='qljvpyxsycokpjft')
#                 connection.sendmail(from_addr='zeruiy@gmail.com', to_addrs='gabrieladealmeidajorge@hotmail.com',
#                                     msg=f'Subject: Look up!! \n\n The international station is above you, try to see it!')
#     print(count)

#     time.sleep(60)


# #If the ISS is close to my current position
# # and it is currently dark
# # Then send me an email to tell me to look up.
# # BONUS: run the code every 60 seconds.




