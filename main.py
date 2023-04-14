# import library

# import files
import random

import initialization
import global_var as var
import helper as help
import mutation
import fitness
import parent_selection

# declerations

# ---------------
# Evo Alg
# ---------------

# Set gen start
gen = 0
gen_max = 3

# INITIALIZE
virus_pop = initialization.initialize_virus_population()
var.vaccine = initialization.initialize_vaccine()

# help.init_tree(virus_pop)

# FITNESS
# evaluate fitness of the populations
# fitness.update_fitness(virus_pop)
print("Generation ZERO")
help.print_virus_readable(virus_pop)


# GENERATIONAL LOOP
while gen < gen_max:

    # VIRUS REPRODUCTION
    # virus has virality rate which determines its potency to replicate
    # each virus has viratility rate chance of making a close with a chance for that clone to mutate

    offspring = parent_selection.generate_virus_clones(virus_pop, gen)

    for clone in offspring:
        mutation.virus_node_mutation(clone)
        help.update_virus_virality(clone)
        virus_pop.append(clone)

    for i in virus_pop:
        mutation.virus_node_mutation(i)
        help.update_virus_virality(i)

    # FITNESS

    gen += 1
    # print(virus_pop)
    avg = help.get_generation_virality_avg(virus_pop)
    print("Generation: ", gen, "Avg Virality: ", avg)
    help.print_virus_readable(virus_pop)

# PRINT BEST SOLUTION

# for i in range(len(virus_pop)):
#     for j in range(len(virus_pop[i])):
#         virus_pop[i][j + 1].tag = mutation.virus_mutation(virus_pop[i][j + 1].tag)
# virus_pop[i].show()
