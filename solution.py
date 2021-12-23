import numpy as np
import solution as solution


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

    def randomInitializationVariaton(self,step):
        # Numeros aleatorios en las dimenciones | Vector solucion
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound, size=(self.size,))
        # Numeros aleatorios en las dimenciones que tenga un step de separación
        iterations = 0
        for i in range(self.size):
            self.cells[i],it = self.__selectBest(step, self.cells[i])
            iterations+=it
        #Evalua en la funcion y regresa el valor a fitness
        self.fitness = self.function.evaluate(self.cells)
    def __selectBest(self,step,bound):
        #Mustreo en el espacio de busqueda
        finish = bound+step*5
        start = bound-step*5
        localSearch = np.arange(start,finish, step)
        localSearch[localSearch < self.function.lowerbound] = self.function.lowerbound
        localSearch[localSearch > self.function.upperbound] = self.function.upperbound
        #localSearch= np.arange(np.abs(bound)*(-1), np.abs(bound), step)
        localSearch = list(set(localSearch))
        if len(localSearch)<self.size:
            localSearch = np.random.choice(localSearch, len(localSearch), replace=False)
        else:
            localSearch = np.random.choice(localSearch, self.size,replace=False)
        best = 50000
        pos=0
        for i in range(len(localSearch)):
            auxDimiension = np.zeros(1, float)
            auxDimiension[0]=localSearch[i]
            auxFitness = self.function.evaluate(auxDimiension)
            if best > auxFitness:
                best = auxFitness
                pos = i
        return localSearch[pos],i+1



    def tweak(self, bw: float):
        #Ajuste
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def tweakVariation(self,bw,probGauss):
        # Ajuste
        probability = np.full(100, probGauss)
        for i in range(probGauss,100):
            probability[i]=(100-probGauss)
        choice = np.random.choice(probability)
        if choice == probGauss:
            """
            gauss = np.random.normal(0,sigma,self.size)
            for x in self.changes:
                self.cells[x]+=gauss[x]
            self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
            self.cells[self.cells > self.function.upperbound] = self.function.upperbound
            self.fitness = self.function.evaluate(self.cells)
            """
            self.tweak(bw)
        else:
            self.cells = self.cells*(-1)



    def show(self):
        print("Position: ",self.cells)
        print("Fitness: ",self.fitness)