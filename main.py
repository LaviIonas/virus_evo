# import library

# import files
import initialization
import global_var as var
import mutation

# declerations
virus_pop = [] # Set of all Virus'
virus_rep_rate = [] # Set of all Reproduction Rates of each Virus

# ---------------
# Evo Alg
# ---------------

gen = 0

# INITIALIZE the virus population
virus_pop = initialization.initialize_virus_population(var.virus_length, var.virus_pop_size)
# MUTATION INDEX
var.mutation_index = initialization.mutation_index()

while gen < 10:
    new_virus_pop = [] # population of the new virus

    # MUTATE the virus
    for i in range(0, len(virus_pop)):
        new_virus_pop.append(mutation.virus_mutation(virus_pop[i], virus_rep_rate))

    gen += 1 # Next Generation
    print(virus_pop)
