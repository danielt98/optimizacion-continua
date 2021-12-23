import numpy as np
class schwefel:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        #summa = (cells.sum()*cells.sum()).sum()
        return np.sum([np.sum(cells[:i]) ** 2
                       for i in range(len(cells))])
        return summa
    def __str__(self) -> str:
        return "Schwefel"
