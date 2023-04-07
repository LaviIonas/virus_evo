# import library

# import files
import random

import initialization
import global_var as var
import helper as help
import mutation

# declerations
virus_rep_rate = []  # Set of all Reproduction Rates of each Virus

# ---------------
# Evo Alg
# ---------------

# Set gen start
gen = 0
gen_max = 10

# INITIALIZE the virus population

virus_pop = initialization.initialize_virus_population()
vaccine = initialization.initialize_vaccine()




# # THREAT VIRUS TEST
# virus1 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 4, 3], [1]]
# vaccine1 = [0,1,0,0,0,0,0,0]
#
# help.virus_threaten(virus1, vaccine1)
# print(virus1)

# # TEST get virus LP
# array = help.get_virus_lp(virus_pop[0])
# print(array)


# #TEST GET SET OF VIRUS THREAT
# print(virus_pop[0])
# help.set_virus_threat(virus_pop[0], 1)
# threat1 = help.get_virus_threat(virus_pop[0])
# print(threat1)
# help.set_virus_threat(virus_pop[0], 0)
# threat1 = help.get_virus_threat(virus_pop[0])
# print(threat1)

# # TEST LETHAL POINT AVG
# LP_list = []
# for x in range(10):
#     temp = []
#     for i in range(8):
#         temp.append(random.randint(0,1))
#     LP_list.append(temp)
#
# for i in LP_list:
#     print(i)
# avg = help.avg_lp_virus_string(LP_list)
# print("AVERAGE: ", avg)

# # TEST VACCINE INIT
# print(virus_pop)
# print("VACCINE INIT : ", vaccine)


# for i in range(len(virus_pop)):
#     for j in range(len(virus_pop[i])):
#         virus_pop[i][j + 1].tag = mutation.virus_mutation(virus_pop[i][j + 1].tag)
# virus_pop[i].show()
