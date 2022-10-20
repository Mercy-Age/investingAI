from API.yahoo import Api
import pandas as pd
import torch
from ai import NeuralNetwork

def main():
	apple = Api("AAPL")
	Open = apple.open("2018-09-29")
	Grow = apple.grow("2018-09-20")
	Close = apple.close("2018-09-20")
	# by merging our data we remove all dates that only appere in one of them
	df = pd.merge(Open, Grow, on='Date')
	df = pd.merge(df, Close, on='Date')
	Close = df['Close'].values
	Open = df['Open'].values
	Grow = df['Grow'].values
	Grow = Grow*1
	x = torch.stack((torch.from_numpy(Open), torch.from_numpy(Close)), -1).float()
	y = torch.from_numpy(Grow).float().reshape(-1, 1)
	print(x, y)
	# torch_tensor = torch.tensor([Open,Grow])
	# print(torch_tensor)
	AI = NeuralNetwork()
	for i in range(100):
		y_predicted = AI.model(x)
		loss = AI.loss_function(y_predicted, y)
		
		loss.backward()
		AI.update()


if __name__ == '__main__':
	main()