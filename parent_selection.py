import random
import global_var as var

def generate_virus_clones(virus_pop, gen):
    offspring = []
    for i in range(0, len(virus_pop)):
        clone = []
        v_rate = virus_pop[i][var.virus_length+1][2]
        if v_rate > 0:
            # set clone id
            clone = virus_pop[i]
            clone[var.virus_length+1][3] += str(gen)+str(i)+":"
            # add clone
            offspring.append(clone)

    return offspring
