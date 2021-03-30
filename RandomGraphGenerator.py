import numpy as np
import sys
import time
import random
import json

"""
    Creates the random instance based on specific parameters
    @arg n is the number of vertices in the graph.
    @arg denseGraph is a boolean that controls the rate of 1
"""


def main(n=5, denseGraph=False, nameFile="test.json"):
    startTime = time.time()  # time start
    matrix = createAdjancencyList(n, denseGraph)
    endTime = time.time() - startTime  # time end
    print("The running time: %.0f\n", endTime)

    writeToFile(nameFile, matrix)


"""
    Generate a random instance of a graph
    @arg n number of nodes
    @arg denseGraph boolean to control # of edges
"""


def createAdjancencyList(n, dense):
    randomAdjencyDict = {}
    for vertex in range(1, n + 1):
        # randomAdjencyDict[str(vertex)] = [1, 2]
        neighbors = []
        for vertexNeighbor in range(1, n + 1):
            if vertex == vertexNeighbor:
                pass
            else:
                chance = random.randint(0, 100)
                if dense:
                    print("Dense graph")
                    if chance > 65:
                        neighbors.append(vertexNeighbor)
                # else no connection
                else:
                    if chance > 50:
                        neighbors.append(vertexNeighbor)
                    # else no connection
        randomAdjencyDict[str(vertex)] = neighbors
    return randomAdjencyDict


"""
    Writes the random instance generated into a test file
    @arg nameOfFile 
"""


def writeToFile(nameOfFile, matrix):

    try:
        data = {}
        writer = open("./" + nameOfFile, "a+")
        data["generator"] = matrix
        json.dump(data, writer)
    finally:
        writer.close()


if __name__ == "__main__":
    inputAl = sys.argv
    # if(len(inputAl) == 3):
    #     n, nameFile,  = int(inputAl[1]), inputAl[1],
    # elif(len(inputAl)==2):
    #     n, nameFile = int(inputAl[1]), int(inputAl[2])
    # # main(n, k)
    main()  # default values
