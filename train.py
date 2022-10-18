from API.yahoo import Api
import pandas as pd
import torch
from ai import NeuralNetwork

def main():
	# apple = Api("AAPL")
	# Open = apple.open("2018-09-29")
	# Grow = apple.grow("2018-09-20")
	# # by merging our data we remove all dates that only appere in one of them
	# df = pd.merge(Open, Grow, on='Date')
	# print(df)
	# Open = df['Open'].values
	# Grow = df['Grow'].values
	# torch_tensor = torch.tensor([Open,Grow])
	# print(torch_tensor)
	model = NeuralNetwork()
	# X = torch.rand(1)
	# print(X)
	# logits = model(X)

if __name__ == '__main__':
	main()