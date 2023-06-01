import requests as rq

from twilio.rest import Client

account_sid = 'AC2c242e76c2071e86643dab69e967eb01'
auth_token = '64958d7b7c90be0b6999d1fc62dc65f5 '
client = Client(account_sid, auth_token)


response = rq.get("https://cat-fact.herokuapp.com/facts")
response.raise_for_status()
facts = response.json()
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=f"Did you know?\n{facts[0]['text']} \nThat's today's cat fact.\nSee you tomorrow bringing more facts!",
  to='whatsapp:+5522999440175'
)
print(facts[0]["text"])
print(message.sid)
