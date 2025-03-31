city_pop = {'A':9765,'B':3441,'C':2954,'D':1531}

def urban(x):
    population = tuple(i for i in x.values())
    def max_pop():
        i = population[0]
        for n in population:
            if i < n:
                i = n
        return i
    def min_pop():
        i = population[0]
        for n in population:
            if n > i:
                n = i
        return n
    def different():
        return max_pop() - min_pop()
    def average_pop():
        return sum(population)/len(population)
    return max_pop, min_pop, different, average_pop

max1, min1, dif, avg = urban(city_pop)
print(max1())
print(min1())
print(dif())
print(avg())