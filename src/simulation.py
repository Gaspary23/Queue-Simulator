from dataclasses import dataclass

from src.event import Event, EventType
from src.queue_ import Queue


@dataclass
class Simulation:
    queues: list[Queue]
    starting_queue: int  # Index of the queue that receives arrivals
    random: iter  # Generator of random numbers
    arrival_interval: tuple[int, int]
    first_arrival: int
    randoms_used: int = 0
    global_time: int = 0

    def __post_init__(self):
        # Initialize the scheduler with the first arrival
        self.scheduler = [
            Event(EventType.ARRIVAL, self.first_arrival, queue=self.starting_queue)
        ]

    def simulation_step(self):
        event = self._next_event()
        if event.event_type == EventType.ARRIVAL:
            self._arrival(event)
        else:
            self._departure(event)

    def _next_event(self):
        next_event = min(self.scheduler, key=lambda x: x.time)
        self.scheduler.remove(next_event)

        return next_event

    def _arrival(self, event: Event):
        self._update_time(event)
        queue = self.queues[self.starting_queue]

        if not queue.is_full():
            queue.status += 1

            if queue.status <= queue.servers:
                self._schedule_departure(queue)
        else:
            queue.loss += 1

        self._schedule_arrival()

    def _departure(self, event: Event):
        self._update_time(event)
        queue = self.queues[event.queue]

        queue.status -= 1
        if queue.status >= queue.servers:
            self._schedule_departure(queue)

        dest_queue = self._choose_destination(queue)
        if dest_queue is not None:
            if not dest_queue.is_full():
                dest_queue.status += 1
                if dest_queue.status <= dest_queue.servers:
                    self._schedule_departure(dest_queue)
            else:
                dest_queue.loss += 1

    def _update_time(self, event: Event):
        delta = event.time - self.global_time

        for queue in self.queues:
            queue.states[queue.status]["Time"] += delta

        self.global_time = event.time

    def _choose_destination(self, queue: Queue):
        if len(queue.departure_paths) == 0:
            return None

        self.randoms_used += 1
        rand = next(self.random)

        for q, prob in queue.departure_paths.items():
            if rand < prob:
                return self.queues[q]
            rand -= prob
        return None

    def _schedule_arrival(self):
        self.randoms_used += 1
        delta = (
            next(self.random) * (self.arrival_interval[1] - self.arrival_interval[0])
            + self.arrival_interval[0]
        )

        self.scheduler.append(
            Event(
                EventType.ARRIVAL,
                self.global_time + delta,
                queue=self.starting_queue,
            )
        )

    def _schedule_departure(self, queue: Queue):
        self.randoms_used += 1
        delta = (
            next(self.random)
            * (queue.departure_interval[1] - queue.departure_interval[0])
            + queue.departure_interval[0]
        )

        self.scheduler.append(
            Event(
                EventType.DEPARTURE,
                self.global_time + delta,
                queue=self.queues.index(queue),
            )
        )
