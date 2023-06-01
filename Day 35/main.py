import requests as rq
from time import sleep, time
import datetime
api_key = "417884a6bb8dcf2e552d399cad04f141"
lat = "-22.878679"
lon = "-42.019878"
appid = api_key

twilio ="Amavaitomarnocu+3fe"
call = f"https://api.openweathermap.org/data/2.8/onecall?lat={lat}&lon={lon}&appid={appid}"
funciona= "https://api.openweathermap.org/data/2.8/onecall?lat=-22.878679&lon=-42.019878&appid=417884a6bb8dcf2e552d399cad04f141"
response = rq.get(call)

response = response.json()
"https://api.openweathermap.org/data/3.0/onecall?lat=-22.878679&lon=-42.019878&appid=417884a6bb8dcf2e552d399cad04f141"
# students_score = { student: randint(1,100) for student in names}

# passed = {student: nota for student, nota in students_score.items() if nota >= 70}

# for hour in range(response["hourly"][0]["dt"]):
#     for weather in response["hourly"][0]["weather"][0]["main"]:
#         dic = {hour: weather}
# dic = {hour:weather for hour in response["hourly"][0]["dt"] for weather in  response["hourly"][0]["weather"][0]["main"]  }
# print( response["hourly"][0]["dt"], response["hourly"][0]["weather"][0]["main"] )
# # print(dic)

from twilio.rest import Client

account_sid = 'AC2c242e76c2071e86643dab69e967eb01'
auth_token = '64958d7b7c90be0b6999d1fc62dc65f5 '
client = Client(account_sid, auth_token)
sleep(1)
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=f'Fala gostosa!\n Oh vamo ver a previsão pras próximas 12 horas?\n',
  to='whatsapp:+5522988277221'
)
sleep(1)
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=f'Computando......\n',
  to='whatsapp:+5522988277221'
)
sleep(1)
weather_slice = response["hourly"][:12]
for hour_data in weather_slice:
    cond_code = hour_data["weather"][0]["id"]
    # print(hour_data["weather"][0]["dt"],hour_data["weather"][0]["main"], end= " ")
    sleep(2)
    if int(cond_code) < 700:
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'{datetime.datetime.fromtimestamp(hour_data["dt"]).time().isoformat()}: Vai chover! Leve Guarda chuva\n',
        to='whatsapp:+5522988277221')
        print(message.sid)
    else:
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'{datetime.datetime.fromtimestamp(hour_data["dt"]).time().isoformat()}:Não vai chover! Não precisa levar guarda chuva\n',
        to='whatsapp:+5522988277221')
        print(message.sid)

#         print('')
#     print(response["hourly"][0]["weather"][0]["id"])
# for i in range(len(response["hourly"])):
#     print(response["hourly"][i]["dt"], response["hourly"][i]["weather"][0]["id"],  response["hourly"][i]["weather"][0]["main"])
# if response["hourly"][0]["weather"][0]["id"] < 700:
#     print("bring an umbrella")
# vaichove = {hora:vai for hora in range(1,12) }
