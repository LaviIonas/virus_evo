import random
import decimal

import global_var as var

def init_human_pop():
    human_pop = []

    for i in range(1, var.human_pop+1):
        human_pop.append(init_human(i))

    return human_pop

def init_human(id):
    human = []

    # What makes up a person in respect to a virus

    # Properties
    # Name
    human.append("H"+str(id))
    # Action; Humans start their journey at home
    human.append('Home')
    # Family Name
    human.append('')
    # Immune System
    human.append([random.randint(0, 100)/100])
    # Relations

    return human

def get_nth_key(dict, n):
    for i, key in enumerate(dict.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")
