# import library

# import files
import random

import global_var
import initialization
import global_var as var
import mutation
import helper

# declerations
virus_rep_rate = []  # Set of all Reproduction Rates of each Virus

# ---------------
# Evo Alg
# ---------------

# Set gen start
gen = 0
gen_max = 10

# INITIALIZE the virus population

"""
Mutate the lethal point
"""
virus_pop = initialization.initialize_virus_population()
for i in range(global_var.virus_length):
   for j in range(global_var.virus_length):
       virus_pop[i][j] = mutation.virus_mutation(virus_pop[i][j])
print(virus_pop[0])
initialization.MutateLethalPoint(virus_pop[0])
print(virus_pop[0])
"""
Geter, setter
"""
print(helper.LP_get(virus_pop[0]))
helper.LP_set(virus_pop[0], [1, 2])
print(helper.LP_get(virus_pop[0]))

# for i in range(len(virus_pop)):
#     for j in range(len(virus_pop[i])):
#         virus_pop[i][j + 1].tag = mutation.virus_mutation(virus_pop[i][j + 1].tag)
# virus_pop[i].show()
