import requests as rq

from twilio.rest import Client

account_sid = '<>'
auth_token = '<> '
client = Client(account_sid, auth_token)


response = rq.get("https://cat-fact.herokuapp.com/facts")
response.raise_for_status()
facts = response.json()
message = client.messages.create(
  from_='whatsapp:+yourtwilionumber',
  body=f"Did you know?\n{facts[0]['text']} \nThat's today's cat fact.\nSee you tomorrow bringing more facts!",
  to='whatsapp:+yournumber'
)
print(facts[0]["text"])
print(message.sid)
