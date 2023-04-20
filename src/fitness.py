import global_var as var
import helper as hp


def vaccine_fitness(lp, vaccine):
    score=0
    for i in range(len(lp)):
        if lp[i]==vaccine:
            score += 1
    if score == 0:
        return 1
    return score
