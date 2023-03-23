# import
import random
import global_var as var

# function
def virus_mutation(individual):
    new_individual = random.choices(population=[0, 1], weights=var.mutation_rate, k=len(individual))
    return new_individual
