import random

def temp(virus_pop):
    fitness = []
    for i in virus_pop:
        fitness.append(random.random())
    return fitness
