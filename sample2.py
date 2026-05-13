import torch

# Way 1 — from a Python list (most direct)
a = torch.tensor([1.0, 2.0, 3.0])
print(a)
# tensor([1., 2., 3.])

# Way 2 — all zeros  (used to initialise empty buffers)
b = torch.zeros(3, 4)     # 3 rows, 4 columns
print(b)
# tensor([[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]])

# Way 3 — all ones
c = torch.ones(2, 3)
print(c)
# tensor([[1., 1., 1.],
#         [1., 1., 1.]])

# Way 4 — random values from a normal distribution
#          (this is how neural network weights are initialised)
d = torch.randn(3, 3)
print(d)
# tensor([[ 0.3241, -0.1823,  0.5517],
#         [-1.2041,  0.8832, -0.0412],
#         [ 0.6753, -0.4921,  1.1023]])

# Way 5 — a range of numbers (like Python's range())
e = torch.arange(0, 10, 2)   # start, stop, step
print(e)
# tensor([0, 2, 4, 6, 8])
