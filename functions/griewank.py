import numpy as np
class griewank:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        product = 1
        summa = (cells * cells).sum()
        for i in range(len(cells)):
            product = product * (np.cos(cells[i] / np.sqrt(i+1)))
        summa = summa/4000 - product + 1
        return summa
    def __str__(self) -> str:
        return "Griewank"