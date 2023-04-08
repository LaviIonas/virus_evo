# import library

# import files
import random

import initialization
import global_var as var
import helper as help
import mutation

# declerations
virus_rep_rate = []  # Set of all Reproduction Rates of each Virus

# ---------------
# Evo Alg
# ---------------

# Set gen start
gen = 0
gen_max = 10

# INITIALIZE
virus_pop = initialization.initialize_virus_population()
var.vaccine = initialization.initialize_vaccine()

# FITNESS
# evaluate fitness of the populations

# GENERATIONAL LOOP


# for i in range(len(virus_pop)):
#     for j in range(len(virus_pop[i])):
#         virus_pop[i][j + 1].tag = mutation.virus_mutation(virus_pop[i][j + 1].tag)
# virus_pop[i].show()
