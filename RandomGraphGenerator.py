import numpy as np
import time
import random

"""
    Creates the random instance based on specific parameters
    @arg n is the number of vertices in the graph.
    @arg denseGraph is a boolean that controls the rate of 1
"""


def main(n=5, denseGraph=False):
    startTime = time.time()  # time start
    # ramdomMatrix = np.zeros((n, n), dtype=int)
    # # adjacency = np.random.randint(0, 2, (n, n)) #50% probability
    # print(adjacency)
    randomAdjencyDict = {}
    for vertex in range(1, n + 1):
        # randomAdjencyDict[str(vertex)] = [1, 2]
        neighbors = []
        for vertexNeighbor in range(1, n + 1):
            if vertex == vertexNeighbor:
                pass
            else:
                chance = random.randint(0, 100)
                if denseGraph:
                    print("Dense graph")
                    if chance > 65:
                        neighbors.append(vertexNeighbor)
                # else no connection
                else:
                    if chance > 50:
                        neighbors.append(vertexNeighbor)
                    # else no connection
        randomAdjencyDict[str(vertex)] = neighbors

    endTime = time.time() - startTime  # time end
    print(randomAdjencyDict)
    print("The running time: %.0f\n", endTime)


main()
