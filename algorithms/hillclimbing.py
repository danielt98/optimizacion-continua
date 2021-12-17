from solution import solution
import numpy as np


class hillclimbing:
    def __init__(self, function, dimension: int, maxIterations: int, bw: float):
        self.best = solution(dimension, function)
        self.function = function
        self.maxiterations = maxIterations
        #Efecto al tweak (r)
        self.bandwith = bw

    def evolve(self):
        #Incluyendo inicion y excluyendo fin llena de 0 es decir [0,1...HastaMaximoIterations-1)
        x = np.arange(0, self.maxiterations)
        #Llena de 0 flotante hasta maxiterations
        y = np.zeros(self.maxiterations, float)
        #Inicio algoritmo para sacar un fitness
        self.best.randomInitialization()
        #For para iterar las veces estipuladas
        for iteration in range(self.maxiterations):
            #Nueva posible solucion
            copyofbest = solution(self.best.size, self.best.function)
            #Asignar paramentros a la copia
            copyofbest.from_solution(self.best)
            #Ajuste
            copyofbest.tweak(self.bandwith)
            #Si la nueva solucion es menor que la anterior, remplazar
            if copyofbest.fitness < self.best.fitness:
                self.best.from_solution(copyofbest)
            #Asgina solucion a vecino
            y[iteration] = self.best.fitness
        self.best.show()
        return [x, y]
