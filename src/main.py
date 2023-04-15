# import library

# import files
import random
import copy
from treelib import Tree, Node

import initialization
import global_var as var
import helper as help
import mutation
import fitness
import parent_selection
import natural_selection as ns
import human_population as hp
# declerations

# ---------------
# Evo Alg
# ---------------

# NATURAL SELECTION APPROACH
# ns.natural_selection()

human_pop = hp.init_human_pop()
print(human_pop)


for i in range(0, human_pop/human_cluster):


day = 0
max_day = 4

while day < max_day:
    # Human takes action
    for human in human_pop:
        n = random.randint(0,3)
        action = hp.get_nth_key(var.human_actions, n)
        human[1] = action

    print(human_pop)

    day += 1
