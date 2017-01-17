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
        for i in range(5, 100, 10):
            equation = template
            L = equation.replace('x', str(self.intervals[i - 5]))
            R = equation.replace('x', str(self.intervals[i + 5]))
            left = eval(L)
            right = eval(R)
            self.cost += (left - self.intervals[i])**2 + (right - self.intervals[i]**2)

    def mate(self, pair):
        pivot = math.floor(len(self.intervals)/2)
        