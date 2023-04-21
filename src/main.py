# import library

# import files
import random
from treelib import Tree, Node

import initialization
import global_var as var
import helper as help
import mutation
import fitness
import parent_selection as ps
import natural_selection as ns
import fitness
# declerations

# ---------------
# Evo Alg
# ---------------

# NATURAL SELECTION APPROACH
ns.natural_selection()

Set gen start
gen = 0
gen_max = 5

# INITIALIZE
virus_pop = initialization.initialize_virus_population()
vaccine_pop = initialization.initialize_vaccine_population()

# FITNESS
vaccine_fitness_array = []

virus_lp_nodes = []
for virus in virus_pop:
    virus_lp_nodes.append(help.get_virus_lp(virus))

for vaccine in vaccine_pop:
    vaccine_fitness_array.append(fitness.vaccine_fitness(virus_lp_nodes, vaccine))

# PRINT
help.init_tree(virus_pop)
print("Generation ZERO")
# print(vaccine_fitness_array)
help.print_virus_readable(virus_pop)
print("VACCINE", vaccine_pop)
var.tree.show()

# GENERATIONAL LOOP
while gen < gen_max:
    gen += 1
    # VIRUS FITNESS
    virus_fitness_list = help.generate_virus_fitness_list(virus_pop)

    # VIRUS EVOLUTION

    # SELECT PARENTS
    virus_p = []
    p1, p2 = ps.select_parents(virus_pop, virus_fitness_list)
    virus_p.append(p1)
    virus_p.append(p2)

    help.print_virus_readable(virus_p)

    # call cross over (parents)
    # GENERATE OFFSPRING
    # ... n = 2
    offsping = []
    # add offsping to population

    # MUTATION OF POPULATION
    for virus in virus_pop:
        mutation.virus_mutation(virus)
        help.update_virus_virality(virus)

    # VACCINE EVOLUTION

    # PARENT SELECTION
    vaccine_p = []
    p1, p2 = ps.select_parents(vaccine_pop, vaccine_fitness_array)
    vaccine_p.append(p1)
    vaccine_p.append(p2)

    # OFFSPRING

    # MUTATION
    for vaccine in vaccine_pop:
        mutation.vaccine_mutation(vaccine)

    # vaccine_fitness_array = []
    #
    # virus_lp_nodes = []
    # for virus in virus_pop:
    #     virus_lp_nodes.append(help.get_virus_lp(virus))
    #
    # for vaccine in vaccine_pop:
    #     vaccine_fitness_array.append(fitness.vaccine_fitness(virus_lp_nodes, vaccine))
    #
    # print(vaccine_fitness_array)

    # ...
