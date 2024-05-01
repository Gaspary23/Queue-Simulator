import sys

from src.statistics_ import print_statistics
from utils.config_reader import instantiate_simulation_from_config


def main(filename="config.yml"):
    simulation, repetitions = instantiate_simulation_from_config(filename)
    simulation.run(repetitions)
    print_statistics(simulation)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        main()
