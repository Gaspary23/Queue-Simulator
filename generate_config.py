# Example configuration data
config_data = {
    'QueueSimulator': {
        'servers': 1,
        'capacity': 5,
        'arrival_interval': [2, 5],
        'departure_interval': [3, 5],
        'first_arrival': 2,
        'rand': {
            'A': 512345,
            'C': 373621,
            'M': '2**31',
            'seed': 100
        }
    }
}

config_dataQ1 = {
    'QueueSimulator': {
        'servers': 2,
        'capacity': 3,
        'arrival_interval': [1, 4],
        'departure_interval': [3, 4],
        'first_arrival': 1.5,
        'rand': {
            'A': 512345,
            'C': 373621,
            'M': '2**31',
            'seed': 100
        }
    }
}

config_dataQ2 = {
    'QueueSimulator': {
        'servers': 1,
        'capacity': 5,
        'arrival_interval': [1, 0],
        'departure_interval': [2, 3],
        'first_arrival': 10000,
        'rand': {
            'A': 512345,
            'C': 373621,
            'M': '2**31',
            'seed': 100
        }
    }
}

def generate_config_file(filename, config_data):
    with open(filename, 'w') as file:
        for key, value in config_data.items():
            file.write(f'{key}:\n')
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    file.write(f'  {sub_key}:\n')
                    for sub_sub_key, sub_sub_value in sub_value.items():
                        file.write(f'    {sub_sub_key}: {sub_sub_value}\n')
                else:
                    file.write(f'  {sub_key}: {sub_value}\n')


if __name__ == '__main__':
    import sys
#    generate_config_file('config.yml', config_data)

    qtd = int(sys.argv[1])
    for i in range(qtd):
        generate_config_file(f'configQ{i+1}.yml', config_data)
    
