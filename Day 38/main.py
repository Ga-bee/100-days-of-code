import requests as rq
import datetime as dt
from requests.auth import HTTPBasicAuth
import os


#já setei as variaveis mas fica dizendo que n tem nada

USERNAME = os.environ["USER"]
api_id = os.environ["APIID"] 
api_key = os.environ["APIKEY"] 
PASSWORD = os.environ["PASS"]
TOKEN = os.environ['TOKEN']

exercise = str(input("Tell me wich exercises you did:\n"))


hoje = dt.datetime.today().date()
hoje_f = hoje.strftime('%d/%m/%Y')
print(hoje_f)

agora = dt.datetime.now().time()
agora_f = agora.strftime("%H:%M:%S")
print(agora_f)


# api_id = "76620e5b"
# api_key = "a34d0e8a7ad697b149c2697e04432d34"


headers = {
    "x-app-id":api_id,
    "x-app-key":api_key
}

param = {
 "query":f"{exercise}",
 "gender":"female",
 "weight_kg":65.7,
 "height_cm":170.64,
 "age":22
}

url_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"

response_nutri = rq.post(url=url_exercise,headers=headers, json=param)
workouts = response_nutri.json()
print(workouts)
sheety_url = os.environ["SHEETY_ENDPOINT"]

basic = HTTPBasicAuth(f'{USERNAME}',f'{PASSWORD}')
# basic = HTTPBasicAuth('gabee','Olha1chao')
# sheety_url = "https://api.sheety.co/52ee36bab0b3226e253c1f8cf7940097/workouts/workouts"
# sheety_header = {
# "Authorization": "Basic Z2FiZWU6T2xoYTFjaGFv"}

sheety_header = {
"Authorization": TOKEN}

for exercises in range(0,len(workouts['exercises'])):
    body = {
        "workout": {
        "date" : f"{hoje_f}",
        "time": f"{agora_f}",
        "exercise": f"{workouts['exercises'][exercises]['user_input']}",
        "duration":f"{workouts['exercises'][exercises]['duration_min']}",
        "calories": f"{workouts['exercises'][exercises]['nf_calories']}"
    }
    }
    response_sheety = rq.post(url=sheety_url, json=body, auth=basic, headers=sheety_header)
    response_sheety.raise_for_status()
    print(response_sheety.text)

