from solution import solution
import numpy as np


class hillclimbingRandom:
    def __init__(self, function, dimension: int, maxIterations: int, bw: float,neighbors: int):
        self.best = solution(dimension, function)
        self.function = function
        self.maxiterations = maxIterations
        #Efecto al tweak (r)
        self.bandwith = bw
        #Cantidad vecinos reinicio aleatorio
        self.neighbors = neighbors

    def evolve(self):
        #Incluyendo inicion y excluyendo fin llena de 0 es decir [0,1...HastaMaximoIterations-1)
        x = np.arange(0, self.maxiterations)
        #Llena de 0 flotante hasta maxiterations
        y = np.zeros(self.maxiterations, float)
        #Inicio algoritmo para sacar un fitness
        self.best.randomInitialization()
        initialSolution = solution(self.best.size, self.best.function)
        initialSolution.from_solution(self.best)
        #For para iterar las veces estipuladas
        for iteration in range(self.maxiterations):
            for iNeig in range(self.neighbors):
                #Nueva posible solucion
                copyofbest = solution(self.best.size, self.best.function)
                #Asignar paramentros a la copia
                copyofbest.from_solution(self.best)
                #Ajuste
                copyofbest.tweak(self.bandwith)
                # Si la nueva solucion es menor que la anterior, remplazar
                if copyofbest.fitness < initialSolution.fitness:
                    initialSolution.from_solution(copyofbest)
            #Si la nueva solucion es menor que la anterior, remplazar
            if initialSolution.fitness < self.best.fitness:
                self.best.from_solution(initialSolution)
            initialSolution.randomInitialization()
            # Asgina solucion a vecino
            y[iteration] = self.best.fitness
        self.best.show()
        return [x, y]
