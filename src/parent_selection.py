import random
import global_var as var


def select_parents(virus_pop, fitness_scores):
    total_fitness = sum(fitness_scores)
    selection_probs = [score / total_fitness for score in fitness_scores]
    parent1 = random.choices(virus_pop, weights=selection_probs)[0]
    parent2 = random.choices(virus_pop, weights=selection_probs)[0]
    return parent1, parent2
