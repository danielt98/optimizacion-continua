from solution import solution
import numpy as np


class hillclimbingReplacement:
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
            copyofbest = solution(self.best.size, self.best.function)
            copyofbest.from_solution(self.best)
            copyofbest.tweak(self.bandwith)
            for iNeig in range(self.neighbors):
                #Nueva posible solucion
                copyTweak = solution(self.best.size, self.best.function)
                #Asignar paramentros a la copia
                copyTweak.from_solution(self.best)
                #Ajuste
                copyTweak.tweak(self.bandwith)
                # Si la nueva solucion es menor que la anterior, remplazar
                if copyTweak.fitness < copyofbest.fitness:
                    copyofbest.from_solution(copyTweak)
            initialSolution.from_solution(copyofbest)
            #Si la nueva solucion es menor que la anterior, remplazar
            if initialSolution.fitness < self.best.fitness:
                self.best.from_solution(initialSolution)
            # Asgina solucion a vecino
            y[iteration] = self.best.fitness
        self.best.show()
        return [x, y]