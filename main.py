import yaml

from src.event import EventType
from src.queue import QueueSimulator
from src.statistics import print_statistics

SIMULATION_REPETITIONS = 100_000


def main():
    events = []
    queue = QueueSimulator.from_config(read_config('config.yml'))

    count_randoms = 0
    while count_randoms < SIMULATION_REPETITIONS:
        event = queue.next_event()
        events.append(event)

        if event.event_type == EventType.ARRIVAL:
            queue.arrival(event.time)

            count_randoms += 1
            if queue.status < queue.capacity and queue.status <= queue.servers:
                count_randoms += 1
        else:
            queue.departure(event.time)

            if queue.status >= queue.servers:
                count_randoms += 1

    print_statistics(queue, events)


def read_config(filename='config.yml'):
    try:
        with open(filename, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None


if __name__ == "__main__":
    main()
