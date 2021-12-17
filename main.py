import numpy as np
from functions.sphere import sphere
from functions.step import step
from functions.schwefel import schwefel
from functions.rastrigin import rastrigin
from functions.griewank import griewank
from functions.ackley import ackley
import matplotlib.pyplot as plt
from algorithms.hillclimbing import hillclimbing
from algorithms.hillclimbingReplacement import hillclimbingReplacement
from algorithms.hillclimbingReplacementOpuestaCaos import hillclimbingReplacementOpuestaCaos
from excelExport import  excelExport
import time

if __name__ == '__main__':
    maxRepetitions = 31
    maxIterations = 1000
    dimensions = 10
    avgX = np.arange(0, maxIterations)

    myStep = step(-100, 100)
    mySphere = sphere(-100, 100)
    mySchwefel = schwefel(-100, 100)
    myRastrigin = rastrigin(-5.12, 5.12)
    myGriewank = griewank(-600, 600)
    myAckley = ackley(-32, 32)
    #myHCR = hillclimbingRandom(mysphere, 4, 100, 0.5, 20)
    myProblems = {'Sphere':[mySphere,None,None],
                  'Step':[myStep,None,None],
                  'Schwefel':[mySchwefel,None,None],
                  'Rastrigin':[myRastrigin,None,None],
                  'Griewank':[myGriewank,None,None],
                  'Ackley':[myAckley,None,None]}
    # myHCReplac= hillclimbing(myProblems[function][0], dimensions, maxIterations, 0.6)
    myHCReplace = hillclimbingReplacement(dimensions, maxIterations, 0.6)
    # | Dimenciones | Repeticiones | BW | Step | Cantidad que se van a estar ajustando
    myHCReplaceOC = hillclimbingReplacementOpuestaCaos(dimensions, maxIterations, 0.6, 0.09,7)
    myAlgorithms = [myHCReplace,myHCReplaceOC]
    for function in myProblems:
        best = []
        pos = 0
        times = []
        for algorithm in myAlgorithms:
            avgY = np.zeros(maxIterations, float)
            best.append(np.zeros(maxRepetitions, dtype=float))
            times.append(np.copy(time.time()))
            for i in range(maxRepetitions):
                np.random.seed(i)
                [x, y] = algorithm.evolve(myProblems[function][0])
                best[pos][i] = algorithm.best.fitness
                avgY = avgY + y
            fin = time.time()
            times[pos] =fin - times[pos]
            plt.plot(avgX, avgY)
            pos+=1
        myProblems[function][2] = np.copy(times)
        myProblems[function][1] = np.copy(best)
        # plotting
        plt.title("Convergence curve " + function)
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.legend(["HCReplace","HCReplaceChaos"])
        plt.show()
    myExport = excelExport(myProblems)
    myExport.evaluate()

"""
    fig1, ax1 = plt.subplots() 16:19
    ax1.set_title('Box Plot for best solutions')
    ax1.boxplot(best)
    plt.show()
"""