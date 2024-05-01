from dataclasses import dataclass


@dataclass
class Random_Generator:
    generator: iter

    def __iter__(self):
        return self.generator

    def __next__(self):
        try:
            return next(self.generator)
        except StopIteration:
            return 1.0

    @classmethod
    def from_config(cls, config, num_randoms):
        random = Pseudo_Random(
            config["A"],
            config["C"],
            eval(config["M"]),
            config["seed"],
        )
        return cls(generator=(random.get_random() for _ in range(num_randoms)))


@dataclass
class Pseudo_Random:
    A: int
    C: int
    M: int
    seed: int

    def get_random(self):
        next = ((self.A * self.seed) + self.C) % self.M
        self.seed = next
        return next / self.M
