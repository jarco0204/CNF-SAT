import numpy as np
import matplotlib.pyplot as plt


def plotFirstQuestion(filename="./firstQuestionPlotNormal.txt"):
    data = []  # 2D array
    try:
        writer = open(filename, "r")
        lines = writer.readlines()
        for line in lines:
            temp = line.strip("\n")
            data.append(temp.split(","))

    finally:
        writer.close()

    # Change list to np array to access columns
    arr = np.array(data, dtype=float)
    edgesData = arr[:, 0]
    verticesData = arr[:, 1]

    # Graphics for first comparison
    plt.figure()
    plt.gray()
    plt.title("Edges as function of vertices")
    plt.xlabel("vertices (n)")
    # plt.xticks([5, 10, 15, 20, 25, 30])
    plt.ylabel("edges (m) ")
    # plt.yticks([25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300])
    plt.plot(verticesData, edgesData, label="f(n)=m")
    plt.legend()
    plt.show()


def plotSecondQuestion(filename="./secondQuestionPlotNormal.txt"):
    data = []  # 2D array
    try:
        writer = open(filename, "r")
        lines = writer.readlines()
        for line in lines:
            temp = line.strip("\n")
            data.append(temp.split(","))

    finally:
        writer.close()

    # Change list to np array to access columns
    arr = np.array(data, dtype=float)
    time = arr[:, 0]
    ratioSolved = arr[:, 1]
    n = arr[:, 2]

    # Graphics for first comparison
    plt.figure()
    plt.gray()

    # First graphic
    plt.subplot(1, 2, 1)
    plt.title("Time as a function of n")
    plt.xlabel("vertices (n)")
    plt.ylabel("time (s) ")
    plt.plot(n, time, label="Satisfiability time")
    plt.legend()

    # Second graphic
    plt.subplot(1, 2, 2)
    plt.title("Satisfiable instances (# of satisfiable/10) ")
    plt.xlabel("vertices (n)")
    plt.ylabel("Ratio of satisfiable instances ")
    plt.plot(n, ratioSolved, label="Satisfiable ratio")

    plt.legend()
    plt.show()


def plotSparse(edgesDataFile, timeDataFile):
    dataEdges = []  # 2D array
    dataTime = []  # 2D array
    try:
        writer = open(edgesDataFile, "r")
        writerTime = open(timeDataFile, "r")
        lines = writer.readlines()
        linesTime = writerTime.readlines()
        for line in lines:
            temp = line.strip("\n")
            dataEdges.append(temp.split(","))

        for line in linesTime:
            temp = line.strip("\n")
            dataTime.append(temp.split(","))

    finally:
        writer.close()
        writerTime.close()

    # Change list to np array to access columns
    arr = np.array(dataEdges, dtype=float)
    edgesData = arr[:, 0]
    verticesData = arr[:, 1]

    # Change list to np array to access columns
    arrTime = np.array(dataTime, dtype=float)
    time = arrTime[:, 0]
    ratioSolved = arrTime[:, 1]
    n = arrTime[:, 2]

    # Graphics for 3 subgraphics comparison
    plt.figure()
    plt.gray()

    # Graphics for first comparison
    plt.subplot(1, 3, 1)
    plt.title("Edges as function of vertices")
    plt.xlabel("vertices (n)")
    # plt.xticks(np.arange(min(verticesData), max(verticesData), 5.0))
    plt.ylabel("edges (m) ")
    # plt.yticks(np.arange(min(edgesData), max(edgesData), 20.0))
    plt.plot(verticesData, edgesData, label="f(n)=m")
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.title("Time as a function of n")
    plt.xlabel("vertices (n)")
    plt.ylabel("time (s) ")
    plt.plot(verticesData, time, label="Satisfiability time")
    plt.legend()

    # Third graphic
    plt.subplot(1, 3, 3)
    plt.title("Satisfiable instances (# of satisfiable/10) ")
    plt.xlabel("vertices (n)")
    plt.ylabel("Ratio of satisfiable instances ")
    # plt.yticks(np.arange(min(ratioSolved), max(ratioSolved), 0.1))
    plt.plot(verticesData, ratioSolved, label="Satisfiable ratio")
    plt.legend()

    plt.show()


def plotDense(edgesDataFile, timeDataFile):
    dataEdges = []  # 2D array
    dataTime = []  # 2D array
    try:
        writer = open(edgesDataFile, "r")
        writerTime = open(timeDataFile, "r")
        lines = writer.readlines()
        linesTime = writerTime.readlines()
        for line in lines:
            temp = line.strip("\n")
            dataEdges.append(temp.split(","))

        for line in linesTime:
            temp = line.strip("\n")
            dataTime.append(temp.split(","))

    finally:
        writer.close()
        writerTime.close()

    # Change list to np array to access columns
    arr = np.array(dataEdges, dtype=float)
    edgesData = arr[:, 0]
    verticesData = arr[:, 1]

    # Change list to np array to access columns
    arrTime = np.array(dataTime, dtype=float)
    time = arrTime[:, 0]
    ratioSolved = arrTime[:, 1]
    n = arrTime[:, 2]

    # Graphics for 3 subgraphics comparison
    plt.figure()
    plt.gray()

    # Graphics for first comparison
    plt.subplot(1, 3, 1)
    plt.title("Edges as function of vertices")
    plt.xlabel("vertices (n)")
    plt.ylabel("edges (m) ")
    plt.plot(verticesData, edgesData, label="f(n)=m")
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.title("Time as a function of n")
    plt.xlabel("vertices (n)")
    plt.ylabel("time (s) ")
    plt.plot(n, time, label="Satisfiability time")
    plt.legend()

    # Second graphic
    plt.subplot(1, 3, 3)
    plt.title("Satisfiable instances (# of satisfiable/10) ")
    plt.xlabel("vertices (n)")
    plt.ylabel("Ratio of satisfiable instances ")
    plt.plot(n, ratioSolved, label="Satisfiable ratio")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    plotDense("./thirdQuestionEdgesDensePlot.txt", "./thirdQuestionTimeDensePlot.txt")

