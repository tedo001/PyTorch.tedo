import torch

x = torch.randn(4, 3, 64, 64)   # a batch of 4 dog images

print(x.shape)    # torch.Size([4, 3, 64, 64])
print(x.dtype)    # torch.float32
print(x.device)   # cpu
print(x.numel())  # 49152  ← total number of values inside

# Access shape like a tuple
print(x.shape[0])   # 4   ← batch size
print(x.shape[1])   # 3   ← colour channels (R, G, B)
print(x.shape[2])   # 64  ← height
print(x.shape[3])   # 64  ← width
