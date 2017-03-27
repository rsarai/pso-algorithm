import random
from constants import number_of_particles, iterations_number
from topologies import Topology
from problems import Problem
from particle import Particle

class PSO():
    swarm = []
    global_best_position = []
    global_fitness = 0
    inertia_weight = 0.9
    problem = Problem()
    topology = Topology()
    result = []

    def __init__(self, problem, topology):
        self.problem = problem
        self.topology = topology

    def initialize_swarm(self):
        swarm = []
        for i in range(0, number_of_particles):
            position_list = self.generate_random_position(self.problem)
            velocity = self.generate_random_velocity()
            p=Particle(position_list, velocity)
            swarm.append(p)
        return swarm

    def search(self, velocity_factor):
        self.swarm = self.initialize_swarm()
        self.global_best_position = self.swarm[0].personal_best
        self.define_inertia_weight(velocity_factor)

        for i in range(0, iterations_number):    
            self.topology.update_velocity(self.swarm, self.inertia_weight, self.global_best_position, self.problem)
            self.update_position()
            self.update_global_best(self.problem)
            self.global_fitness = self.problem.evaluate_solution(self.global_best_position)
            self.result.append([self.global_fitness, i])
        return self.result

    def update_position(self):
        for particle in self.swarm:
            for i in range(0, len(particle.position_list)):
                particle.position_list[i] += particle.velocity[i]

    def define_inertia_weight(self, velocity_factor):
        if velocity_factor == 1:
            self.inertia_weight = 0.8
        elif velocity_factor == 2:
            self.inertia_weight -= 0.00005
        else:
            self.inertia_weight = 0.729

    def update_global_best(self, problem):
        for particle in self.swarm:
            if problem.evaluate_solution(particle.personal_best) < problem.evaluate_solution(self.global_best_position):
                self.global_best_position = particle.personal_best

    def update_local_best(self, problem):
        for particle in self.swarm:
            if problem.evaluate_solution(particle.position_list) < problem.evaluate_solution(particle.personal_best):
                particle.personal_best = particle.position_list

    def generate_random_velocity(self):
        velocity = []
        for i in range(0, 30):
            velocity.append(random.uniform(-1, 1))
        return velocity

    def generate_random_position(self, problem):
        position_list = []
        for i in range(0, 30):
            position_list.append(random.uniform(problem.lower_bound, problem.upper_bound))
        return position_list
