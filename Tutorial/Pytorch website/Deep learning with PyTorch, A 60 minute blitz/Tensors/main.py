import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data) # datatype inferred

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data) # shape and datatype not changed
print(f"Ones tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype = torch.float) # overrides datatype
print(f"Random tensor: \n {x_rand} \n")

shape = (2, 3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeroes_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeroes_tensor} \n")

tensor = torch.rand(3, 4)

print(f"Shape: {tensor.shape}")
print(f"Datatype: {tensor.dtype}")
print(f"Device: {tensor.device}")

if torch.cuda.is_available:
  tensor = tensor.to("cuda")

print(f"Device: {tensor.device} \n")

tensor = torch.ones(4, 4)
tensor[:,1] = 0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim = 1)
print(t1)

print(f"tensor.mul(tensor): \n {tensor.mul(tensor)} \n") # Element-wise multiplication
print(f"tensor.matmul(tensor.T): \n {tensor.matmul(tensor.T)} \n") # Matrix multiplication

# Operations that have a _ suffix are in-place
print(f"{tensor} \n")
print(f"{tensor.add_(5)} \n")

# Tensors on the cpu and numpy arrays can share memory locations
t = torch.ones(5)
n = t.numpy()
print(t, n)

t.add_(1)
print(t, n)