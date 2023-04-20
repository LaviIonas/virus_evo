import global_var as var
import helper as hp


def vaccine_fitness(hp.LP,hp.vaccine):
    score=0
    for i in range(len(hp.LP)):
        if hp.LP[i]==hp.vaccine[i]:
            score += 1
    return score