# def initialize_virus_tree ():
#     pop = []
#
#     for i in range(var.virus_pop_size):
#         individual = Tree()
#         nodeID = 1
#         parent_nodeID = nodeID
#         individual.create_node([0] * var.virus_length, nodeID) # root node
#         for j in range(var.virus_tree_size):
#             nodeID += 1
#             individual.create_node([0] * var.virus_length, nodeID, parent=parent_nodeID)
#         pop.append(individual)
#     return pop
#
# # INITIALIZE the mutation index for virus genome of length n
# def mutation_index ():
#     # var.virus_length
#     mut_index = []
#     return mut_index
#
# def transform(virus):
#     new = []
#     for node in range(1, var.virus_length + 1):
#         new.append(virus.get_node(node).tag)
#     return new
#
# def virus_tree_mutation(individual):
#     new_individual = random.choices(population=[0, 1], weights=var.mutation_rate, k=len(individual))
#     return new_individual
