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

def generate_config_file(filename, config_data, num_queues):
    with open(filename, 'w') as file:
        file.write('QueueSimulator:\n')
        for i in range(num_queues):
            file.write(f'  Q{i+1}:\n')
            for key, value in config_data.items():
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict):
                        file.write(f'    {sub_key}:\n')
                        for sub_sub_key, sub_sub_value in sub_value.items():
                            file.write(f'      {sub_sub_key}: {sub_sub_value}\n')
                    else:
                        file.write(f'    {sub_key}: {sub_value}\n')


if __name__ == '__main__':
    import sys
    qtd = int(sys.argv[1])
    generate_config_file('queue_config.yml', config_data, qtd)