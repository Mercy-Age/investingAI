import yfinance as yf

class Api:
	def __init__(self, symbol):
		self.symbol = symbol
		self.ticker = yf.Ticker(symbol)

	def open(self, start):
		df = self.ticker.history(start=start)
		df = df.drop(['Volume','Close','Low','High','Dividends', 'Stock Splits'], axis=1)
		return df

	def grow(self, start):
		df = self.ticker.history(start=start)
		df['Grow'] = df['Open'] < df['Close']
		df = df.drop(['Volume','Open' ,'Close', 'Low','High','Dividends', 'Stock Splits'], axis=1)
		return df

def main():
	apple = Api("AAPL")
	print(apple.open("2018-09-29"))
	print(apple.grow("2018-09-29"))

if __name__ == '__main__':
	main()