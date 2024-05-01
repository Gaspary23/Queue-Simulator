import yaml

from src.queue_ import Queue
from src.random_ import Random_Generator
from src.simulation import Simulation


def instantiate_simulation_from_config(filename="config.yml"):
    (
        simulation_randoms,
        arrival_interval,
        first_arrival,
        starting_queue,
        queues,
        rand,
    ) = _read_config_file(filename)

    simulation = Simulation(
        queues=queues,
        starting_queue=starting_queue,
        random=rand,
        arrival_interval=arrival_interval,
        first_arrival=first_arrival,
    )

    return simulation, simulation_randoms


def _read_config_file(filename="config.yml"):
    try:
        queues = {}
        with open(filename, "r") as file:
            config = yaml.safe_load(file)
            # Simulator section
            simulation_randoms = config["Simulator"]["simulation_randoms"]
            arrival_interval = tuple(config["Simulator"]["arrival_interval"])
            first_arrival = config["Simulator"]["first_arrival"]
            starting_queue = config["Simulator"]["starting_queue"]
            # Queues section
            for key, value in config.items():
                if key.startswith("Q"):
                    queues[key] = Queue.from_config(value)
            # Random section
            rand = Random_Generator.from_config(config["rand"], simulation_randoms)
        return (
            simulation_randoms,
            arrival_interval,
            first_arrival,
            starting_queue,
            queues,
            rand,
        )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
