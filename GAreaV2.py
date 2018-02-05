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
        for j in range(0,len(self.intervals)):
            equation = template
            M = equation.replace('x', str(j + 0.5))
            middle = eval(M)
            total += abs(middle - self.intervals[j])
        self.cost = total

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
        for j in range(5, 10):
            child.intervals[j] = pair.intervals[j]
        return child

    def mutate(self, chance, step):
        if chance > random.uniform(0, 1):
            specific_interval = random.randint(0, 9)
            mutation = random.randint(-step, step)
            self.intervals[specific_interval] += mutation


class Population:

    def __init__(self):
        self.array = []
        for i in range(0,50):
            Riemann = Gene()
            Riemann.rand()
            self.array.append(Riemann)

    def generation(self, template, numgens, step):
        for generations in range(0, numgens):
            print("Generation: " + str(generations))

            for i in range(0, len(self.array)):
                self.array[i].calcCost(template)

            self.array.sort(key=lambda Riemann: Riemann.cost)

            if (self.array[0].cost < step):
                print("Approximate Answer Found")
                print("Area: " + str(self.array[0].calcArea()))
                print("Cost: " + str(self.array[0].cost))
                break

            if (generations % numgens//10):
                print("Area: " + str(self.array[0].calcArea()))
                print("Cost: " + str(self.array[0].cost))

            child1 = self.array[0].mate(self.array[1])
            child2 = self.array[1].mate(self.array[0])

            for i in range(0, len(self.array)/2, 2):
                self.array[i] = child1

            for i in range(1, len(self.array)/2, 2):
                self.array[i] = child2

            for i in range(len(self.array)/2, len(self.array)):
                child3 = Gene()
                child3.rand()
                self.array[i] = child3

            for i in range(0, len(self.array)):
                self.array[i].mutate(0.5, step)

        print("---End Of Approximation---")

    def realAnswer(self, template):
        total = 0
        for i in range(0,10):
            equation = template
            M = equation.replace('x', str(i + 0.5))
            total += eval(M)
        print("The actual midpoint sum is: " + str(total))

print("Welcome to GArea.py!")
print("GArea is a Riemann sum calculator that uses a genetic algorithm to demonstrate how GA's can approximate answers.")
equation = input('Please enter an equation as a string *Proper Syntax Required*: ')
numgens = input('Please enter a generation cap (integer): ')
step = input('Please enter the mutation range: ')
pop = Population()
pop.generation(equation, numgens, step)
pop.realAnswer(equation)