# import
import random
import numpy as np
import global_var as var


# function
def virus_node_mutation(virus):
    if random.random() < var.virus_mut_rate:
        r1 = random.randint(0,var.virus_length-1)
        r2 = random.randint(0,var.virus_length-1)

        virus[r1][r2] = 1 - virus[r1][r2]

        mut_index = r1*var.virus_length + r2
        print("MUT INDEX", mut_index)

        if virus[r1][r2] == 0:
            virus[var.virus_length+2][mut_index] = 0
        else:
            virus[var.virus_length+2][mut_index] = (var.b - var.a)*np.random.rand() + var.a


def virus_lp_muation(virus):
    return 0

def virus_tree_mutation(individual):
    new_individual = random.choices(population=[0, 1], weights=var.mutation_rate, k=len(individual))
    return new_individual
