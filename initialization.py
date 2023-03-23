# imports
import numpy as np
from treelib import Tree, Node
import global_var as var
# functions

# INITIALIZE the starting virus population
def initialize_virus_population ():
    

# INITIALIZE the mutation index for virus genome of length n
def mutation_index ():
    # var.virus_length
    mut_index = []
    return mut_index

def initialize_virus_tree ():
    pop = []

    for i in range(var.virus_pop_size):
        individual = Tree()
        nodeID = 1
        parent_nodeID = nodeID
        individual.create_node([0, 0, 0, 0, 0, 0], nodeID) # root node
        for j in range(var.virus_tree_size):
            nodeID += 1
            individual.create_node([0, 0, 0, 0, 0, 0], nodeID, parent=parent_nodeID)
        pop.append(individual)
    return pop
