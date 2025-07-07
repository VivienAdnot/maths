# import of libraries
import random
import matplotlib.pyplot as plt

# instanciation of needed objects
rnd = random.Random()

# declaration of  backtest
def backtest(capital, successRate, gain, loss, spread, numberFlips):
    resultat = []
    trade = 0
    startupCapital = capital
    failureRate = 100 - successRate
    i = numberFlips

    while i > 0 and capital > 0:
        trade = rnd.choices([gain, loss], weights=(successRate, failureRate))
        capital = capital + trade[0] - spread
        resultat.append(capital)
        if capital <= 0:
            break
        i-=1

    plt.figure(figsize=(12,5))
    plt.axhline(startupCapital, color="gray")
    plt.plot(resultat)
    plt.show()
    plt.close()


# Example of backtest function calling
backtest(10000, 55, 28, -25, 1, 1000)
