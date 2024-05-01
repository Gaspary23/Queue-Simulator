def print_statistics(simulation):
    print(f'{"-"*70}')
    print(f'{"-"*25} SIMULATION  REPORT {"-"*25}')
    print(f'{"-"*70}')
    for i, qname in enumerate(simulation.queues):
        queue = simulation.queues[qname]
        state_dict, mean_population = _get_statistics(queue, simulation.global_time)
        print(f'{"*"*70}')
        print(f"Queue {qname[1]}: (G/G/{queue.servers}/{queue.capacity})")
        if i == simulation.starting_queue:
            print(f"Arrival: {simulation.arrival_interval}")
        print(f"Departure: {queue.departure_interval}")
        print(f'{"*"*70}')
        for state in state_dict.keys():
            print(
                "State: {:<10} Time: {:<25} Probability: {:.2f}".format(
                    state,
                    queue.states[state]["Time"],
                    queue.states[state]["Probability"] * 100,
                )
            )
        print(f"\nNumber of losses: {queue.loss}")
        print(f"Mean population: {mean_population.__round__(2)}")
        print(f'{"*"*70}')
    print(f"Simulation time: {simulation.global_time}")


def _get_statistics(queue, total_time):
    for state in queue.states:
        queue.states[state]["Probability"] = queue.states[state]["Time"] / total_time

    mean_population = sum(
        (queue.states[state]["Probability"] * state) for state in queue.states
    )

    return queue.states, mean_population
