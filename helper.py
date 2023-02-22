# imports
import global_var as var

# helper functions

# calculates the reproduction rate of a virus
def calculate_virus_reproduction_rate (mut_val):
    return var.virus_base_rep_rate + mut_val
