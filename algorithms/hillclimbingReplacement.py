from solution import solution
import numpy as np


class hillclimbingReplacement:
    def __init__(self, dimension: int, maxIterations: int, bw: float):
        self.dimension = dimension
        #Efecto al tweak (r)
        self.bandwith = bw
        #Cantidad vecinos reinicio aleatorio
        self.neighbors = 100
        self.maxiterations = maxIterations

    def evolve(self,function):
        self.best = solution(self.dimension, function)
        self.function = function
        #Incluyendo inicion y excluyendo fin llena de 0 es decir [0,1...HastaMaximoIterations-1)
        x = np.arange(0, self.maxiterations)
        #Llena de 0 flotante hasta maxiterations
        y = np.zeros(self.maxiterations, float)
        #Inicio algoritmo para sacar un fitness
        self.best.randomInitialization()
        initialSolution = solution(self.best.size, self.best.function)
        initialSolution.from_solution(self.best)
        realiterations = int(self.maxiterations / self.neighbors)
        cont = 0
        #For para iterar las veces estipuladas
        for iteration in range(realiterations):
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
                # Asgina solucion a vecino
                y[cont] = self.best.fitness
                cont +=1
            initialSolution.from_solution(copyofbest)
            #Si la nueva solucion es menor que la anterior, remplazar
            if initialSolution.fitness < self.best.fitness:
                self.best.from_solution(initialSolution)
        #self.best.show()
        return [x, y]