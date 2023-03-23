# imports
import global_var as var
import treelib
# helper functions

# calculates the reproduction rate of a virus
def calculate_virus_reproduction_rate (mut_val):
    return var.virus_base_rep_rate + mut_val

def transform(virus):
    new = []
    for node in range(1, var.virus_length + 1):
        new.append(virus.get_node(node).tag)
    return new
