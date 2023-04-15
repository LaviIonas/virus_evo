import random
import global_var as var


def select_parents(var.virus_pop_size, fitness_scores):
    total_fitness = sum(fitness_scores)
    selection_probs = [score / total_fitness for score in fitness_scores]
    parent1 = random.choices(var.virus_pop_size, weights=selection_probs)[0]
    parent2 = random.choices(var.virus_pop_size, weights=selection_probs)[0]
    return parent1, parent2

