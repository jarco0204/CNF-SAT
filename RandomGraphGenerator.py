import numpy as np
import random
import json

# import time

"""
    Creates the random instance based on specific parameters
    @arg n is the number of vertices in the graph.
    @arg denseGraph is int to control likelihood of # of edges {1,2,3}
        Default parameter is 2 which indicates 50% likehood of an edge
"""


def generateRandomGraph(n=5, denseGraph=2, nameFile="randomInstance.json"):
    # startTime = time.time()  # time start
    matrix = createAdjancencyList(n, denseGraph)
    # endTime = time.time() - startTime  # time end
    # print("The running time: %.0f\n", endTime)

    writeToFile(nameFile, matrix)


"""
    Generate a random instance of a graph
    @arg n number of nodes
    @arg denseGraph int to control likelihood of # of edges {1,2,3}
"""


def createAdjancencyList(n, dense):
    randomAdjencyDict = {}
    for vertex in range(1, n + 1):
        # randomAdjencyDict[str(vertex)] = [1, 2]
        neighbors = []
        for vertexNeighbor in range(1, n + 1):
            if vertex == vertexNeighbor:
                pass  # no self-loops
            else:
                chance = random.randint(0, 100)
                if dense == 1:
                    # print("25% likelihood of edge (sparse)")
                    if chance > 75:
                        neighbors.append(vertexNeighbor)
                    # else no edge
                elif dense == 2:
                    # print("50% likelihood of edge (medium)")
                    if chance > 50:
                        neighbors.append(vertexNeighbor)
                    # else no connection
                elif dense == 3:
                    # print("75% likelihood of edge (dense)")
                    if chance > 25:
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
        writer.truncate(0)  # erase
        data["generator"] = matrix
        json.dump(data, writer)
    finally:
        writer.close()


if __name__ == "__main__":
    generateRandomGraph()  # default values
