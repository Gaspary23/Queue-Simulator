from dataclasses import dataclass


@dataclass
class Pseudo_Random_Generator:
    A: int
    C: int
    M: int
    seed: int

    def next_random(self):
        next = ((self.A * self.seed) + self.C) % self.M
        self.seed = next
        return next / self.M

    def next_random_bounded(self, low, high):
        return self.next_random() * (high - low) + low
