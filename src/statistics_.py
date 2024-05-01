def print_statistics(simulation):
    print(f'{"-"*82}')
    print(f'{"-"*32} SIMULATION REPORT {"-"*31}')
    print(f'{"-"*82}')
    for i, queue in enumerate(simulation.queues):
        state_dict, mean_population = _get_statistics(queue, simulation.global_time)
        print(f'{"*"*82}')
        print(f"Queue {i+1}: (G/G/{queue.servers}/{queue.capacity})")
        if i == simulation.starting_queue:
            print(f"Arrival: {simulation.arrival_interval}")
        print(f"Departure: {queue.departure_interval}")
        print(f'{"*"*82}')
        for state in state_dict.keys():
            print(
                "State: {:<10} Time: {:<25} Probability: {}".format(
                    state,
                    queue.states[state]["Time"],
                    queue.states[state]["Probability"],
                )
            )
        print(f"\nNumber of losses: {queue.loss}")
        print(f"Mean population: {mean_population.__round__(2)}")
        print(f'{"*"*82}')
        print(f"Simulation time: {simulation.global_time}")


def _get_statistics(queue, total_time):
    for state in queue.states:
        queue.states[state]["Probability"] = queue.states[state]["Time"] / total_time

    mean_population = sum(
        (queue.states[state]["Probability"] * state) for state in queue.states
    )

    return queue.states, mean_population
