import numpy as np


class step:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        #Funcion piso
        newcells = np.floor(cells+0.5)
        #Eleva al 2 y suma cada celda
        summa = ( newcells * newcells).sum()
        return summa
