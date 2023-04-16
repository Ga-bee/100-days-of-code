import requests
from datetime import datetime
# resonse =requests.get(url="http://api.open-notify.org/iss-now.json")
# resonse.raise_for_status()
# print(resonse.content)

# data = resonse.json()

# print(data['iss_position'])

lat = str(-22.878679)
lng = str(-42.019878)
endpoint = 'https://api.sunrise-sunset.org/json'+ '?'+'lat='+lat+'&'+'lng='+lng

parameters = {
    'lat':lat
        ,
    'lng':lng,
    'formatted':0
}

response = requests.get(endpoint,params=parameters)
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]

sunset = data['results']['sunset'].split('T')[1].split(':')[0]
timenow = datetime.now()
print(timenow.hour)
print(f'Sunrise: {sunrise}\nSunset: {sunset}')