# import library

# import files
import initialization
import mutation

# declerations
virus_pop_size = 10 # Number of Virus in Population
virus_length = 6 # Size of the Virus
virus_pop = [] # Set of all Virus'

# Evo Alg

# INITIALIZE the virus population
virus_pop = initialization.initialize_virus_population(virus_length, virus_pop_size)

#
mutation.virus_mutation(virus_pop, virus_pop_size)

print(virus_pop)
