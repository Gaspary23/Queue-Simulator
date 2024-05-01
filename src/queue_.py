from dataclasses import dataclass


@dataclass
class Queue:
    name: str
    servers: int
    capacity: int
    departure_interval: tuple[int, int]
    departure_paths: dict[int, float]  # {queue_index: probability}
    status: int = 0
    loss: int = 0

    def __post_init__(self):
        self.states = {
            x: {"Time": 0, "Probability": 0} for x in range(self.capacity + 1)
        }

    def is_full(self):
        return self.status >= self.capacity

    @classmethod
    def from_config(cls, name, config):
        return cls(
            name=name,
            servers=config["servers"],
            capacity=config["capacity"],
            departure_interval=config["departure_interval"],
            departure_paths=config["departure_paths"],
        )
