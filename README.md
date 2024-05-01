# Queue Simulator

The simulator uses a file called `config.yml` to load the simulation parameters. To generate a configuration file with default parameters, just run the script `config_generator.py`, specifying the number of desired queues with the command:

```bash
python utils/config_generator.py <num_queues>
```

After generating the configuration file, just change the parameter values in the `config.yml` file to the desired values.

> **_Note_**: Queue names should be unique, and comprised of a capital 'Q' followed by a number. For example, Q1, Q2, Q3, etc.

To run the simulator just execute the `main.py` file with the command:

```bash
python main.py
```
