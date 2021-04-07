from pysat.solvers import Glucose3
import sys

"""
    This is the primary entry file to this project.

    It makes the appropriate calls to MonochromaticTriangle.py and RandomGraphGenerator.py

    Will contain the section that evaluates performance.
    
"""


def main():
    pass


if __name__ == "__main__":
    inputAl = sys.argv
    print(inputAl)
    if len(inputAl) == 3:
        n, nameFile, = (
            int(inputAl[1]),
            inputAl[1],
        )
    elif len(inputAl) == 2:
        n, nameFile = int(inputAl[1]), int(inputAl[2])
    # main(n, k)
