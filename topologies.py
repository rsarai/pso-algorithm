import random
import time
import abc
from constants import c1, c2

class Topology():
    @abc.abstractmethod
    def update_velocity(self, swarm, inertia_weight, global_best_position, problem):
        pass

class Focal(Topology):
    def update_velocity(self, swarm, inertia_weight, global_best_position, problem):
        particle = swarm[0]
        for swarm_particle in swarm:
            if problem.evaluate_solution(particle) < problem.evaluate_solution(swarm_particle):
                particle.position_list = swarm_particle.position_list
                particle.personal_best = swarm_particle.position_list
        for i in range(0, len(swarm)):
            for j in range(0, len(swarm)):
                personal_component[i][j] = c1 * random.random() * (swarm[i].personal_best[j] - swarm[i].position_list[j])
                global_component[i][j] = c2 * random.random() * (particle.personal_best[j] - swarm[i].position_list[j])
                initial_value = inertia_weight * swarm[i].velocity[j]
                velocity[j] = initial_value + personal_component[i][j] + global_component[i][j]
            swarm[i].velocity = velocity

class Local(Topology):
    def update_velocity(self, swarm, inertia_weight, global_best_position, problem):
        personal_component = []
        global_component = []
        velocity = []

        for i in range(0, len(swarm)):
            for j in range(0, len(swarm)):
                personal_component = c1 * random.random() * (swarm[i].personal_best[j] - swarm[i].position_list[j])
                best_neighborhood = self._get_nearest_neighbor(swarm[i], swarm)
                global_component = c2 * random.random() * (best_neighborhood.position_list[j] - swarm[i].position_list[j])
                initial_value = swarm[i].velocity[j]
                velocity.append(inertia_weight * (initial_value + personal_component + global_component))

            swarm[i].velocity = velocity


    def _get_nearest_neighbor(self, particle, swarm):
        nearest_neighbor = 1000000000
        index_of_nearest = 0

        for i in range(0, len(swarm)):
            value = self._calculate_euclidean_distance(particle, swarm[i])
            if value < nearest_neighbor:
                nearest_neighbor = value
                index_of_nearest = i
        return swarm[i]


    def _calculate_euclidean_distance(self, particle, particle2):
        some_of_terms = 0
        for i in range(0, len(particle.position_list)):
            some_of_terms += (particle.position_list[i] - particle2.position_list[i]) ** 2
        return (some_of_terms ** 0.5)

class Global(Topology):

    def update_velocity(self, swarm, inertia_weight, global_best_position, problem):
        personal_component = []
        global_component = []
        velocity = []

        for i in range(0, len(swarm)):
            for j in range(0, len(swarm)):
                personal_component = c1 * random.random() * (swarm[i].personal_best[j] - swarm[i].position_list[j])
                global_component = c2 * random.random() * (global_best_position[j] - swarm[i].position_list[j])
                initial_value = inertia_weight * swarm[i].velocity[j]
                velocity.append(initial_value + personal_component + global_component)
            swarm[i].velocity = velocity
