# imports
import numpy as np
import global_var as var
import random

# functions

# INITIALIZE A Virus Population
def initialize_virus_population ():
    virus_pop = []
    for i in range(0, var.virus_pop_size):
        virus = initialize_virus()
        virus_pop.append(virus)

    return virus_pop

# INITIALIZE A Virus
def initialize_virus ():
    virus = []
    for i in range(1, var.virus_length):
        virus.append([0]*var.virus_length)

    # Append List of Lethal Points
    LP = init_LP()
    virus.append(LP)

    # Append List of Properties
    virus.append([0]) # Threatened Boolean

    return virus

def init_LP ():
    LP = []
    numLP = random.randint(1, 3)
    for i in range(numLP):
        lethal = random.randint(0, 7)
        if lethal not in LP:
            LP.append(lethal)
    return LP
