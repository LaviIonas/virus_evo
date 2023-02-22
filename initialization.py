# imports
import numpy as np
import global_var as var
# functions

# INITIALIZE the starting virus population
def initialize_virus_population ():
    return np.zeros((var.virus_length, var.virus_pop_size))

# INITIALIZE the mutation index for virus genome of length n
def mutation_index ():
    # var.virus_length
    mut_index = []
    return mut_index
