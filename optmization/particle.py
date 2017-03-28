import random

from functions import Function, Sphere, Rastrigin, Rosenbrocks
from constrictions import ConstrictionFactor, FixedInertia, FloatingInertia, ClercConstriction
from enum import EnumConstrictionFactor, EnumFunction


class Particle():
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
