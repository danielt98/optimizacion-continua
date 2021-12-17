import numpy as np
import solution as solution


class solution:
    def __init__(self, dimension: int, function):
        self.size = dimension
        #Llenar el vector de 0
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = function
        self.changes = self.cells

    def from_solution(self, origin:solution):
        #Asignar tamaño solucion inicial
        self.size = origin.size
        #Copia dimenciones iniciales
        self.cells = np.copy(origin.cells)
        #Asignar original fitness
        self.fitness = origin.fitness
        #original function
        self.function = origin.function
        self.changes= origin.changes

    def randomInitialization(self):
        #Numeros aleatorios en las dimenciones | Vector solucion
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,size=(self.size,))
        #Evalua en la funcion y regresa el valor a fitness
        self.fitness = self.function.evaluate(self.cells)

    def randomInitializationVariaton(self,step, nchanges):
        #Numeros aleatorios en las dimenciones que tenga un step de separación
        self.cells= np.random.choice(np.arange(self.function.lowerbound, self.function.upperbound, step), self.size, replace=False)
        self.changes = np.random.choice(len(self.cells), nchanges, replace=False)
        #Evalua en la funcion y regresa el valor a fitness
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bw: float):
        #Ajuste
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def tweakVariation(self,sigma):
        # Ajuste
        gauss = np.random.normal(0,sigma,self.size)
        for x in self.changes:
            self.cells[x]+=gauss[x]
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)


    def show(self):
        print("Position: ",self.cells)
        print("Fitness: ",self.fitness)