from pysat.solvers import Glucose3
import sys
import time
from MonochromaticTriangle import reduceGraphToSAT
from RandomGraphGenerator import generateRandomGraph
from plotResults import plotFirstQuestion

"""
    This is the primary entry file to this project.

    It makes the appropriate calls to MonochromaticTriangle.py and RandomGraphGenerator.py

    RandomGraph will generate a graph based on two parameters n=number of vertices & edgePopulation = {1,2,3}, which represents the likelihood of edges sparse(0.25), medium(0.5), and dense graph(0.75).
    # of edges (m) = f(n,p) = n*p
    
"""


def main():

    # First section computes random instance for normal graphs. Probability is 0.5.
    # Second section runs the SAT solver on these created instances
    filename = "./test.json"
    outputCNF = "./test.cnf"
    plotDataFirstQuestFile = "./firstQuestionPlot.txt"  # edges and number of vertices
    plotDataSecondQuestFile = (
        "./secondQuestionPlot.txt"  # time, fractionSatisInstances, #vertices
    )
    try:
        writer = open(plotDataFirstQuestFile, "a+")
        writer.truncate(0)  # erase the contents before appending
        writerSAT = open(plotDataSecondQuestFile, "a+")
        writer.truncate(0)  # erase the contents before appending
        for numVertices in range(5, 31):
            averageEdges = 0
            averageRunningTimeSAT = 0
            satisfiableInstances = 0
            for i in range(10):
                generateRandomGraph(
                    numVertices, 2, filename
                )  # 2 represents normal graph
                edges = reduceGraphToSAT(filename, outputCNF)
                averageEdges += edges

                # Start second section
                startTime = time.time()  # time start
                answer, partiton = addClausestoSATSolver(outputCNF)
                endTime = time.time() - startTime  # time end
                averageRunningTimeSAT += endTime
                if answer == True:
                    satisfiableInstances += 1

            averageEdges = float(averageEdges / 10)
            writer.write(str(averageEdges) + "," + str(numVertices) + "\n")

            fractionOfSatisfiable = float(satisfiableInstances / 10)
            averageTime = float(averageRunningTimeSAT / 10)
            writerSAT.write(
                str(averageTime)
                + ","
                + str(fractionOfSatisfiable)
                + ","
                + str(numVertices)
                + "\n"
            )

    finally:
        writer.close()
        writerSAT.close()

    plotFirstQuestion(plotDataFirstQuestFile)
    # ------------------------------- End first & second sections  -------------------------


"""
    Utilitity function to add clauses to the solver.
"""


def addClausestoSATSolver(inputFilename):
    solver = Glucose3()
    try:
        reader = open(inputFilename, "r")
        clauses = reader.readlines()
        i = 0
        clausesSAT = []
        for clause in clauses:
            if i == 0:
                pass
            else:
                cleanClause = clause.strip("\n")
                cleanClause = clause.strip()
                arClause = cleanClause.split(" ")
                finalClause = []
                for var in arClause:
                    finalClause.append(int(var))
                clausesSAT.append(finalClause)
            i += 1

        for clause in clausesSAT:
            solver.add_clause(clause)

        return (solver.solve(), solver.get_model())
        # print(solver.solve())
        # print(solver.get_model())

    finally:
        reader.close()


if __name__ == "__main__":
    # inputAl = sys.argv
    # print(inputAl)
    # if len(inputAl) == 3:
    #     n, nameFile, = (
    #         int(inputAl[1]),
    #         inputAl[1],
    #     )
    # elif len(inputAl) == 2:
    #     n, nameFile = int(inputAl[1]), int(inputAl[2])
    # main(n, k)
    main()
