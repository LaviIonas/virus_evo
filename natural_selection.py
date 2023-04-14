import random
import copy
from treelib import Tree, Node

import helper as help
import global_var as var
import mutation
import initialization

def natural_selection():

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

        # VIRUS REPRODUCTION
        # virus has virality rate which determines its potency to replicate
        # each virus has viratility rate chance of making a close with a chance for that clone to mutate
        clones = generate_virus_clones(virus_pop, gen)

        for clone in clones:
            mutation.natural_selection_mutation(clone)
            help.update_virus_virality(clone)
            virus_pop.append(clone)

        # MUTATION
        for i in virus_pop:
            mutation.natural_selection_mutation(i)
            help.update_virus_virality(i)

        # AVG VIRALITY
        avg = help.get_generation_virality_avg(virus_pop)

        # PRINT
        print("Generation: ", gen, "Avg Virality: ", avg)
        help.print_virus_readable(virus_pop)
        var.tree.show()


def generate_virus_clones(virus_pop, gen):
    clones = []
    for i in range(0, len(virus_pop)):
        clone = []
        v_rate = virus_pop[i][var.virus_length+1][2]
        if v_rate > 0:
            # set clone id
            clone = copy.deepcopy(virus_pop[i])
            clone[var.virus_length+1][3] += str(gen)+":"

            # Tree Update
            name = str(clone[var.virus_length+1][3])
            var.tree.create_node(name, name, parent=str(virus_pop[i][var.virus_length+1][3]))

            # add clone
            clones.append(clone)

    return clones
