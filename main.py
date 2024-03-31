from src.event import EventType
from src.queue import QueueSimulator
from src.random_generator import Pseudo_Random_Generator
from src.statistics import print_statistics

SIMULATION_REPETITIONS = 100_000


def main():
    events = []
    rand = Pseudo_Random_Generator(
        A=512345, C=373621, M=2**31, seed=100
    )

    queue = QueueSimulator(
        rand=rand, first_arrival=2,
        servers=2, capacity=5,
        arrival_interval=(2, 5),
        departure_interval=(3, 5)
    )

    for _ in range(SIMULATION_REPETITIONS):
        event = queue.next_event()
        events.append(event)
        if event.event_type == EventType.ARRIVAL:
            queue.arrival(event.time)
        else:
            queue.departure(event.time)

    print_statistics(queue, events)


if __name__ == "__main__":
    main()
