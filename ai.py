import torch
from torch import nn

class NeuralNetwork():
    def __init__(self):
    	self.model = nn.Linear(2, 2)
    	self.loss_function = nn.MSELoss()
    	self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01)

    def update(self):
    	self.optimizer.step()
    	self.model.cleargrads()

