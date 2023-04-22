import random
import copy
from treelib import Tree, Node
import matplotlib.pyplot as plt

import helper as help
import global_var as var
import mutation
import initialization
import crossover
import fitness
import parent_selection as ps

def natural_selection():

    # Set gen start
    gen = 0
    gen_max = 15

    highest = 0
    z = 0

    pop_plot = []
    score_plot = []
    gen_plot = []

    # INITIALIZE
    virus_pop = initialization.initialize_virus_population()
    vaccine_pop = initialization.initialize_vaccine_population2()

    # virus_fitness = []
    vaccine_fitness = []

    virus_lp_nodes = []
    for virus in virus_pop:
        lp_index = virus[var.virus_length]
        for i in lp_index:
            virus_lp_nodes.append(virus[i])

    for vaccine in vaccine_pop:
        vaccine_fitness.append(fitness.vaccine_fitness(virus_lp_nodes, vaccine))

    # for lp in virus_lp_nodes:
    #     virus_fitness.append(fitness.virus_fitness(lp))
    help.init_tree(virus_pop)
    # PRINT
    print("Generation ZERO")
    help.print_virus_readable(virus_pop)
    var.tree.show()

    # GENERATIONAL LOOP
    while gen < gen_max or len(virus_pop) == 0:
        gen += 1

        # VACCINE

        # lp_array = []
        # for virus in virus_pop:
        #     lp_array.append(help.get_virus_lp(virus))
        # vac = help.avg_lp_virus_string(lp_array)
        # help.set_vaccine(vac)

        # parent
        p1, p2 = ps.select_parents(vaccine_pop, vaccine_fitness)
        print(p1, p2)
        # p1 = ps.selection(vaccine_pop, vaccine_fitness, k=4)

        # offspring
        offspring = []
        o1, o2 = crossover(p1, p2)
        offspring.append(o1)
        offspring.append(o2)

        # c = []
        # clone1 = copy.deepcopy(p1)
        # clone2 = copy.deepcopy(p2)
        # c.append(clone1)
        # c.append(clone2)
        #
        # for i in c:
        #     mutation.vaccine_mutation(i)
        #     vaccine_pop.append(i)

        # Vaccine Mutate Child
        for child in offspring:
            mutation.vaccine_mutation(child)
            vaccine_pop.append(child)

        # calculates fitness
        vaccine_fitness = [0]*len(vaccine_pop)
        array = []

        for virus in virus_pop:
            lp_index = virus[var.virus_length]
            for i in range(0, len(vaccine_pop)):
                match = False
                for lp in lp_index:
                    if vaccine_pop[i] == virus[lp]:
                        match = True
                if match:
                    vaccine_fitness[i] += 1
                else:
                    vaccine_fitness[i] += 0.001

        # virus_lp_nodes = []
        # for virus in virus_pop:
        #     lp_index = virus[var.virus_length]
        #     for i in lp_index:
        #         virus_lp_nodes.append(virus[i])
        #
        # score = 0
        # for vaccine in vaccine_pop:
        #     score += fitness.vaccine_fitness(virus_lp_nodes, vaccine)
        #     vaccine_fitness.append(score)

        # for lp in virus_lp_nodes:
        #     virus_fitness.append(fitness.virus_fitness(lp))
        # lowest = 1000000
        # index_a = []
        # for i in range(1):
        #     index = 0
        #     for v in range(0, len(vaccine_fitness)):
        #         if vaccine_fitness[v] < lowest:
        #             index = v
        #             lowest = vaccine_fitness[v]
        #     index_a.append(index)
        #
        # for i in index_a:
        #     del vaccine_pop[i]
        #     del vaccine_fitness[i]

        # print(vaccine_fitness)
        # simulate

        # print(vaccine_pop)

        # VIRUS THREAT
        # for virus in virus_pop:
        #     help.virus_threat_check(virus_pop, virus)
        #
        # help.virus_pop_clean(virus_pop)

        # VIRUS REPRODUCTION
        # virus has virality rate which determines its potency to replicate
        # each virus has viratility rate chance of making a close with a chance for that clone to mutate
        z = 0
        # print(z)
        clones = generate_virus_clones(virus_pop, gen, z)
        help.virus_pop_clean(virus_pop)

        # print(clones)

        # clones = generate_virus_clones_highest(virus_pop, gen)

        for clone in clones:
            mutation.natural_selection_mutation(clone)
            mutation.virus_lp_mutation(clone)
            help.update_virus_virality(clone)
            virus_pop.append(clone)

        # MUTATION
        for i in virus_pop:
            mutation.natural_selection_mutation(i)
            mutation.virus_lp_mutation(i)
            help.update_virus_virality(i)


        # AVG VIRALITY
        # avg = help.get_generation_virality_avg(virus_pop)

        # PRINT

        highest = 0
        for vaccine in vaccine_pop:
            score = help.sim_vaccine(virus_pop, vaccine)
            if score > highest:
                highest = score


        score_plot.append(highest)
        gen_plot.append(gen)
        pop_plot.append(len(virus_pop))
        plt.xlabel("gen")
        plt.plot(gen_plot, pop_plot)
        plt.plot(gen_plot, score_plot)


        print("Generation: ", gen, "Vac Score: ", highest, "Population: ", len(virus_pop), "eff:", highest/len(virus_pop))
        # help.print_virus_readable(virus_pop)
        # var.tree.show()



    l = len(virus_pop)
    e = highest / l
    print("EFF", e, "POP", l)
    # return highest, l, e
    plt.show()


def generate_virus_clones(virus_pop, gen, z):

    clones = []
    for i in range(0, len(virus_pop)):
        clone = []
        v_rate = virus_pop[i][var.virus_length+1][2]
        lp_num = len(virus_pop[i][var.virus_length])

        if v_rate > 0:
            # set clone id
            for j in range(random.randint(0,lp_num)):
                clone = copy.deepcopy(virus_pop[i])
                clone[var.virus_length+1][3] += "-"+str(gen)+":"+str(j)
                clones.append(clone)

                name = str(clone[var.virus_length+1][3])
                var.tree.create_node(name, name, parent=str(virus_pop[i][var.virus_length+1][3]))

                help.set_virus_threat(virus_pop[i], 1)

            # Tree Update

            # add clone

        # if v_rate > z:
        #     for j in range(0,2):
        #         clone = copy.deepcopy(virus_pop[i])
        #         clone[var.virus_length+1][3] += str(gen)+"-"+str(j)+":"
        #         clones.append(clone)
        #         # Tree Update
        #         name = str(clone[var.virus_length+1][3])
        #         # var.tree.create_node(name, name, parent=str(virus_pop[i][var.virus_length+1][3]))
        #
        #     help.set_virus_threat(virus_pop[i], 1)

    return clones

def generate_virus_clones_highest(virus_pop, gen):

    # determine the highest virus
    top_v = []
    highest = 0
    for virus in virus_pop:
        val = virus[var.virus_length+1][2]
        if val >= highest:
            top_v = virus

    clones = []

    for i in range(0, 2):
        clone = copy.deepcopy(top_v)
        clone[var.virus_length+1][3] += " "+str(gen)+":"+str(i)

        name = str(clone[var.virus_length+1][3])
        # var.tree.create_node(name, name, parent=str(top_v[var.virus_length+1][3]))
        clones.append(clone)


    return clones

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2
