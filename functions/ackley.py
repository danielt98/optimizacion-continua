import numpy as np
class ackley:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        sum1 = 0.0
        sum2 = 0.0
        for i in cells:
            sum1 += i** 2.0
            sum2 += np.cos(2 * np.pi * i)
        n = float(len(cells))
        return -20.0 * np.exp(-0.2 * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + 20 + np.e