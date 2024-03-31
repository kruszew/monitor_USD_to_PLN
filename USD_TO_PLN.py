import requests
import time


def Get_Price(api_key):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=PLN&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    cena = data.get('Realtime Currency Exchange Rate', {}).get('5. Exchange Rate')
    return cena

api_key = 'Twoje API'
cena = Get_Price(api_key)
aktualna_cena = cena
print(f"aktualna cena: {aktualna_cena}")


while True:
    try:
        cena = Get_Price(api_key)
        if cena != aktualna_cena:
            aktualna_cena = cena
            print(f"nowa cena to: {aktualna_cena}")
        time.sleep(20)
    except Exception as e:
        print(f"blad: {e}")

#alphavantage ma limit do 25 requestów api na dzień przy darmowym pakiecie