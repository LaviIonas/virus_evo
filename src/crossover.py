"""
Usage:  The crossover functions are only usable for those lists with no duplicated elements in it.
To be specific, in our project, we might encode our binary strings to a permutation with no
duplicated elements and then use crossover functions to recombine them. Finally, we decode the permutation
Example:
    Sample use of PMX
    p1 = [0, 1, 0, 1, 1, 1, 1, 0]
    p2 = [1, 1, 0, 1, 1, 0, 1, 0]
    o1, o2, m1, m2 = encoder(p1, p2)
    encoded_offspring, segment = PMX(o1, o2)
    print(encoded_offspring, segment)
    offspring = decoder(encoded_offspring,m1, m2, segment)
    Sample use of order_crossover
    p1 = [0, 1, 0, 1, 1, 1, 1, 0]
    p2 = [1, 1, 0, 1, 1, 0, 1, 0]
    o1, o2, m1, m2 = encoder(p1, p2)
    encoded_offspring, segment = order_crossover(o1, o2)
    print(encoded_offspring, segment)
    offspring = decoder(encoded_offspring,m1, m2, segment)
    sprint(offspring)
"""
# imports
import random

def encoder(p1, p2):
    """
    To encode the permutation, we created two mappings to keep track of their
    original values, and two new encoded parents
    """
    # create 2 mappings
    mapping1, mapping2 = {}, {}
    for i in range(len(p1)):
        mapping1[i] = p1[i]
    for j in reversed(range(len(p2))):
        mapping2[j] = p2[j]

    # encode the parents
    encoded_p1, encoded_p2 = [], []
    for a in mapping1:
        encoded_p1.append(a)
    for b in mapping2:
        encoded_p2.append(b)
    # return the newly encoded parents and their mappings to original values
    return encoded_p1, encoded_p2, mapping1, mapping2

def decoder(offspring, mapping1, mapping2, segment):
    """
    To decode, we used mappings to put the original values back to the
    offspring
    """
    # The first segment is from p1, put values from p1 back to the offspring
    new_offspring = [-10] * len(offspring)
    for i in segment:
        new_offspring[i] = mapping1[i]
    # The remaining values are from p2
    for j in range(len(new_offspring)):
        if new_offspring[j] == -10:
            new_offspring[j] = mapping2[offspring[j]]
    # just return a new offspring
    return new_offspring


def PMX(p1, p2):
    """
    Parameter: 2 permutations of parents
    Return: offspring permutation
    """
    # choose a random segment
    crossover_points = sorted(random.sample(range(len(p1)), 2))
    # copies of segments of 2 parents
    segment1 = p1[crossover_points[0]:crossover_points[1]].copy()
    segment2 = p2[crossover_points[0]:crossover_points[1]].copy()
    # initialize offspring
    offspring = [-10] * len(p1)
    # put the selected segment into offspring
    idx = 0
    for i in range(crossover_points[0], crossover_points[1]):
        offspring[i] = segment1[idx]
        idx += 1
    # create mappings
    mapping = {p2[i]: p1[i] for i in range(crossover_points[0], crossover_points[1])}
    # put the elements outside the segment into offspring
    for idx, elem in enumerate(p2):
        if elem not in offspring and elem not in segment2:
            offspring[idx] = elem
    # put the remaining elements into offspring
    for i in mapping:
        if i not in segment1:
            pos = p2.index(mapping[i])
            while offspring[pos] != -10 and p2[pos] in mapping:
                pos = p2.index(mapping[p2[pos]])
            else:
                offspring[pos] = i
    return offspring, segment1


"""
PMX test
p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
print(PMX(p1, p2))
"""

def order_crossover(p1, p2):
    """
    Parameter: 2 permutations of parents
    Return: offspring permutation
    """
    # choose a random segment
    crossover_points = [3, 7]
    # create a segment from p1
    segment = p1[crossover_points[0]:crossover_points[1]].copy()
    # initialize offspring
    offspring = [0] * len(p1)
    # put the selected segment into offspring
    idx = 0
    for i in range(crossover_points[0], crossover_points[1]):
        offspring[i] = segment[idx]
        idx += 1

    # create a crossover set with the remaining elements in order
    index = crossover_points[1]
    xover_set = []
    for _ in range(len(p1)):
        if p2[index] not in segment:
            xover_set.append(p2[index])
        if index != len(p1) - 1:
            index += 1
        else:
            index = 0

    # add the elements from crossover set into offspring
    start = crossover_points[1]
    for e in xover_set:
        offspring[start] = e
        if start != len(p1) - 1:
            start += 1
        else:
            start = 0
    return offspring, segment

"""
p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
print(order_crossover(p1, p2))
"""

"""
Sample use of PMX
p1 = [0, 1, 0, 1, 1, 1, 1, 0]
p2 = [1, 1, 0, 1, 1, 0, 1, 0]
o1, o2, m1, m2 = encoder(p1, p2)
encoded_offspring, segment = PMX(o1, o2)
print(encoded_offspring, segment)
offspring = decoder(encoded_offspring,m1, m2, segment)
"""

"""
Sample use of order_crossover
p1 = [0, 1, 0, 1, 1, 1, 1, 0]
p2 = [1, 1, 0, 1, 1, 0, 1, 0]
o1, o2, m1, m2 = encoder(p1, p2)s
encoded_offspring, segment = order_crossover(o1, o2)
print(encoded_offspring, segment)
offspring = decoder(encoded_offspring,m1, m2, segment)
print(offspring)
"""
