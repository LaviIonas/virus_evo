# imports
import global_var as var
import random

# helper functions

def sim_vaccine(virus_pop, vaccine):
    score = 0

    for virus in virus_pop:
        lp_index = virus[var.virus_length]
        match = False
        for lp in lp_index:
            if vaccine == virus[lp]:
                match = True
        if match:
            score += 1

    return score

# Set Virus Threat Value
def set_virus_threat(virus, value):
    virus[var.virus_length+1][0] = value

# Get Virus Threat Value
def get_virus_threat(virus):
    return virus[var.virus_length+1][0]

# remove all empty lists from virus pop
def virus_pop_clean(virus_pop):
    del_index = []
    for i in range(0, len(virus_pop)):
        if virus_pop[i][var.virus_length+1][0] == 1:
            current_id = str(virus_pop[i][var.virus_length+1][3])
            del_index.append(i)

    for index in sorted(del_index, reverse=True):
        del virus_pop[index]

def print_virus_readable(virus_pop):
    for i in range(0, len(virus_pop)):
        print("V", virus_pop[i][var.virus_length+1][3], "=> Threat:", virus_pop[i][var.virus_length+1][0], ", Virality:", virus_pop[i][var.virus_length+1][2])

def update_virus_virality(virus):
    mut_val = virus[var.virus_length+2]
    sum = 0
    for i in mut_val:
        sum += i
    virus[var.virus_length+1][2] = sum
