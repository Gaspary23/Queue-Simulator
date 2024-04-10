import yaml

from src.event import EventType
from src.queue import QueueSimulator
from src.statistics import print_statistics

SIMULATION_REPETITIONS = 100_000


def main():
    events = []
    queue_count = count_queues(read_config('queue_config.yml'))
    queues = []
    queues = [QueueSimulator.from_config(read_config(f'queue_config.yml'), i+1) for i in range(queue_count)]
    
    queue1 = queues[0]
    queue2 = queues[1]

    count_randoms = 0
    while count_randoms < SIMULATION_REPETITIONS:
        event = queues[0].next_event()
        events.append(event)

        if event.event_type == EventType.ARRIVAL:
            queues[0].arrival(event.time)

            count_randoms += 1
            if queues[0].status < queues[0].capacity and queues[0].status <= queues[0].servers:
                count_randoms += 1
        else:
            for i in range(queue_count):
                if queues[i].status > 0:
                    queues[i].departure(event.time)
                    if queues[i].status >= queues[i].servers:
                        count_randoms += 1
                    if i < queue_count - 1:
                        queues[i+1].arrival(event.time)
                        count_randoms += 1
                        if queues[i+1].status < queues[i+1].capacity and queues[i+1].status <= queues[i+1].servers:
                            count_randoms += 1
        
    for queue in queues:
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

def count_queues(config):
    return len(config['QueueSimulator'])

if __name__ == "__main__":
    main()
