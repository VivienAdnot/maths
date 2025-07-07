import scipy as sp
import matplotlib.pylab as plt

A = sp.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (A)

AT = sp.transpose(A)
print(AT)

foo = sp.matmul(A, AT)
print(foo)

t = sp.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()