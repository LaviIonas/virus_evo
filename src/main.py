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
# declerations

# ---------------
# Evo Alg
# ---------------

# NATURAL SELECTION APPROACH
# ns.natural_selection()


# Set gen start
gen = 0
gen_max = 5

# INITIALIZE
virus_pop = initialization.initialize_virus_population()
vaccine_pop = initialization.initialize_vaccine_population()

# FITNESS

# PRINT
help.init_tree(virus_pop)
print("Generation ZERO")
help.print_virus_readable(virus_pop)
var.tree.show()

# GENERATIONAL LOOP
while gen < gen_max:
    gen += 1
    # VIRUS FITNESS
    virus_fitness_list = help.generate_virus_fitness_list(virus_pop)

    # VIRUS EVOLUTION

    # SELECT PARENTS
    parents = []
    p1, p2 = ps.select_parents(virus_pop, virus_fitness_list)
    parents.append(p1)
    parents.append(p2)

    print("PARENTS: ", parents)
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

    # OFFSPRING

    # MUTATION
    for vaccine in vaccine_pop:
        mutation.vaccine_mutation(vaccine)

    # FITNESS



    # ...
