import numpy as np
import solution as solution
from sphere import sphere

class solution:
    def __init__(self, dimension: int, function):
        self.size = dimension
        #Llenar el vector de 0
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = function

    def from_solution(self, origin:solution):
        #Asignar tamaño solucion inicial
        self.size = origin.size
        #Copia dimenciones iniciales
        self.cells = np.copy(origin.cells)
        #Asignar original fitness
        self.fitness = origin.fitness
        #original function
        self.function = origin.function

    def randomInitialization(self):
        #Numeros aleatorios en las dimenciones | Vector solucion
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,size=(self.size,))
        #Evalua en la funcion y regresa el valor a fitness
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bw: float):
        #Ajuste
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def show(self):
        print("Position: ",self.cells)
        print("Fitness: ",self.fitness)