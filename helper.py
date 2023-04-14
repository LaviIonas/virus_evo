# imports
import global_var as var
# helper functions

# calculates the reproduction rate of a virus
def calculate_virus_reproduction_rate (mut_val):
    return var.virus_base_rep_rate + mut_val

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

def LP_get(individual):
    """
        Get LP of an individual
        :param binary string virus individual
        :return: Its LP list
        """
    return individual[var.virus_length]

def LP_set(individual, lp):
    """
        Set LP for an individual
        :param binary string virus individual
        :return: None
        """
    individual[var.virus_length] = lp
