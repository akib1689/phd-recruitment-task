import torch

print("PyTorch version:", torch.__version__)
print("Is MPS built?   ", torch.backends.mps.is_built())
print("Is MPS available?", torch.backends.mps.is_available())

# Try creating a tensor on MPS
if torch.backends.mps.is_available():
    x = torch.randn(3, 3).to("mps")
    print("✅ Tensor on MPS:", x.device)
else:
    print("❌ MPS not available. Check macOS version & PyTorch build.")