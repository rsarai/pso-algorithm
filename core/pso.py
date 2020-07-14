import math
import random
from core.particle import Particle
from core import topologies


class PSOAlgorithm:
    def __init__(
        self, topology, bound, max_speed, dimensions, num_particles, num_iterations,
        fitness_function, inertia_coef=0.9
    ):
        # Configurations
        self.bound = bound
        self.max_speed = max_speed
        self.dimensions = dimensions
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.fitness_function = fitness_function
        self.inertia_coef = inertia_coef

        # Internals
        self.topology = topology
        self.global_best = float('inf')
        self.global_best_position = []
        self.list_global_best_values = []
        self.swarm = []

        self._initialize_swarm()

    def _initialize_swarm(self):
        self.swarm = []
        for _ in range(self.num_particles):
            particle = Particle(
                position_list=[
                    random.uniform(self.bound[0], self.bound[1])
                    for i in range(self.dimensions)
                ],
                velocity_list=[
                    random.uniform(self.max_speed[0], self.max_speed[1])
                    for i in range(self.dimensions)
                ],
                fitness_function=self.fitness_function
            )
            self.swarm.append(particle)
        print(
            f"Swarm initialized with {self.num_particles} particles "
            f"and {self.dimensions} dimensions"
        )

    def updates_global_best(self, particle):
        new_best = particle.fitness

        if new_best < self.global_best:
            self.global_best = new_best
            self.global_best_position = list(particle.position_list)

    def updates_velocity(self, particle, inertia_type):
        if type(self.topology) == topologies.Global:
            new_velocities = self.topology.get_new_velocity(
                inertia_coef=self.inertia_coef,
                particle=particle,
                swarm_global_best_pos=self.global_best_position,
                clerc=(3 == inertia_type))
            particle.set_velocity_list(new_velocities)

        if type(self.topology) == topologies.Local:
            new_velocities = self.topology.get_new_velocity(
                inertia_coef=self.inertia_coef,
                particle=particle,
                swarm=self.swarm,
                clerc=(3 == inertia_type))
            particle.set_velocity_list(new_velocities)

    def updates_position(self, particle):
        new_positions = [
            particle.position_list[i] + particle.velocity_list[i]  # note that velocity list was already updated
            for i in range(0, len(particle.position_list))
        ]

        final_new_positions = []
        for pos in new_positions:
            if pos > self.bound[1]:
                final_new_positions.append(self.bound[1])
            elif pos < self.bound[0]:
                final_new_positions.append(self.bound[0])
            else:
                final_new_positions.append(pos)
        particle.set_position_list(final_new_positions)

    def updates_inertia_weight_if_necessary(self, inertia_type, i):
        if inertia_type == 1:
            self.inertia_coef = 0.8
        elif inertia_type == 2:
            self.inertia_coef = (0.9 - 0.4) * ((self.num_iterations - i)/self.num_iterations) + 0.4
        elif inertia_type == 3:
            greek_letter = self.topology.c1_individuality_factor + self.topology.c2_sociability_factor
            square_func_val = (greek_letter * greek_letter) - (4 * greek_letter)
            self.inertia_coef = 2 / abs(2 - greek_letter - math.sqrt(square_func_val))
        else:
            raise Exception()

    def search(self, inertia_type):

        for i in range(self.num_iterations):
            for particle in self.swarm:
                particle.update_personal_best()
                self.updates_global_best(particle)

            self.updates_inertia_weight_if_necessary(inertia_type, i)
            for particle in self.swarm:
                self.updates_velocity(particle, inertia_type)
                self.updates_position(particle)

            self.list_global_best_values.append(self.global_best)
            print(f"End of iteration {i}. Global best is {self.global_best}. Best position len is: {len(self.global_best_position)}")
