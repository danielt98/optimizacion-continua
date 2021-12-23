from solution import solution
import numpy as np


class HcModifide:
    def __init__(self, dimension: int, maxIterations: int, bw: float,step:float,probabilityGauss:int,):
        self.dimension = dimension
        self.maxiterations = maxIterations
        #Efecto al tweak (r)
        self.bandwith = bw
        self.step = step
        self.probabilityGauss = probabilityGauss


    def evolve(self,function):
        self.best = solution(self.dimension, function)
        self.function = function
        #Incluyendo inicion y excluyendo fin llena de 0 es decir [0,1...HastaMaximoIterations-1)
        x = np.arange(0, self.maxiterations)
        #Llena de 0 flotante hasta maxiterations
        y = np.zeros(self.maxiterations, float)
        #Inicio algoritmo para sacar un fitness
        self.best.randomInitializationVariaton(self.step)
        #For para iterar las veces estipuladas
        for iteration in range(self.maxiterations):
            #Nueva posible solucion
            copyofbest = solution(self.best.size, self.best.function)
            #Asignar paramentros a la copia
            copyofbest.from_solution(self.best)
            #Ajuste
            copyofbest.tweakVariation(self.bandwith,self.probabilityGauss)
            #Si la nueva solucion es menor que la anterior, remplazar
            if copyofbest.fitness < self.best.fitness:
                self.best.from_solution(copyofbest)
            #Asgina solucion a vecino
            y[iteration] = self.best.fitness
        return [x, y]

    def __str__(self) -> str:
        return "HC-Modificado"
