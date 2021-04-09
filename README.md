## Project CS3600 Winter 2021 Section 0056-Dr.Kolokolova

# Author: Johan Alexander Arcos Mendez

# SAT solver used: PySAT

## Random Instance Generator Module
Creates a stochastic UNDIRECTED GRAPH in adjanceny form.
e.g., {"1": [2,3,4],
        "2": [3,4]...,
        }
# Note: Keys are str and value array are ints

GraphGenerator.py returns the random created adjacency matrix
•Where [i][j]= 1 v 0 indicates if there is an edge connecting vertices i and j.

# Note
Logic sets matrix such that loops are not permitted.


## Monochromatic Triangle Module
• Solves the problem.

## Main Module
Controls the program flow. 

## How to run?
You can run a module individually, with this command:
python "nameOfFile" e.g., python RamdonGraphGenerator.py

In order to visualize the project completely run: (Note: it takes some time to show the graphics)

python Main.py
