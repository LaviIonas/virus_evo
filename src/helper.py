# imports
import global_var as var
import random
from treelib import Tree, Node

# helper functions

# calculates the reproduction rate of a virus
def calculate_virus_reproduction_rate (mut_val):
    return var.virus_base_rep_rate + mut_val

# Find the average virus LP strings of LP array of virus pop
def avg_lp_virus_string (lethal_points):
    average = []
    for i in range(0, var.virus_node_length):
        a, b = 0, 0
        for j in lethal_points[0]:
            if j[i]:
                a += 1
            else:
                b += 1
        if a == b:
            average.append(random.randint(0,1))
        elif a > b:
            average.append(1)
        else:
            average.append(0)

    return average

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

# # Get Virus Lethal Point Strings
# def get_virus_lp(virus):
#     lp_array = []
#     for lp in virus[var.virus_length]:
#         lp_array.append(virus[lp])
#     return lp_array

# Determine Virus Threat Based on Vaccine
def virus_threat_check(virus_pop, virus):
    virus_lp = get_virus_lp(virus)
    threat = False
    for lp in virus_lp:
        if lp == var.vaccine:
            threat = True

    if threat:
        if get_virus_threat(virus):
            current_id = str(virus[var.virus_length+1][3])
            # Virus is already threathed from a previous iteration
            # Mark to Kill Virus
            set_virus_threat(virus, -1)

            # Tree Restructure
            var.tree.link_past_node(current_id)

        else:
            # threaten the virus
            set_virus_threat(virus, 1)
    else:
        # reset threat values
        set_virus_threat(virus, 0)

# remove all empty lists from virus pop
def virus_pop_clean(virus_pop):
    del_index = []
    for i in range(0, len(virus_pop)):
        if virus_pop[i][var.virus_length+1][0] == 1:
            current_id = str(virus_pop[i][var.virus_length+1][3])
            var.tree.link_past_node(current_id)
            del_index.append(i)

    for index in sorted(del_index, reverse=True):
        del virus_pop[index]

def print_virus_readable(virus_pop):
    for i in range(0, len(virus_pop)):
        print("V", virus_pop[i][var.virus_length+1][3], "=> Threat:", virus_pop[i][var.virus_length+1][0], ", Virality:", virus_pop[i][var.virus_length+1][2])

def get_generation_virality_avg(virus_pop):
    avg = 0
    for v in virus_pop:
        avg += v[var.virus_length+1][2]

    return avg / len(virus_pop)

def generate_virus_fitness_list(virus_pop):
    fit_list = []
    for v in virus_pop:
        fit_list.append(v[var.virus_length+1][2])
    return fit_list

# Set the array value of the vaccine
def set_vaccine(vaccine):
    var.vaccine = vaccine

def update_virus_virality(virus):
    mut_val = virus[var.virus_length+2]
    sum = 0
    for i in mut_val:
        sum += i
    virus[var.virus_length+1][2] = sum


# TREE HELPER
def init_tree(virus_pop):
    var.tree.create_node("ROOT", "root")

    for v in virus_pop:
        id = v[var.virus_length+1][3]
        var.tree.create_node(id, id, parent="root")
