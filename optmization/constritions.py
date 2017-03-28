from abc import ABC, abstractmethod
from constants import iteration_number


class ConstrictionFactor(ABC):
	c1 = 2.05
	c2 = 2.05

	@abstractmethod
	def calculate_velocity(
		self, velocity, random1, random2, position, position_global_best, position_personal_best):
		pass

	def calculate_velocity_with_inertia(
		self, inertia, velocity, random1, random2, position, position_global_best, position_personal_best):
		return inertia * velocity + self.c1 * random1 * (
			position_personal_best - position
		) + self.c2 * random2 * (position_global_best - position)


class FixedInertia(ConstrictionFactor):
	inertia = 0.8

	def calculate_velocity_with_inertia(
		self, velocity, random1, random2, position, position_global_best, position_personal_best):
		return self.calculate_velocity_with_inertia(
			self.inertia, velocity, random1, random2, position, position_global_best, position_personal_best
		)


class FloatingInertia(ConstrictionFactor):
	inertia = 0.9

	def calculate_velocity_with_inertia(
		self, velocity, random1, random2, position, position_global_best, position_personal_best):
		return self.calculate_velocity_with_inertia(
			self.inertia, velocity, random1, random2, position, position_global_best, position_personal_best
		)

	def update_inertia(self):
		self.inertia -= (0.9 - 0.4) / iteration_number


def ClercConstriction(ConstrictionFactor):
	phi = self.c1 + self.c2
	c = 2 / abs((2 - Phi - (Phi * Phi - 4 * Phi) ** 0.5))

	def calculate_velocity_with_inertia(
		self, velocity, random1, random2, position, position_global_best, position_personal_best):
        return (c * self.calculate_velocity(
        	1, velocity, random1, random2, position, positionGlobalBest, positionPersonalBest)
       	)