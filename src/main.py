# import library

# import files
import random
from treelib import Tree, Node

import initialization
import global_var as var
import helper as help
import mutation
import fitness
import parent_selection
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
var.vaccine = initialization.initialize_vaccine()

# PRINT
help.init_tree(virus_pop)
print("Generation ZERO")
help.print_virus_readable(virus_pop)
var.tree.show()

# GENERATIONAL LOOP
while gen < gen_max:
    gen += 1

    # VIRUS EVOLUTION

    # SELECT PARENTS
    # ... n = 2
    parents = []
    # call cross over (parents)
    # GENERATE OFFSPRING
    # ... n = 2
    offsping = []
    # add offsping to population

    # MUTATION OF POPULATION
    for i in virus_pop:
        mutation.natural_selection_mutation(i)
        help.update_virus_virality(i)

    # VACCINE EVOLUTION

    # ...
