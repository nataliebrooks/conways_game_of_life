"""
    Pr2
    Natalie Brooks
    rosbrooks
"""

""" Runner code to exercise the Life/GraphicLife classes """

from life import *
from graphic_life import *
import time

width = 20
height = 15


stable = [(3,3), (3,4), (2,5), (4,4)]
glider = [(5,5), (6,5), (5,6), (7,6), (5,7)]
pentomino = [(4,4), (3,5), (3,6), (4,5), (5,5)]

def run(height, width, living, ngen, delay):
    """
    Run a life simulation with a given grid height & width,
    an initial list of living cells, number of generations
    to run, and a delay (in seconds) to wait between generations.
    Note: This code won't do anything until you implement the
    required methods of the Life object!
    """

    life = GraphicLife(height, width, living)
    life.show()

    for i in range(ngen):
        time.sleep(delay)
        life.unshow()
        life()
        life.show()
        print("Generation: ", i + 1)

run(40, 40, pentomino, 100, .5)
