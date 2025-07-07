import numpy as np

# 1
print(np.shape([0]))

# 2
print(np.shape([1, 2]))

# 2, 2
print(np.shape([[1, 2], [3, 4]]))

# 3, 2
print(np.shape([[1, 2], [3, 4], [5, 6]]))

# 2 ?
print(np.shape([[1, 2], [3, 4, [5, 6]]]))

# 1, 1
print(np.shape([[0]]))

# 1, 1, 1
print(np.shape([[[0]]]))

# 1, 1, 2
print(np.shape([[[1, 2]]]))