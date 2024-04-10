import yaml

from src.event import EventType
from src.queue import QueueSimulator
from src.statistics import print_statistics

SIMULATION_REPETITIONS = 100_000


def main():
    events = []
    queue1 = QueueSimulator.from_config(read_config('configQ1.yml'))
    queue2 = QueueSimulator.from_config(read_config('configQ2.yml'))

    count_randoms = 0
    while count_randoms < SIMULATION_REPETITIONS:
        event = queue1.next_event()
        events.append(event)

        if event.event_type == EventType.ARRIVAL:
            queue1.arrival(event.time)

            count_randoms += 1
            if queue1.status < queue1.capacity and queue1.status <= queue1.servers:
                count_randoms += 1
        else:
            queue1.departure(event.time)
            queue2.arrival(event.time)
            count_randoms += 1
            if queue2.status < queue2.capacity and queue2.status <= queue2.servers:
                count_randoms += 1   


            if queue1.status >= queue1.servers:
                count_randoms += 1

    print_statistics(queue1, events)
    print_statistics(queue2, events)


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
