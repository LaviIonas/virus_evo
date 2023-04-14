# imports
import global_var as var
import random

# functions

# INITIALIZE A Virus Population
import mutation


def initialize_virus_population ():
    virus_pop = []
    for i in range(0, var.virus_pop_size):
        virus = initialize_virus()
        virus_pop.append(virus)

    return virus_pop

# INITIALIZE A Virus
def initialize_virus ():
    virus = []
    for i in range(var.virus_length):
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

def alterLethalPoint(individual):
    """
    Re-initialize the LP indices
    :param binary string virus individual
    :return: None
    """
    individual[var.virus_length] = init_LP()

def MutateLethalPoint(individual):
    """
    Re-initialize a single binary string
    :param binary string virus individual:
    :return: None
    """
    # Find the binary string that represents the LP
    for p in individual[var.virus_length]:
        individual[p] = mutation.virus_mutation(individual[p])
