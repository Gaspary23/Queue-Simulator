import yaml

from src.queue_ import Queue
from src.random_ import Random_Generator


def read_config(num_randoms, filename="config.yml"):
    try:
        queues = []
        with open(filename, "r") as file:
            config = yaml.safe_load(file)
            arrival_interval = tuple(config["Simulator"]["arrival_interval"])
            for key, value in config.items():
                if key.startswith("Q"):
                    queues.append(Queue.from_config(key, value))
            rands = Random_Generator.from_config(config["rand"], num_randoms)
        return arrival_interval, queues, rands
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
