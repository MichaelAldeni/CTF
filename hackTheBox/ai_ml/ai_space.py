import numpy as np
import matplotlib.pyplot as plt

data = np.load('ai_ml/ai_space/distance_matrix.npy')

print(f"Shape: {data.shape}")
print(f"Dtype: {data.dtype}")
print(f"Min: {data.min()}, Max: {data.max()}")
print(f"Sample:\n{data[:5]}")

# 2D scatter
plt.figure(figsize=(10, 6))
plt.scatter(data[:, 0], data[:, 1], s=1, c="red")
plt.axis("equal")
plt.show()