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

# Set gen start
gen = 0
gen_max = 10

# INITIALIZE the virus population
virus_pop = initialization.initialize_virus_population(var.virus_length, var.virus_pop_size)
# INITIALIZE the mutation index
var.mutation_index = initialization.mutation_index()

while gen < gen_max:
    new_virus_pop = [] # population of the new virus

    # MUTATE the virus
    for i in range(0, len(virus_pop)):
        new_virus_pop.append(mutation.virus_mutation(virus_pop[i], virus_rep_rate))

    gen += 1 # Next Generation
    print(virus_pop)
