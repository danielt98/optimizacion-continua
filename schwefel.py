class schwefel:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        #summa = (cells.sum()*cells.sum()).sum()
        summa = 0
        for i in range(0, len(cells)):
            suma = 0
            for j in range(0, i+1):
                suma = suma + cells[j]
            summa = suma * suma + summa
        return summa
