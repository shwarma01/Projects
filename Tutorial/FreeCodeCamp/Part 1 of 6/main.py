import torch
import numpy as np

x = torch.tensor(3.)
w = torch.tensor(4., requires_grad = True)
b = torch.tensor(5., requires_grad = True)

y = w*x + b
print(y)

# We can compute the derivative of y w.r.t the tensors that have requires_grad set to True
# This would be tensor w and tensor b
y.backward() # Computing the derivates

print(f"dy/dx: {x.grad}")
print(f"dy/dw: {w.grad}")
print(f"dy/db: {b.grad}")


# target1 = w1*x + w2*y + w3*z + b1
# target2 = v1*x + v2*y + v3*z + b2

inputs = np.array([[73, 67, 43],
                  [91, 88, 64],
                  [87, 134, 58],
                  [102, 43, 37],
                  [69, 96, 70]], dtype = "float32")

targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]], dtype="float32")

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# torch.randn creates a tensor with mean 0 and st deviation 1
w = torch.randn(2, 3, requires_grad=True)
b = torch.randn(2, requires_grad=True)

def model(x):
  return torch.matmul(x, w.t()) + b
  # w.T transposes the matrix but not inplace
  # w.t() transposes the matrix and changes it

preds = model(inputs)
print(preds)

# MSE loss - mean squared error
def mse(t1, t2):
  diff = t1 - t2
  return torch.sum(diff * diff) / diff.numel()
  # diff is the difference element-wise
  # .numel() is the number of elements
  # diff*diff makes all the difference values positive

loss = mse(preds, targets)
print(loss)

loss.backward()
print(w.grad)

w.grad.zero_()
b.grad.zero_()

# Adjusting weights and biases using gradient descent
preds = model(inputs)
loss = mse(preds, targets)
print(loss)
loss.backward()
with torch.no_grad():
  w -= w.grad * 1e-5
  b -= b.grad * 1e-5
  w.grad.zero_()
  b.grad.zero_()

preds = model(inputs)
loss = mse(preds, targets)
print(loss)

for i in range(100):
  preds = model(inputs)
  loss = mse(preds, targets)
  loss.backward()
  with torch.no_grad():
    w -= w.grad * 1e-5
    b -= b.grad * 1e-5
    w.grad.zero_()
    b.grad.zero_()

preds = model(inputs)
loss = mse(preds, targets)
print(loss)


import torch.nn as nn

inputs = np.array([[[73, 67, 43],
                  [91, 88, 64],
                  [87, 134, 58],
                  [102, 43, 37],
                  [69, 96, 70]], 
                  [[73, 67, 43],
                  [91, 88, 64],
                  [87, 134, 58],
                  [102, 43, 37],
                  [69, 96, 70]],
                  [[73, 67, 43],
                  [91, 88, 64],
                  [87, 134, 58],
                  [102, 43, 37],
                  [69, 96, 70]]], dtype = "float32")

targets = np.array([[[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]],
                    [[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]],
                    [[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]]], dtype="float32")

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

from torch.utils.data import TensorDataset

train_ds = TensorDataset(inputs, targets)

from torch.utils.data import DataLoader

batch_size = 5
train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

for xb, yb in train_dl:
  print("Batch:")
  print(xb)
  print(yb)

model = nn.Linear(3, 2) # (inputs, outputs)
print(model(inputs))

import torch.nn.functional as F

loss_fn = F.mse_loss
loss = loss_fn(model(inputs), targets)
print(loss)

opt = torch.optim.SGD(model.parameters(), lr = 1e-5)

def fit(num_epochs, model, loss_fn, opt, train_dl):
  for epoch in range(num_epochs):
    for xb, yb in train_dl:
      pred = model(xb)
      loss = loss_fn(pred, yb)
      opt.zero_grad()
      loss.backward()
      opt.step()
  
    if (epoch + 1) % 10 == 0:
      print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")
    
fit(100, model, loss_fn, opt, train_dl)
