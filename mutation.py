# import
import random
import global_var as var

# function
def virus_mutation(individual):
    new_individual = random.choices(population=[0, 1], weights=var.mutation_rate, k=len(individual))
    # for i in range(len(new_individual)):
    #     mutate_value = random.uniform(-1, 1)
    #     mutate_value = str(round(mutate_value, 2))
    #     if new_individual[i] == 1:
    #         new_individual[i] = float(mutate_value)
    return new_individual
