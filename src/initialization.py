# imports
import numpy as np
import global_var as var
import random
import mutation
# functions

# INITIALIZE A Virus Population
def initialize_virus_population ():
    virus_pop = []
    for i in range(0, var.virus_pop_size):
        id = "R" + str(i+1) + "-"
        virus = initialize_virus(id)
        virus_pop.append(virus)

    return virus_pop

# INITIALIZE A Virus
def initialize_virus (id):
    virus = []
    for i in range(0, var.virus_length):
        virus.append([0]*var.virus_node_length)

    # Append List of Lethal Points
    LP = init_LP()
    virus.append(LP)

    # Append List of Properties
    virus.append([])

    # Append Threat Boolean to Properties
    virus[var.virus_length+1].append(0)
    # Append Fitness Score to Properties
    virus[var.virus_length+1].append(0)
    # Append Virality Score to Properties
    virus[var.virus_length+1].append(1)
    # Append Virus Name
    virus[var.virus_length+1].append(id)

    # Mutation Value Array
    virus.append([0]*var.virus_length*var.virus_node_length)

    return virus

def generate_randomly(length):
    choices = [0,1]
    return [random.choice(choices) for _ in range(length)]

def initialize_vaccine_population():
    vaccine_pop = [generate_randomly(8) for _ in range(var.vaccine_pop_size)]
    return vaccine_pop
    

#INITIALIZE lethal points of a virus
def init_LP ():
    LP = []
    numLP = 3
    for i in range(random.randint(1, numLP+1)):
        lethal = random.randint(0, var.virus_length-1)
        if lethal not in LP:
            LP.append(lethal)
    return LP
