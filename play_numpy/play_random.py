import numpy as np

# low, high=None, size=None, dtype=int
# if high is none, the results are from 0 (inclusive) to low (exclusive)
foo = np.random.randint(10, size=6)
print(foo)