from dataclasses import dataclass
from math import inf


@dataclass
class Queue:
    servers: int
    capacity: int
    departure_interval: tuple[int, int]
    departure_paths: dict[str, float]  # {queue_name: probability}
    status: int = 0
    loss: int = 0

    def __post_init__(self):
        if self.capacity is None:
            self.capacity = inf

        if self.capacity != inf:
            self.states = {
                x: {"Time": 0, "Probability": 0} for x in range(self.capacity + 1)
            }
        else:
            self.states = {0: {"Time": 0, "Probability": 0}}

    def is_full(self):
        return self.status >= self.capacity

    @classmethod
    def from_config(cls, config):
        return cls(
            servers=config["servers"],
            capacity=config["capacity"],
            departure_interval=config["departure_interval"],
            departure_paths=config["departure_paths"],
        )
