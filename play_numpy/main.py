import numpy as np

a = np.zeros(3)
print(a)

z = np.ones(10)
print(z)

# Return evenly spaced numbers over a specified interval.
# start, stop , total
# 2, 4, 6, 8, 1O
q = np.linspace(2, 10, 5)

# 3, 6, 9
qz = np.linspace(3, 9, 3)
print(qz)

my_list = [1, 2, 3, 4, 5, 6, 7]
coucou = np.array(my_list)
print(type(coucou))