import numpy as np
from functions.sphere import sphere
from functions.step import step
from functions.schwefel import schwefel
from functions.rastrigin import rastrigin
from functions.griewank import griewank
from functions.ackley import ackley
import matplotlib.pyplot as plt
from algorithms.hillclimbing import hillclimbing
from algorithms.HcModifide import HcModifide
from algorithms.hillclimbingReplacement import hillclimbingReplacement
from algorithms.hillclimbingReplacementM import hillclimbingReplacementM
from excelExport import excelExport
import time

if __name__ == '__main__':
    maxRepetitions = 30
    maxIterations = 1000
    dimensions = 10
    avgX = np.arange(0, maxIterations)
    bandwith = 0.9

    myStep = step(-100, 100)
    mySphere = sphere(-100, 100)
    mySchwefel = schwefel(-100, 100)
    myRastrigin = rastrigin(-5.12, 5.12)
    myGriewank = griewank(-600, 600)
    myAckley = ackley(-32, 32)
    #myHCR = hillclimbingRandom(mysphere, 4, 100, 0.5, 20)
    myProblems = [mySphere,myStep,mySchwefel,myRastrigin,myGriewank,myAckley]
    myHC = hillclimbing(dimensions, maxIterations, bandwith)
    # Step | Prob de usar tweak normal
    myHCM = HcModifide(dimensions, maxIterations, bandwith,5,50)
    #myHCReplace = hillclimbingReplacement(dimensions, maxIterations, bandwith)
    #Step | Cantidad que se van a estar ajustando| Prob de usar Gauss | Cantidad de vecinos
    #myHCReplaceOC = hillclimbingReplacementM(dimensions, maxIterations, bandwith, 10,60,100)
    myAlgorithms = [myHC,myHCM]
    myLeg = []
    myData = []
    for function in myProblems:
        best = (np.zeros(maxRepetitions, dtype=float))
        times = 0
        for algorithm in myAlgorithms:
            avgY = np.zeros(maxIterations, float)
            times = time.time()
            for i in range(maxRepetitions):
                np.random.seed(i)
                [x, y] = algorithm.evolve(function)
                best[i] = algorithm.best.fitness
                avgY = avgY + y
            fin = time.time()
            times = fin - times
            avgY = avgY/maxIterations
            plt.plot(avgX, avgY)
            myLeg.append(str(algorithm))
            myData.append([str(function),best.mean(),best.std(),best.max(),best.min(),times])
        # plotting
        plt.title("Convergence curve " + str(function))
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.legend(myLeg)
        plt.show()
    myExport = excelExport(myData)
    myExport.evaluate()

"""
    fig1, ax1 = plt.subplots() 16:19
    ax1.set_title('Box Plot for best solutions')
    ax1.boxplot(best)
    plt.show()
"""