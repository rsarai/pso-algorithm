import math


def sphere_function(position_list):
    fitness = 0
    for i in range(0, len(position_list)):
        fitness += position_list[i] ** 2
    return fitness


def rastrigin_function(position_list):
    fitness = 0
    for i in range(0, len(position_list)):
        fitness += (position_list[i] ** 2 + 10 - 10*math.cos(2*math.pi*position_list[i]))
    return fitness


def rosenbrocks_function(position_list):
    fitness = 0
    for i in range(0, len(position_list) - 1):
        fitness += 100 * ((position_list[i] ** 2 - position_list[i + 1]) ** 2) + ((position_list[i] - 1) ** 2)
    return fitness


def ackley_function(position_list):
    fitness = 0
    for i in range(0, len(position_list) - 1):
        part_1 = - 0.2 * math.sqrt(0.5 * (position_list[i] * position_list[i] + position_list[i + 1] * position_list[i + 1]))
        part_2 = 0.5 * (math.cos(2 * math.pi * position_list[i]) + math.cos(2 * math.pi * position_list[i + 1]))
        value_point = math.exp(1) + 20 - 20 * math.exp(part_1) - math.exp(part_2)

        fitness += value_point

    return fitness
