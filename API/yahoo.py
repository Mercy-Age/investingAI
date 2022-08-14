import yfinance as yf

def main():
	apple = yf.Ticker("AAPL")
	print(apple.history(period="max"))

if __name__ == '__main__':
	main()