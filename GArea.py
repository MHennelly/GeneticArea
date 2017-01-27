import random
import math


class Gene:

    def __init__(self):
        self.cost = 9999
        self.intervals = []

    def rand(self):
        n = 10
        while (n > 0):
            self.intervals.append(random.randint(-1000, 1000))
            n -= 1

    def calcCost(self, template):
        self.cost = 0
        for i in range(1, 10):
            equation = template
            L = equation.replace('x', str(i - 0.5))
            R = equation.replace('x', str(i + 0.5))
            left, right = 0, 0
            left += eval(L)
            right += eval(R)
            self.cost += (math.fabs(left - self.intervals[i])) + math.fabs((right - self.intervals[i]))

    def mate(self, pair):
        child1, child2 = Gene()
        child1.rand()
        child2.rand()
        for i in range(0, 5):
            child1.intervals[i] = self.intervals[i]
            child2.intervals[i] = pair.intervals[i]
        for i in range(6, 10):
            child1.intervals[i] = pair.intervals[i]
            child2.intervals[i] = self.intervals[i]
        return child1, child2

    def mutate(self, chance):
        if chance > random.uniform(0,1):
            square = random.randrange(0, 10)
            mutation = random.randrange(-1, 1)
            self.intervals[square] += mutation
        else:
            return

def compare(a):
    return a.cost


class Population:

    def __init__(self):
        self.array = []
        i = 20
        while (i > 0):
            Riemann = Gene()
            Riemann.rand()
            self.array.append(Riemann)
            i -= 1

    def sort(self):
        self.array.sort(key=compare(Gene))

    def print(self):
        for i in range(0,20):
            print(self.array[i].cost)


equation = input('Please enter an equation *Syntax Required* :')
pop = Population()
for i in range(0, 20):
    pop.array[i].calcCost(equation)
pop.print()