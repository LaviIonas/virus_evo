def evaluate_fitness(virus, vaccine):
    score = 0
    for i in range(len(virus)):
        if virus[i] == vaccine[i]:
            score += 1
    return score / len(virus)

