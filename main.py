# import library

# import files
import initialization
import mutation

# declerations
virus_pop_size = 10 # Number of Virus in Population
virus_length = 6 # Size of the Virus
virus_mut_rate = 0.5 # Rate at which the virus mutates
virus_pop = [] # Set of all Virus'
virus_rep_rate = [] # Set of all Reproduction Rates of each Virus

# MUTATION INDEX
mutation_index = initialization.mutation_index(virus_length)
# Evo Alg

gen = 0

# INITIALIZE the virus population
virus_pop = initialization.initialize_virus_population(virus_length, virus_pop_size)

while gen < 10:
    new_virus_pop = [] # population of the new virus

    # MUTATE the virus
    for virus in virus_pop:
        new_virus_pop.append(mutation.virus_mutation(virus, mutation_index, virus_rep_rate))

    gen += 1 # Next Generation
    print(virus_pop)
