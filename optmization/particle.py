import random
from abc import ABC, abstractmethod

from functions import Function, Sphere, Rastrigin, Rosenbrocks
from constrictions import ConstrictionFactor, FixedInertia, FloatingInertia, ClercConstriction
from enum import EnumConstrictionFactor, EnumFunction, EnumTopology
from constants import dimensions


class Particle(ABC):
	position = []
	position_pbest = []
	pbest = 0
	position_gbest = []
	gbest = 0
	velocity = []

	function_type = 0
	function = Function()

	constriction_type = 0
	constrictions = ConstrictionFactor()

	def __init__(self, function_type, constriction_type):
		self.function_type = function_type
		self.constriction_type = constriction_type

		if function_type == EnumFunction.sphere:
			self.function = Sphere()
		elif function_type == EnumFunction.rotated_rastrigin:
			self.function = Rastrigin()
		else:
			self.function = Rosenbrocks()

		if constriction_type == EnumConstrictionFactor.fixed_inertia:
			self.constrictions = FixedInertia()
		elif constriction_type == EnumConstrictionFactor.floating_inertia:
			self.constrictions = FloatingInertia()
		else:
			self.constrictions = ClercConstriction()

	def initialize(self):
		for i in range(0, dimensions):
			self.position[i] = (
				self.function.upper_bound - self.function.lower_bound
			) * random.random() + self.function.lower_bound
			self.velocity[i] = (
				self.function.upper_bound * 0.1 - self.function.lower_bound * 0.1
			) * random.random() + self.function.lower_bound * 0.1

		self.position_pbest = self.position
		self.pbest = self.function.calculate_fitness(self.position)

		if self.gbest == 0 and self.position_gbest == []:
			self.position_gbest = self.position_pbest
			self.gbest = self.pbest

		self.update_fitness()

	def update_position(self):
		for i in range(0, dimensions):
			self.position[i] += self.velocity[i]
		self.constrictions.update_parameters()

	def create_swarm(self, topology_type, function, constriction, particle_amount):
		swarm = []

		for i in range(0, particle_amount):
			if topology_type == EnumTopology.tlocal:
				swarm.insert(i, LocalParticle(function, constriction, swarm))
			elif topology_type == EnumTopology.tglobal:
				swarm.insert(i, GlobalParticle(function, constriction, swarm))
			else:
				swarm.insert(i, FocalParticle(function, constriction, swarm))

		return swarm

	@abstractmethod
	def update_speed(self):
		pass

	def update_fitness(self):
		new_pbest = self.function.calculate_fitness(self.position)

		if new_pbest < self.pbest:
			self.position_pbest = self.position
			self.pbest = new_pbest

			# This part is confusing, i dont think that should do this here
			if self.gbest > new_pbest:
				self.position_gbest = self.position
				self.gbest = new_pbest

	def force_boundaries(self):
		pass


class LocalParticle():
	pass


class GlobalParticle():
	pass


class FocalParticle():
	pass
