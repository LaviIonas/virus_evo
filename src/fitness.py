import global_var as var
import helper as hp


def vaccine_fitness(lp):

    score=0
    for i in range(len(lp)):
        if lp[i]==var.vaccine:
            score += 1
    return score
