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
help.init_tree(virus_pop)

# PRINT
print("Generation ZERO")
help.print_virus_readable(virus_pop)
var.tree.show()

# GENERATIONAL LOOP
while gen < gen_max:
    gen += 1

    

    # MUTATION
    for i in virus_pop:
        mutation.natural_selection_mutation(i)
        help.update_virus_virality(i)
