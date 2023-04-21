import random
import global_var as var


def select_parents(vaccine_pop, fitness_scores):
    total_fitness = sum(fitness_scores)
    selection_probs = [score / total_fitness for score in fitness_scores]
    parent1 = random.choices(vaccine_pop, weights=selection_probs)[0]
    parent2 = random.choices(vaccine_pop, weights=selection_probs)[0]
    return parent1, parent2

# tournament selection
def selection(pop, scores, k=4):
 # first random selection
 selection_ix = randint(len(pop))
 for ix in randint(0, len(pop), k-1):
     # check if better (e.g. perform a tournament)
     if scores[ix] < scores[selection_ix]:
     selection_ix = ix
 return pop[selection_ix]
