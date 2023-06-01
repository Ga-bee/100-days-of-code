import requests as rq
import datetime
from twilio.rest import Client
import time

account_sid = 'AC2c242e76c2071e86643dab69e967eb01'
auth_token = '64958d7b7c90be0b6999d1fc62dc65f5 '
client = Client(account_sid, auth_token)


#####versao print
def print():
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    hoje = datetime.datetime.today().date()
    ontem = hoje - datetime.timedelta(days=1)

    api_key= "V2CFUEJ89BK63Y5T"
    url_stock = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={api_key}"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey={api_key}"
    response = rq.get(url_stock)
    daily = response.json()
    fechamento_hoje=float(daily["Time Series (Daily)"][f"{ontem}"]["4. close"])
    fechamento_ontem=float(daily["Time Series (Daily)"][f"{ontem - datetime.timedelta(days=1)}"]["4. close"])
    porcentagem = ((fechamento_hoje-fechamento_ontem)/fechamento_ontem)*100
    print(fechamento_hoje)
    print(fechamento_ontem)
    print(porcentagem)


    if porcentagem > 0 :
            print(f"""TSLA: 🔺 {int(porcentagem)}%""")
    else:
            print(f"""TSLA: 🔻 {int(porcentagem)}%""")


    key_news = "f32b21531d144a9c8106fc6af7f46629"
    url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={hoje}&sortBy=popularity&apiKey={key_news}"
    url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={ontem}&sortBy=popularity&apiKey={key_news}"
    response = rq.get(url_news)
    news = response.json()

    first_new = {
        "Headline":news["articles"][0]["title"],
        "Brief":news["articles"][0]["description"]
                }

    second_new = {
        "Headline":news["articles"][1]["title"],
        "Brief":news["articles"][1]["description"]

    }

    third_new = {
        "Headline":news["articles"][2]["title"],
        "Brief":news["articles"][2]["description"]

    }

        
    if porcentagem >= 5:
               print(f"""Headline: {first_new['Headline']}\nBrief: {first_new['Brief']}\n\n""")
               print(f"""Headline: {second_new['Headline']}\nBrief: {second_new['Brief']}\n\n""")
               print(f"""Headline: {third_new['Headline']}\nBrief: {third_new['Brief']}\n\n""")
    return
        
#########versao wpp
def versao_wpp():
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    hoje = datetime.datetime.today().date()
    ontem = hoje - datetime.timedelta(days=1)

    api_key= "V2CFUEJ89BK63Y5T"
    url_stock = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={api_key}"
    response = rq.get(url_stock)
    daily = response.json()
    fechamento_hoje=float(daily["Time Series (Daily)"][f"{hoje}"]["4. close"])
    fechamento_ontem=float(daily["Time Series (Daily)"][f"{ontem}"]["4. close"])
    porcentagem = ((fechamento_hoje-fechamento_ontem)/fechamento_ontem)*100
    # print(fechamento_hoje)
    # print(fechamento_ontem)
    # print(porcentagem)
    # time.sleep(1)



    if porcentagem > 0 :
            message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""BOM DIA!\nTSLA: 🔺 {int(porcentagem)}%""",
            to='whatsapp:+5522988277221')
            time.sleep(1)
    else:
            message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""BOM DIA!\nTSLA: 🔻 {int(porcentagem)}%""",
            to='whatsapp:+5522988277221')
            time.sleep(1)


    key_news = "f32b21531d144a9c8106fc6af7f46629"
    url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={hoje}&sortBy=popularity&apiKey={key_news}"
    response = rq.get(url_news)
    news = response.json()



    first_new = {
        "Headline":news["articles"][0]["title"],
        "Brief":news["articles"][0]["description"]
                }

    second_new = {
        "Headline":news["articles"][1]["title"],
        "Brief":news["articles"][1]["description"]

    }

    third_new = {
        "Headline":news["articles"][2]["title"],
        "Brief":news["articles"][2]["description"]

    }

    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""Aqui estão algumas notícias relevantes para entender esse comportamento.\n\n
            "Headline: {first_new['Headline']}\nBrief: {first_new['Brief']}\n\n""",
            to='whatsapp:+5522988277221')
    
    time.sleep(1)

    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""Headline: {second_new['Headline']}\nBrief: {second_new['Brief']}\n\n""",
            to='whatsapp:+5522988277221')
    
    time.sleep(1)

    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"""Headline: {third_new['Headline']}\nBrief: {third_new['Brief']}\n\n""",
            to='whatsapp:+5522988277221')    

