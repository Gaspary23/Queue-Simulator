import sys

# Example configuration data
config_data = {
    "Simulator": {
        "arrival_interval": [2, 5],
    },
    "Queue": {
        "servers": 1,
        "capacity": 5,
        "departure_interval": [3, 5],
    },
    "rand": {"A": 512345, "C": 373621, "M": "2**31", "seed": 100},
}


def generate_config_file(filename, config_data, num_queues):
    with open(f"../{filename}", "w") as file:
        file.write("Simulator:\n")
        for key, value in config_data["Simulator"].items():
            file.write(f"  {key}: {value}\n")
        for i in range(num_queues):
            file.write(f"Q{i+1}:\n")
            for key, value in config_data["Queue"].items():
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
    generate_config_file("config.yml", config_data, qtd)
