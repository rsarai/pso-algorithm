import random


class Global:
    def __init__(self, max_speed, c1_individuality_factor=2.05, c2_sociability_factor=2.05):
        self.c1_individuality_factor = c1_individuality_factor
        self.c2_sociability_factor = c2_sociability_factor
        self.max_speed = max_speed

    def get_new_velocity(self, inertia_coef, particle, swarm_global_best_pos, clerc=False):
        new_velocities_list = []
        for i in range(0, len(particle.position_list)):
            r1 = random.random()
            personal_component = self.c1_individuality_factor * r1 * (particle.personal_best_list[i] - particle.position_list[i])

            r2 = random.random()
            social_component = self.c2_sociability_factor * r2 * (swarm_global_best_pos[i] - particle.position_list[i])

            if clerc:
                new_velocity = particle.velocity_list[i] + personal_component + social_component
                new_velocity = inertia_coef * new_velocity
            else:
                actual_component = inertia_coef * particle.velocity_list[i]
                new_velocity = actual_component + personal_component + social_component

            if new_velocity > self.max_speed[1]:
                new_velocity = self.max_speed[1]
            elif new_velocity < self.max_speed[0]:
                new_velocity = self.max_speed[0]

            new_velocities_list.append(new_velocity)

        return new_velocities_list

    def __str__(self):
        return "Global Topology"


class Local:
    def __init__(self, max_speed, c1_individuality_factor=2.05, c2_sociability_factor=2.05):
        self.c1_individuality_factor = c1_individuality_factor
        self.c2_sociability_factor = c2_sociability_factor
        self.max_speed = max_speed

    def get_new_velocity(self, inertia_coef, particle, swarm, clerc=False):
        neighborhood_particle = self._get_nearest_neighborhood(particle, swarm)
        new_velocities_list = []
        for i in range(0, len(particle.position_list)):
            r1 = random.random()
            personal_component = self.c1_individuality_factor * r1 * (particle.personal_best_list[i] - particle.position_list[i])

            r2 = random.random()
            social_component = self.c2_sociability_factor * r2 * (neighborhood_particle.position_list[i] - particle.position_list[i])

            if clerc:
                new_velocity = particle.velocity_list[i] + personal_component + social_component
                new_velocity = inertia_coef * new_velocity
            else:
                actual_component = inertia_coef * particle.velocity_list[i]
                new_velocity = actual_component + personal_component + social_component

            if new_velocity > self.max_speed[1]:
                new_velocity = self.max_speed[1]
            elif new_velocity < self.max_speed[0]:
                new_velocity = self.max_speed[0]

            new_velocities_list.append(new_velocity)

        return new_velocities_list

    def _get_nearest_neighborhood(self, particle, swarm):
        nearest_neighbor = float('inf')
        other_particle = None

        for neighbor_particle in swarm:
            value = self._calculate_euclidean_distance(particle, neighbor_particle)
            if value < nearest_neighbor:
                nearest_neighbor = value
                other_particle = neighbor_particle
        return other_particle

    def _calculate_euclidean_distance(self, particle, particle2):
        some_of_terms = 0
        for i in range(0, len(particle.position_list) - 1):
            some_of_terms += (particle.position_list[i] - particle2.position_list[i]) ** 2
        return (some_of_terms ** 0.5)

    def __str__(self):
        return "Local Topology"
