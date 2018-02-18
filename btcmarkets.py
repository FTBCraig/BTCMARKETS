# First Python application including Api support
# Going to try and pull AUD price of Bitcoin from BTC Market

import urllib.parse
import requests

# VAR

main_api = 'https://api.btcmarkets.net'
address = '/market/BTC/AUD/tick'
url = main_api + address
json_data = requests.get(url).json()
json_instrument = json_data['instrument']
json_price = json_data['lastPrice']


print('BtcMarkets')
print()
print('Pair: ' + json_instrument + "/AUD")
print('Price: ' + "$"+str(json_price))