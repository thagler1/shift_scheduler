#genetic algorithm
import numpy, random, itertools
#/todo currently this is not a callable function
#these values change based on situation
qualified_controllers = 10
days_to_cover =4
population = 5


gen1 = [numpy.random.randint(1,qualified_controllers+1, size=days_to_cover).tolist() for i in range(5)]


def genOffspring(generation):
    offspring = []
    gen2 = set([])
    total = len(generation)
    print("Total : " + str(total))
    for father in generation:
        for mother in generation:
            offspring.append(father + mother)
    for child in offspring:
        gen2.update(list(itertools.permutations(child, len(generation[0]))))
    return gen2
