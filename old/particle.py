import random


class Particle():
    position_list = []
    personal_best = []
    velocity = []

    def __init__(self, position_list, velocity):
        self.position_list = position_list
        self.velocity = velocity
        self.personal_best = position_list

    def generate_personal_best(self):
        self.personal_best = []
        self.personal_best = self.position_list

    def update_position(self):
        for i in range(0, 30):
            self.position_list[i] += self.velocity[i]
