# import
import initialization
import mutation

# declerations
virus_pop_size = 10
virus_length = 6

# EA
virus_pop = initialization.initialize_virus_population(virus_length, virus_pop_size)
mutation.virus_mutation(virus_pop, virus_pop_size)

print(virus_pop)
