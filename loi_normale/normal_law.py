import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1 # mean and standard deviation

# The probability density function of the normal distribution
# it describes the commonly occurring distribution of samples influenced by a large number of tiny, random disturbances, each with its own unique distribution

# loc=0.0, scale=1.0, size=None)
s = np.random.normal(mu, sigma, 1000)

print(abs(mu - np.mean(s)) < 0.01)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()