import sys

# Example configuration data
single_queue = {
    "Simulator": {
        "arrival_interval": [2, 5],
    },
    "Q0": {
        "servers": 1,
        "capacity": 5,
        "departure_interval": [3, 5],
        "departure_paths": {},
    },
    "rand": {"A": 512345, "C": 373621, "M": "2**31", "seed": 100},
}

three_queues = {
    "Simulator": {"arrival_interval": [2, 5]},
    "Q0": {
        "servers": 3,
        "capacity": 3,
        "departure_interval": [2, 8],
        "departure_paths": {1: 0.4},
    },
    "Q1": {
        "servers": 2,
        "capacity": 3,
        "departure_interval": [10, 20],
        "departure_paths": {0: 0.3, 2: 0.7},
    },
    "Q2": {
        "servers": 4,
        "capacity": 3,
        "departure_interval": [15, 30],
        "departure_paths": {},
    },
    "rand": {"A": 512345, "C": 373621, "M": "2**31", "seed": 100},
}


def generate_config_file(filename, config_data, num_queues):
    with open(filename, "w") as file:
        file.write("Simulator:\n")
        for key, value in config_data["Simulator"].items():
            file.write(f"  {key}: {value}\n")
        for i in range(num_queues):
            file.write(f"Q{i}:\n")
            for key, value in config_data[f"Q{i}"].items():
                file.write(f"  {key}: {value}\n")
        file.write("rand:\n")
        for key, value in config_data["rand"].items():
            file.write(f"  {key}: {value}\n")


if __name__ == "__main__":
    try:
        qtd = int(sys.argv[1])
    except IndexError:
        print("Usage: python generate_config.py <num_queues>")
        sys.exit(1)
    match qtd:
        case 1:
            config = single_queue
        case 3:
            config = three_queues
    generate_config_file("config.yml", config, qtd)
