import random
import matplotlib.pyplot as plt

import helper as help
import global_var as var
import mutation
import initialization
import fitness
import parent_selection as ps
import recombination
import reproduction

# Set gen start
gen = 0
gen_max = 15

highest = 0

# plot arrays
pop_plot = []
score_plot = []
gen_plot = []

# INITIALIZE
virus_pop = initialization.initialize_virus_population()
vaccine_pop = initialization.initialize_vaccine_population()

vaccine_fitness = []

virus_lp_nodes = []
for virus in virus_pop:
    lp_index = virus[var.virus_length]
    for i in lp_index:
        virus_lp_nodes.append(virus[i])

for vaccine in vaccine_pop:
    vaccine_fitness.append(fitness.vaccine_fitness(virus_lp_nodes, vaccine))


# PRINT
print("Generation ZERO")
# help.print_virus_readable(virus_pop)

# GENERATIONAL LOOP
while gen < gen_max or len(virus_pop) == 0:
    gen += 1

    # parents
    p1, p2 = ps.select_parents(vaccine_pop, vaccine_fitness)
    print(p1, p2)

    # offspring
    offspring = []
    o1, o2 = recombination.crossover(p1, p2)
    offspring.append(o1)
    offspring.append(o2)

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

    clones = reproduction.generate_virus_clones(virus_pop, gen)
    help.virus_pop_clean(virus_pop)

    for clone in clones:
        mutation.virus_mutation(clone)
        mutation.virus_lp_mutation(clone)
        help.update_virus_virality(clone)
        virus_pop.append(clone)

    # MUTATION
    for i in virus_pop:
        mutation.virus_mutation(i)
        mutation.virus_lp_mutation(i)
        help.update_virus_virality(i)

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
    help.print_virus_readable(virus_pop)

l = len(virus_pop)
e = highest / l
print("EFF", e, "POP", l)

plt.show()
