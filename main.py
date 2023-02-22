# import library

# import files
import initialization
import mutation

# declerations
virus_pop_size = 10 # Number of Virus in Population
virus_length = 6 # Size of the Virus
virus_pop = [] # Set of all Virus'
# Evo Alg

gen = 0

# INITIALIZE the virus population
virus_pop = initialization.initialize_virus_population(virus_length, virus_pop_size)
mutation_rate = [0.4, 0.6]
while gen < 10:
    new_virus_pop = [] # population of the new virus

    # MUTATE the virus
    for virus in virus_pop:
        new_virus_pop.append(mutation.virus_mutation(virus, mutation_rate))

    gen += 1 # Next Generation

print(new_virus_pop)
