from dataclasses import dataclass


@dataclass
class Random_Generator:
    random_generator: iter

    @classmethod
    def from_config(cls, config, num_randoms):
        generator = Pseudo_Random(
            config["A"],
            config["C"],
            eval(config["M"]),
            config["seed"],
        )
        return cls(random_generator=(generator.random() for _ in range(num_randoms)))


@dataclass
class Pseudo_Random:
    A: int
    C: int
    M: int
    seed: int

    def random(self):
        next = ((self.A * self.seed) + self.C) % self.M
        self.seed = next
        return next / self.M
