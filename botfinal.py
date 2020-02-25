
import requests
import pandas as pd
from coinmarketcap import prices

def precios(dolar_referencia,taker_fee):

        dolar_referencia = int(dolar_referencia)
        taker_fee = float(taker_fee)
        comisiones = 1 - (taker_fee+0.009+0.00075)

        price_btc, price_eth = prices()
        payload_btc = {'market': 'BTCARS', 'type': 'buy', 'page': 0}
        r_btc = requests.get("https://api.cryptomkt.com/v1/book", params=payload_btc).json()

        payload_eth = {'market': 'ETHARS', 'type': 'buy', 'page': 0}
        r_eth = requests.get("https://api.cryptomkt.com/v1/book", params=payload_eth).json()

        btc = pd.DataFrame.from_dict(r_btc['data']).drop(columns="timestamp")
        btc['amount'] = btc['amount'].astype(float)
        btc['amount'] = btc['amount'] * price_btc
        btc['price'] = btc['price'].astype(int)
        btc['Dolar'] = (btc['price'] / price_btc) * comisiones
        btc = btc[btc.Dolar > dolar_referencia]

        eth = pd.DataFrame.from_dict(r_eth['data']).drop(columns="timestamp")
        eth['amount'] = eth['amount'].astype(float)
        eth['amount'] = eth['amount'] * price_eth
        eth['price'] = eth['price'].astype(float)
        eth['Dolar'] = (eth['price'] / price_eth) * comisiones
        eth = eth[eth.Dolar>dolar_referencia]


        btc = btc.dropna()
        eth = eth.dropna()

        btc['amount'] = btc['amount'].cumsum()
        eth['amount'] = eth['amount'].cumsum()
        price_btc = round(price_btc)
        price_eth = round(price_eth)
        btc.columns = ['Monto BTC en USD', 'Precio','Dolar']
        eth.columns = ['Monto ETH en USD', 'Precio','Dolar']

        return btc, eth, price_btc, price_eth

