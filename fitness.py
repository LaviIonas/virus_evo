import random
import global_var as var

def r():
    return random.random()

def update_fitness(virus_pop):
    for v in virus_pop:
        v[var.virus_length+1][1] = r()
