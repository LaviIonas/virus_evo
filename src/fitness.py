import global_var as var
import helper as hp


def vaccine_fitness(lp, vaccine):
    score=0
    for p in lp:
        for i in range(0, var.virus_node_length-1):
            if p[i] == vaccine[i]:
                score += 1

    if score == 0:
        return 1
    return score

def virus_fitness(lethal_point):
    score = lethal_point.count(1)
    return score
