from src.simulation import Simulation
from src.statistics_ import print_statistics
from utils.config_reader import read_config

SIMULATION_REPETITIONS = 100_000
FIRST_ARRIVAL = 2


def main():
    arrival_interval, queues, rands = read_config(SIMULATION_REPETITIONS)

    simulation = Simulation(
        queues=queues,
        starting_queue=0,
        random_generator=rands,
        arrival_interval=arrival_interval,
        first_arrival=FIRST_ARRIVAL,
    )

    while simulation.randoms_used < SIMULATION_REPETITIONS:
        simulation.simulation_step()

    print_statistics(simulation)


if __name__ == "__main__":
    main()
