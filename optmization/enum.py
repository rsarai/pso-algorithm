from enum import Enum


class EnumConstrictionFactor(Enum):
	fixed_inertia = 1
	floating_inertia = 2
	clerc_constriction = 3


class EnumFunction(Enum):
	sphere = 1
	rotated_rastrigin = 2
	rosenbrock = 3


class EnumTopology(Enum):
	tglobal = 1
	tlocal = 2
	tfocal = 3
