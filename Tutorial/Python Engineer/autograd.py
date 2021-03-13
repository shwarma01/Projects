import torch

x = torch.randn(3, device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu'), requires_grad = True)
print(x)

y = x + 2 # Because x requires grad y will have a grad_fn attribute of AddBackward
print(y) 
z = y*y*2
z = z.mean()
print(z) # Will contain a grad_fn of MeanBackward

z.backward() # z.mean() makes z a scalar value so no need to give any arguements in backward()
# if z was not a scalar value then we need to pass a vector to the backward() of size n x 1
# n = no. of rows in z
print(x.grad)

"""
x.requires_grad_(False)
x.detach()
with torch.no_grad()

^ 3 ways to get rid of the requires_grad attribute
If you don't do this then each backward() call will accumulate and result in the wrong gradients
"""