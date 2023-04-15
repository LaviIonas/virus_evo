import mutation as mutate
import global_var as var
import parent_selection as ps
import fitness as fy
import initialization as init

for generation in range(var.GENERATIONS):
    # Evaluate the fitness of each virus in the population
    fitness_scores = [fy.evaluate_fitness(virus, init.virus[i]) for i, virus in enumerate(virus_population)]
    
    # Select the parents and generate the offspring for the next generation
    next_generation = []
    for i in range(var.virus_pop_size // 2):
        parent1, parent2 = ps.select_parents(virus_population, fitness_scores)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1, var.virus_mut_rate)
        mutate(child2,var.virus_mut_rate)
        next_generation += [child1, child2]
    
    # Replace the current generation with the next generation
    virus_population = next_generation