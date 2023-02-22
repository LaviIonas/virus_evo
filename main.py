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

virus_pop = initialization.initialize_virus_population(virus_length=6, virus_pop_size=10)
mutation_rate = [0.4, 0.6]
while gen < 10:
    new_virus_pop = [] # population of the new virus

    # MUTATE the virus
    for virus in virus_pop:
        new_virus_pop.append(mutation.virus_mutation(virus, mutation_rate))

    gen += 1 # Next Generation

print(new_virus_pop)

