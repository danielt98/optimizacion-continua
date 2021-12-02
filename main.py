import numpy as np
from hillclimbing import hillclimbing
from sphere import sphere
from step import step
from schwefel import schwefel
from rastrigin import rastrigin
from griewank import griewank
import matplotlib.pyplot as plt
from hillclimbingRandom import hillclimbingRandom
from hillclimbingReplacement import hillclimbingReplacement

if __name__ == '__main__':
    # myStep = step (-5.0, 5.0)
    # input = np.arrange(1,4);
    # result = myStep.evaluate(input)
    # print (result)
    #Semilla inicial en el proceso de generar numeros aleatorios
    np.random.seed(1000)
    #myStep = step(-5.0, 5.0)
    #myHC = hillclimbing(myStep, 2, 1000, 0.5)

    #mySphere = sphere(-5.0, 5.0)
    #myHC = hillclimbing(mySphere, 4, 100, 0.5)

    #mySchwefel = schwefel(-5.0, 5.0)
    #myHC = hillclimbing(mySchwefel, 4, 100, 0.5)

    #myRastrigin = rastrigin(-5.0, 5.0)
    #myHC = hillclimbing(myRastrigin, 2, 100, 0.5)

    myGriewank = griewank(-5.0, 5.0)
    myHC = hillclimbing(myGriewank,2, 100, 0.5)

    [x, y] = myHC.evolve()

    mysphere = sphere(-5.0, 5.0)
    #myHCR = hillclimbingRandom(mysphere, 4, 100, 0.5, 20)
    #[x, y] = myHCR.evolve()

    #mysphere = sphere(-5.0, 5.0)
    #myHCReplace = hillclimbingReplacement(mysphere, 4, 100, 0.5, 20)
    #[x, y] = myHCReplace.evolve()


    # plotting
    plt.title("Convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.plot(x, y, color="red")
    plt.show()
