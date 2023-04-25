import copy
import random
import global_var as var
import helper as help

def generate_virus_clones(virus_pop, gen):

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

                help.set_virus_threat(virus_pop[i], 1)

    return clones
