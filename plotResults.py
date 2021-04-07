import numpy as np
import matplotlib.pyplot as plt


def plotFirstQuestion(filename="./firstQuestionPlot.txt"):
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
    arr = np.array(data)
    edgesData = arr[:, 0]
    verticesData = arr[:, 1]

    # Graphics for first comparison
    plt.figure()
    plt.gray()
    plt.title("Edges as function of vertices")
    plt.xlabel("vertices (n)")
    plt.ylabel("edges (m) ")
    plt.plot(verticesData, edgesData, label="f(n)=m")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plotFirstQuestion()  # default values
