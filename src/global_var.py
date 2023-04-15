from treelib import Tree, Node

# Declare Variables

# INITIALIZATION
virus_pop_size = 4 # Number of Virus in Population
virus_length = 8 # Size of the Virus
virus_node_length = 8 # Size of each Virus Node
vaccine = []

#RANDOM
a,b = -1, 1

# MUTATION
virus_mut_rate = 0.15 # Rate at which the virus mutates

# PARENT SELECTION


# TREE REPRESENTATION
tree = Tree()

# EFFICIENCY VARIABLES
v_num = virus_pop_size
v_kill = 0

# HUMAN POP
human_cluster = 4
human_pop = 4*human_cluster

human_actions = {'Home': 0.25, 'Public': 0.25, 'Friends': 0.25, 'Family': 0.25}
