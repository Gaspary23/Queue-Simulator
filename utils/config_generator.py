# Example configuration data
example_config = {
    "Simulator": {
        "simulation_randoms": 100_000,
        "arrival_interval": [2, 4],
        "first_arrival": 2,
        "starting_queue": "Q1",
    },
    "Q1": {
        "servers": 1,
        "capacity": "null",
        "departure_interval": [1, 2],
        "departure_paths": {"Q2": 0.8, "Q3": 0.2},
    },
    "Q2": {
        "servers": 2,
        "capacity": 5,
        "departure_interval": [4, 8],
        "departure_paths": {"Q1": 0.3, "Q3": 0.5},
    },
    "Q3": {
        "servers": 2,
        "capacity": 10,
        "departure_interval": [5, 15],
        "departure_paths": {"Q2": 0.7},
    },
    "rand": {"A": 1103515, "C": 123456, "M": "2**31", "seed": 23},
}


def generate_config_file(filename, config_data):
    with open(filename, "w") as file:
        for key, value in config_data.items():
            if key == "Simulator":
                file.write(f"{key}:\n")
                for k, v in value.items():
                    file.write(f"  {k}: {v}\n")
            elif key == "rand":
                file.write(f"{key}:\n")
                for k, v in value.items():
                    file.write(f"  {k}: {v}\n")
            else:
                file.write(f"{key}:\n")
                for k, v in value.items():
                    file.write(f"  {k}: {v}\n")


if __name__ == "__main__":
    generate_config_file("config.yml", example_config)
