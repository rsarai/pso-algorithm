import math
import abc


class Problem():
    dimensions = 0
    lower_bound = -100
    upper_bound = 100

    @abc.abstractmethod
    def evaluate_solution(self, position_list):
        pass


class Sphere(Problem):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.lower_bound = -100
        self.upper_bound = 100

    def evaluate_solution(self, position_list):
        solution = 0
        for i in range(0, len(position_list)):
            solution += position_list[i] ** 2
        return solution


class Rastrigin(Problem):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.lower_bound = -5.12
        self.upper_bound = 5.12

    def evaluate_solution(self, position_list):
        solution = 0
        for i in range(0, len(position_list)):
            solution += (position_list[i] ** 2 + 10 - 10*math.cos(2*math.pi*position_list[i]))
        return solution


class Rosenbrocks(Problem):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.lower_bound = -30
        self.upper_bound = 30

    def evaluate_solution(self, position_list):
        solution = 0
        for i in range(0, len(position_list) - 1):
            solution += 100 * ((position_list[i] ** 2 - position_list[i + 1]) ** 2) + ((position_list[i] - 1) ** 2)
        return solution
