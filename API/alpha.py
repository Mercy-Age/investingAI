import requests
import pandas as pd    

# we are using ALPHA VANTAGE API for more info: https://www.alphavantage.co/documentation/
# Get a key from https://www.alphavantage.co/support/#api-key
KEY = '3FYBS2OTSL5HGH17'
URL = 'https://www.alphavantage.co/query?'

def main():
	data = requests.get(URL + 'function=TIME_SERIES_DAILY&outputsize=full&symbol=VIX&apikey=' + KEY)
	data = data.json()
	print(data)
	df = pd.DataFrame(data['Time Series (Daily)'])
	print(df)

if __name__ == '__main__':
	main()