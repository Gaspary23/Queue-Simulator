from dataclasses import dataclass

from src.event import Event, EventType
from src.random_generator import Pseudo_Random_Generator


@dataclass
class QueueSimulator:
    servers: int
    capacity: int
    arrival_interval: tuple[int, int]
    departure_interval: tuple[int, int]
    rand: Pseudo_Random_Generator
    status: int = 0
    loss: int = 0
    global_time: float = 0
    first_arrival: int = 2
    scheduler: list[Event] = None

    def __post_init__(self):
        # Initialize the scheduler with the first arrival
        self.scheduler = [Event(EventType.ARRIVAL, self.first_arrival)]

    def next_event(self):
        next_event = min(self.scheduler, key=lambda x: x.time)
        self.scheduler.remove(next_event)

        return next_event

    def arrival(self, event_time):
        self.global_time = event_time
        if self.status < self.capacity:
            self.status += 1
            self.last_arrival = event_time

            if self.status <= self.servers:
                self.scheduler.append(
                    Event(
                        EventType.DEPARTURE,
                        event_time + self.schedule_departure()
                    )
                )
        else:
            self.loss += 1
        self.scheduler.append(
            Event(EventType.ARRIVAL, event_time + self.schedule_arrival())
        )

    def departure(self, event_time):
        self.global_time = event_time
        self.status -= 1
        if self.status >= self.servers:
            self.scheduler.append(
                Event(
                    EventType.DEPARTURE,
                    event_time + self.schedule_departure()
                )
            )

    def schedule_arrival(self):
        return self.rand.next_random_bounded(self.arrival_interval[0], self.arrival_interval[1])

    def schedule_departure(self):
        return self.rand.next_random_bounded(self.departure_interval[0], self.departure_interval[1])
