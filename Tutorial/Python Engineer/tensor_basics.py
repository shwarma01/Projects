import torch
import numpy as np

a = torch.ones(2, 2)
b = a.numpy()
a = a.to(device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu'))
a.add_(1)
print(a)
print(b)