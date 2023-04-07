# imports
import global_var as var
import random
# helper functions

# calculates the reproduction rate of a virus
def calculate_virus_reproduction_rate (mut_val):
    return var.virus_base_rep_rate + mut_val

# Find the average virus LP strings of LP array of virus pop
def avg_lp_virus_string (lethal_points):
    average = []
    for i in range(0, var.virus_length):
        count_1 = 0
        count_0 = 0
        for j in lethal_points:
            if j[i]:
                count_1 += 1
            else:
                count_0 += 1
        if count_1 == count_0:
            average.append(random.randint(0,1))
        elif count_1 > count_0:
            average.append(1)
        else:
            average.append(0)

    return average

# Set Virus Threat Value
def set_virus_threat(virus, value):
    virus[var.virus_length+1][0] = value

# Get Virus Threat Value
def get_virus_threat(virus):
    return virus[var.virus_length+1][0]

# Get Virus Lethal Point Strings
def get_virus_lp(virus):
    lp_array = []
    for lp in virus[var.virus_length]:
        lp_array.append(virus[lp])
    return lp_array

# Determine Virus Threat Based on Vaccine
def virus_threaten(virus, vaccine):
    virus_lp = get_virus_lp(virus)
    threat = False
    for lp in virus_lp:
        if lp == vaccine:
            threat = True

    print("threat: ", threat)
    if threat:
        if get_virus_threat(virus):
            # Virus is already threathed from a previous iteration
            print("VIRUS KILLED")
        else:
            # threaten the virus
            set_virus_threat(virus, 1)
    else:
        # reset threat values
        set_virus_threat(virus, 0)
