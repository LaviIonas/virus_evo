# import
import random
import global_var as var

# function
def virus_node_mutation(virus):
    if random.random() < var.virus_mut_rate:
        r1 = random.randint(0,var.virus_length-1)
        r2 = random.randint(0,var.virus_length-1)

        virus[r1][r2] = 1 - virus[r1][r2]

def virus_lp_muation(virus):
    return 0

def virus_tree_mutation(individual):
    new_individual = random.choices(population=[0, 1], weights=var.mutation_rate, k=len(individual))
    return new_individual
