import json
import time

"""
    This file is the graph solution to the monographic triangle problem.

    Input: An n-node undirected graph G(V,E) with node set V and edge set E. 

    Question: Can the edges, E, of G be partitioned into two disjoint sets E1 and E2, in such a way that neither of the two graphs G1(V,E1) or G2(V,E2) contains a triangle, i.e. a set of three distinct nodes u,v,w such that {u,v}, {u,w}, {v,w} are all edges?
    
    Output: True or false (NP)-Proof verifiable if nondeterministic polynomial time.

"""


def main(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
            startTime = time.time()  # time start
            variables, clauses, illegalTriangles = solveMonoTriangle(data["generator"])
            outputCNF(variables, clauses, illegalTriangles)

    finally:
        f.close()


"""
    This module creates the .cnf file required by the SAT solver.
    The general idea is that every triangle will be transformed into two clauses.
    E.g., if vertices 1,5,2 make a triangle, then the clauses are (1 v 5 v 2) ^ (~1 v ~5 v ~2)
"""


def outputCNF(variables, numClauses, triangles):
    clauses = createClauses(triangles)
    try:

        writer = open("./" + "instance.cnf", "a+")
        writer.truncate(0)  # erase all the content

        # Write first line
        writer.write("p " + "CNF " + str(variables) + " " + str(numClauses) + "\n")

        # Write clauses
        for clause in clauses:
            # Write negative clause
            writer.write(clause)

    finally:
        writer.close()


"""
    This function creates an array of clauses of len len(triangles)*2
    It changes an array of vertices into a CNF formula
"""


def createClauses(triangles):
    clausesAr = []

    # clauses of the form (1 v 2 v 3)
    for triangle in triangles:
        clause = ""
        for var in triangle:
            clause = clause + str(var) + " "
        clause = clause + "\n"
        clausesAr.append(clause)

    # clauses of the form (-1 v -2 v -3)
    for triangle in triangles:
        clause = ""
        for var in triangle:
            clause = clause + "-" + str(var) + " "
        clause = clause + "\n"
        clausesAr.append(clause)

    return clausesAr


"""
    Determines if the instance can be partition into two such that a triangle is not created
"""


def solveMonoTriangle(instance):
    vertices = instance.keys()
    edges = createSetOfEdges(vertices, instance)
    print("Adjacency list of problem: ", instance)
    print("All edges is the graph :", edges)
    # Solution to go through all edges and check
    illegalTriangles = []
    for edge in edges:
        verticesNeighbors = []
        for vertex in edge:
            verticesNeighbors.append(instance[str(vertex)])

        # Section to check if edges form an illegal triangle
        for neighbor in verticesNeighbors[0]:
            if neighbor in verticesNeighbors[1]:
                # print("illegal")
                if (
                    [edge[0], edge[1], neighbor] not in illegalTriangles
                    and [edge[0], neighbor, edge[1]] not in illegalTriangles
                    and [edge[1], edge[0], neighbor] not in illegalTriangles
                    and [edge[1], neighbor, edge[0]] not in illegalTriangles
                    and [neighbor, edge[0], edge[1]] not in illegalTriangles
                    and [neighbor, edge[1], edge[0]] not in illegalTriangles
                ):
                    illegalTriangles.append([edge[0], neighbor, edge[1]])
    print("Illegal triangles : ", illegalTriangles)
    return len(vertices), 2 * len(illegalTriangles), illegalTriangles


"""
    Creates a 2D array of edges [[1,2], [vertex1, vertex2],...]
"""


def createSetOfEdges(vertices, data):
    returnAr = []
    for vertex in vertices:
        edgesVertex = data[vertex]
        for vertexNeighbor in edgesVertex:
            if [vertexNeighbor, int(vertex)] in returnAr:
                pass
            else:
                returnAr.append([int(vertex), vertexNeighbor])
    return returnAr


if __name__ == "__main__":
    main("randomInstance.json")  # default values

