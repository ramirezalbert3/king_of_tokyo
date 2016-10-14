import random


def flipCoin(probability):
    n = random.random()
    if (n < probability):
        return True
    else:
        return False
