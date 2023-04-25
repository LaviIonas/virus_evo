# import
import random
import numpy as np
import global_var as var
import initialization

# NATURAL SELECTION IMPLEMENTATION
def virus_mutation(virus):
    if random.random() < var.virus_mut_rate:
        # select a random index in all the nodes
        r1 = random.randint(0,var.virus_length-1)
        r2 = random.randint(0,var.virus_length-1)

        virus[r1][r2] = 1 - virus[r1][r2]

        mut_index = r1*var.virus_length + r2

        if virus[r1][r2] == 0:
            virus[var.virus_length+2][mut_index] = 0
        else:
            virus[var.virus_length+2][mut_index] = (var.b - var.a)*np.random.rand() + var.a

def vaccine_mutation(vaccine):
    if random.random() < var.vaccine_mut_rate:
        r1 = random.randint(0, var.virus_length-1)
        vaccine[r1] = 1 - vaccine[r1]

def virus_lp_mutation(virus):
    if random.random() < var.virus_lp_rate:
        virus[var.virus_length] = initialization.init_LP()
