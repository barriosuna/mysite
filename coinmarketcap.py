from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def prices():
	#import pandas as pd
	#Sera asi de facil?
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	parameters = {
	  'start':'1',
	  'limit':'2',
	  'convert':'USD'
	}
	headers = {
	  'Accepts': 'application/json',
	  'X-CMC_PRO_API_KEY': 'bbe314c7-4d97-4f88-9e55-d78b27df9f56',
	}

	session = Session()
	session.headers.update(headers)

	try:
	  response = session.get(url, params=parameters)
	  data = json.loads(response.text)

	  data = data['data']
	  data1 = data[0]
	  data2 = data[1]
	  #print(type(data1))
	  #print("asdadssadadsadsssss")
	  data1 = data1['quote']['USD']['price']
	  data2 = data2['quote']['USD']['price']
	  #print(data.keys())
	  return data1,data2
	  #df = pd.DataFrame.from_dict(data['data'])
	  #print(df.columns)
	  #print(df['quote'])
	except (ConnectionError, Timeout, TooManyRedirects) as e:
	  print(e)


