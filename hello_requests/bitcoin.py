import requests 
from pprint import pprint 

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(coindesk_url)
data = response.json()
# pprint(data)

dollars_exchange_rate = data['bpi']['USD']['rate_float']
print(dollars_exchange_rate)

bitcoin = float(input('Enter the number of bitcoin: '))

bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate

print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars}')