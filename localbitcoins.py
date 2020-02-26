import requests
import pandas as pd

def local_arg(precio_btc, precio_eth):
	#probando again
	#cambio??
	precios_arg = requests.get("https://localbitcoins.com/buy-bitcoins-online/ars/national-bank-transfer/.json").json()
	precios_arg = precios_arg['data']['ad_list']
	precios_ves = requests.get("https://localbitcoins.com/sell-bitcoins-online/ves/transfers-with-specific-bank/.json").json()
	precios_ves = precios_ves['data']['ad_list']
	#print(precios_ves)
	info = []
	info1 = []
	#precios_arg =precios_arg[0]['data']
	#print(precios_arg.keys())
	for i in precios_arg:
		a = (i['data']['temp_price'],i['data']['max_amount'])
		info.append(a)

	for j in precios_ves:
		b = (j['data']['temp_price'],j['data']['max_amount'])
		info1.append(b)

	info1 = pd.DataFrame(info1)
	info1.columns = ['Precio','Maximo']

	info = pd.DataFrame(info)
	info.columns = ['Precio','Maximo']

	info['Dolar Implicito'] = info.Precio.astype(float) / precio_btc
	info1['Dolar Implicito'] = info1.Precio.astype(float) / precio_btc

	info1 = info1.head(5)
	info = info.head(5)
	info['Precio'] = info.Precio.astype(float)
	info1['Precio'] = info1.Precio.astype(float)
	arg_avg = info.Precio.mean()
	ves_avg = info1.Precio.mean()
	tasa = (ves_avg/arg_avg)*0.99
	tasa =round(tasa,1)
	info=info.values.tolist()
	info1=info1.values.tolist()
	return info,info1,tasa

#print(precios_arg.keys())

