# import library

# import files
import random

import initialization
import global_var as var
import mutation
import treelib

# declerations
virus_rep_rate = []  # Set of all Reproduction Rates of each Virus

# ---------------
# Evo Alg
# ---------------

# Set gen start
gen = 0
gen_max = 10

# INITIALIZE the virus population

virus_pop = initialization.initialize_virus_population()
for i in range(len(virus_pop)):
    for j in range(len(virus_pop[i])):
        virus_pop[i][j + 1].tag = mutation.virus_mutation(virus_pop[i][j + 1].tag)
    # virus_pop[i].show()

#virus_pop[1].show()
def transform(virus):
    new = []
    for node in range(1, var.virus_length + 1):
        new.append(virus.get_node(node).tag)
    return new

def choose_LP():
    LP = []
    numLP = random.randint(1, 3)
    for i in range(numLP):
        lethal = random.randint(0, 7)
        if lethal not in LP:
            LP.append(lethal)
    return LP

new_virus = transform(virus_pop[1])
LP = choose_LP()
print(LP)
print(new_virus)
new_virus.append(LP)
print(new_virus)







