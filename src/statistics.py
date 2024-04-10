from src.event import EventType


def get_statistics(queue, events):
    state_dict = {
        x: {
            "Time": 0,
            "Probability": 0
        } for x in range(queue.capacity + 1)
    }
    total_time = events[-1].time
    status = 0
    previous_time = 0

    for event in events:
        state_dict[status]["Time"] += (event.time - previous_time)
        previous_time = event.time
        if event.event_type == EventType.ARRIVAL:
            if status < queue.capacity:  # if there is space in the queue
                status += 1
        else:
            status -= 1

    for state in state_dict:
        state_dict[state]["Probability"] = state_dict[state]["Time"] / total_time

    mean_population = sum(
        (state_dict[state]["Probability"] * state) for state in state_dict
    )

    return state_dict, mean_population, total_time


def print_statistics(queue, events):
    state_dict, mean_population, sim_time = get_statistics(queue, events)

    print(f'\nQueue: (G/G/{queue.servers}/{queue.capacity})')
    print(f'Arrival: {queue.arrival_interval}')
    print(f'Departure: {queue.departure_interval}')
    print(f'{"-"*82}')
    print(f'{"-"*32} SIMULATION REPORT {"-"*31}')
    print(f'{"-"*82}')
    for state in state_dict.keys():
        print(
            'State: {:<10} Time: {:<25} Probability: {}'.format(
                state, state_dict[state]["Time"], state_dict[state]["Probability"]
            )
        )
    print(f'{"-"*82}')
    print(f'Simulation time: {sim_time}')
    print(f'Mean population: {mean_population.__round__(2)}')
    print(f'Number of losses: {queue.loss}')
 # type: ignore