import numpy as np
class griewank:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        product = 1
        count= 1
        for i in cells:
            product = product * (np.cos(i/np.sqrt(count)) +1)
            count+= 1
        summa = (cells * cells).sum()
        summa = 1/4000 * summa - product
        return summa