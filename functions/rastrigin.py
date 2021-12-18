import numpy as np
class rastrigin:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        summa = (cells*cells - 10*np.cos(2*np.pi*cells) +10).sum()
        return summa
    def __str__(self) -> str:
        return "Rastrigin"