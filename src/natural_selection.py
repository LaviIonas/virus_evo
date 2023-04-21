import random
import copy
from treelib import Tree, Node
import matplotlib.pyplot as plt

import helper as help
import global_var as var
import mutation
import initialization

def natural_selection():

    # Set gen start
    gen = 0
    gen_max = 20

    x_plot = []
    y_plot = []

    # INITIALIZE
    virus_pop = initialization.initialize_virus_population()
    var.vaccine = initialization.initialize_vaccine()

    help.init_tree(virus_pop)
    # PRINT
    print("Generation ZERO")
    help.print_virus_readable(virus_pop)
    var.tree.show()

    # GENERATIONAL LOOP
    while gen < gen_max or len(virus_pop) == 0:
        gen += 1

        # VACCINE
        if gen > 5:
            lp_array = []
            for virus in virus_pop:
                lp_array.append(help.get_virus_lp(virus))
            vac = help.avg_lp_virus_string(lp_array)
            help.set_vaccine(vac)

            # Vaccine Mutation
            mutation.vaccine_mutation(var.vaccine)
            print(var.vaccine)

            # VIRUS THREAT
            for virus in virus_pop:
                help.virus_threat_check(virus_pop, virus)

            help.virus_pop_clean(virus_pop)

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


        #  CLONE WITH HIGHEST
        
        # AVG VIRALITY
        # avg = help.get_generation_virality_avg(virus_pop)

        # PRINT

        x_plot.append(gen)
        y_plot.append(len(virus_pop))
        plt.plot(x_plot, y_plot)

        print("Generation: ", gen, "Avg Virality: ", 0, "Vac Eff: ")
        help.print_virus_readable(virus_pop)
        var.tree.show()


    plt.show()


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
