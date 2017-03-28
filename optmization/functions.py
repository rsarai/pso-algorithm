import math
from abc import ABC, abstractmethod


class Function(ABC):
	upper_board = 0
	lower_board = 0

	@abstractmethod
	def calculate_fitness(self, position):
		pass


class Sphere(Function):
	upper_board = 100
	lower_board = -100

	def calculate_fitness(self, position_list):
		solution = 0
		for position in position_list:
			solution += position ** 2
		return solution


class Rastrigin(Function):
	upper_board = 5.12
	lower_board = -5.12

	def calculate_fitness(self, position_list):
		solution = 0
		for position in position_list:
			solution += (position ** 2 + 10 - 10 * math.cos(2 * math.pi * position))
		return solution


class Rosenbrocks(Function):
	upper_board = 30
	lower_board = -30

	def calculate_fitness(self, position_list):
		solution = 0
		for i in range(0, len(position_list) - 1):
            solution += 100 * ((position_list[i] ** 2 - position_list[i + 1]) ** 2) + ((position_list[i] - 1) ** 2)
		return solution
