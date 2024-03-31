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
    generate_config_file('config.yml', config_data)
