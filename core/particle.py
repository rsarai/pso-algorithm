from core.fitness_functions import sphere_function


class Particle:
    def __init__(self, position_list=None, velocity_list=None,
                 fitness_function=sphere_function):
        self.fitness = float('inf')
        self.fitness_best = float('inf')
        self.fitness_function = fitness_function

        self.position_list = [] if position_list is None else position_list
        self.velocity_list = [] if velocity_list is None else velocity_list
        self.personal_best_list = []

    def update_personal_best(self):
        self.fitness = self.fitness_function(self.position_list)

        if self.fitness < self.fitness_best:
            self.fitness_best = self.fitness
            self.personal_best_list = list(self.position_list)

    def set_velocity_list(self, new_velocities):
        self.velocity_list = list(new_velocities)

    def set_position_list(self, new_positions):
        self.position_list = list(new_positions)
