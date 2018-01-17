import random
import math


class Gene:

    def __init__(self):
        self.cost = 9999
        self.intervals = []

    def rand(self):
        n = 0
        while n < 10:
            self.intervals.append(random.randint(-100, 100))
            n += 1

    def calcCost(self, template):
        total = 0
        j = 1
        while j < len(self.intervals):
            equation = template
            L = equation.replace('x', str(j - 1))
            R = equation.replace('x', str(j))
            left = eval(L)
            right = eval(R)
            total += (math.fabs(left - self.intervals[j-1]) + math.fabs(right - self.intervals[j]))
            #total += (left - self.intervals[int(j)])**2 + (right - self.intervals[int(j)])**2
            self.cost = total
            j += 1

    def calcArea(self):
        total = 0
        for i in range(0, len(self.intervals)):
            total += self.intervals[i] * 1
        return total

    def mate(self, pair):
        child = Gene()
        child.rand()
        for i in range(0, 5):
            child.intervals[i] = self.intervals[i]
        for i in range(5, 10):
            child.intervals[i] = pair.intervals[i]
        return child

    def mutate(self, chance):
        if chance > random.uniform(0, 1):
            specific_interval = random.randint(0, 9)
            mutation = random.randint(-10, 10)
            self.intervals[specific_interval] += mutation


class Population:

    def __init__(self):
        self.array = []
        i = 10
        while i > 0:
            Riemann = Gene()
            Riemann.rand()
            self.array.append(Riemann)
            i -= 1

    def generation(self, template):
        generations = 0
        while generations < 1000000:
            generations += 1
            print("Generation: " + str(generations))

            for i in range(0, len(self.array)):
                self.array[i].calcCost(template)

            self.array.sort(key=lambda Riemann: Riemann.cost)

            print("Area: " + str(self.array[0].calcArea()))
            print("Cost: " + str(self.array[0].cost))

            child1 = self.array[0].mate(self.array[1])
            child2 = self.array[1].mate(self.array[0])

            for i in range(0, len(self.array), 2):
                self.array[i] = child1

            for i in range(1, len(self.array), 2):
                self.array[i] = child2

            for i in range(0, len(self.array)):
                self.array[i].mutate(0.9)

        print("Generation Cap Reached")

print("Welcome to the GArea!")
print("GArea is a Riemann sum calculator that uses genetic algorithms to calculate.")
equation = input('Please enter an equation *Syntax Required* :')
pop = Population()
pop.generation(equation)