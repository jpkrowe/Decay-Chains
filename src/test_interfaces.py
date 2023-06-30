'''Edit the functions in this file as you complete the associated tasks.
Each test should utilise aspects of your code to complete the specified task.
These functions will be called by tests in the test suite to ensure you code is working properly.
'''


def task_0_always_return_0():
    '''This function should always return the value zero'''
    pass


def task_0_addition(a, b):
    '''This function should return the sum of the parameters a and b'''
    pass


def task_1a_simple_decay_chain_populations(output_times: list, initial_number_of_moles: float, decay_rate: float):
    '''
    Edit this function as part of Activity 1A
    This function should return the populations of two isomers at a number of output times as one decays into the other
    :param output_times: list array of floats containing the times at which the populations of the isomers should be returned. The first time will always be 0.
    :param initial_number_of_moles: The initial number of moles of Isomer 1 (the decaying isomer). Isomer 2 (the produced isomer) should have an initial population of 0.
    :param decay_rate: The decay rate of the decaying isomer in units of 1/s.
    :returns: Should return two sequences (e.g. lists, Tuples, 1D Numpy arrays) of length n where n is the number of output times. The first sequence contains the populations of Isomer 1 as a function of time, the second contains he populations of Isomer 1 as a function of time. Ine ach sequence, the value with index [0] in each array is the population the isomer at t=0 and the value with index [n] is the number of moles of the isomer at the end of the simulation.
    '''
    # Write a runge kutta method to solve the following differential equation
    # dn_1/dt = -l*n_1
    # dn_2/dt = l*n_1

    import numpy as np
    from scipy.integrate import solve_ivp

    # Function to calculate the value of dn_1/dt
    def f1(n1, n2, l):
        return -l*n1

    # Function to calculate the value of dn_2/dt
    def f2(n1, n2, l):
        return l*n1

    def dy_dt(t, y):
        return np.array([f1(y[0], y[1], l), f2(y[0], y[1], l)])

    # calculate the values of n_1 and n_2 over 10000 time steps


    # use command line arguments to take initial values of n_1 and n_2
    l = decay_rate # Decay rate for n_1
    requested_times = output_times # Number of time steps
    t_span = (0, np.array(requested_times, dtype=float).max())
    y0 = (initial_number_of_moles, 0)
    # Create a list of time steps from 0 to total_timesteps with a step size of h

    sol = solve_ivp(dy_dt, t_span, y0, t_eval = requested_times)
    n1 = sol.y[0]
    n2 = sol.y[1]
    
    return n1, n2


def task_1b_decay_data_from_filename(filepath: str):
    '''
    Edit this function as part of Activity 1B
    This function should accept the a filename of a file in the endf dataset and return its decay rate and decay mode
    :param filename: str containing the filename to be read from, with no path prefix (such as "dec-019_K_040.endf")
    :returns: Should be a tuple containing the decay rate as a float units of 1/s, and the change to the atomic number and atomic mass caused by the decay as ints (e.g. (1.0, -2, 4) for alpha decay with a decay rate of 1.0/s)
    '''
    import os 
    import re
    import numpy as np

    'parse text to get string after the word ''Parent half-life: '' from a text file'
    def parse_file(filename):
        filename =  os.path.join('/decay_data/',filename)
        print(filename)
        print('screeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        file = open(filename, 'r')
        text = file.read()
        file.close()
        half_life = text.split('Parent half-life: ')[1]
        return half_life

    def parse_text(text):
        # Split the text into lines
        lines = text.split('\n')

        # Parse the first line
        first_line = lines[0]
        if "stable" in first_line.lower():
            parsed_first_line = re.findall(r'(.+?)\s+\d+ 1451', first_line)[0]
            parsed_decay_type = ""
        else:
            parsed_first_line = re.findall(r'(.+?)\s+\d+ 1451', first_line)[0]
            decay_type_line = lines[1]
            parsed_decay_type = re.findall(r'Decay Mode:\s+(.*)\s+\d+ 1451', decay_type_line)[0]

        return parsed_first_line, parsed_decay_type

    def convert_to_seconds(time_value, unit):
        unit = unit.upper()  # Convert the unit to uppercase for case-insensitive matching
        
        conversion_factors = {
            'PS': 1e-12,
            'NS': 1e-9,
            'US': 1e-6,
            'MS': 1e-3,
            'S': 1,
            'H': 3.6e3,
            'D': 8.64e4,
            'Y': 3.1536e7
        }
        
        if unit in conversion_factors:
            conversion_factor = conversion_factors[unit]
            seconds = float(time_value) * conversion_factor
            return seconds
        else:
            raise ValueError("Invalid unit: {}".format(unit))
        
    def find_time_unit(string):
        pattern = r'\b(PS|NS|US|MS|S|H|D|Y)\b'
        matches = re.findall(pattern, string, flags=re.IGNORECASE)
        return matches

    def parse_text_up_to(string, delimiter):
        parsed_text = string.partition(delimiter)[0]
        return parsed_text

    A,Z = 0,0
    #function that if decay mode is A atomic mass number is reduced by 4 and Z atomic number is reduced by 2, if B atomic mass number is reduced by 1 and Z atomic number is increased by 1, if EC atomic mass number is reduced by 1 and Z atomic number is increased by 1, if IT atomic mass number is reduced by 1 and Z atomic number is increased by 1, if P atomic mass number is reduced by 1 and Z atomic number is increased by 1, if N atomic mass number is reduced by 1 and Z atomic number is increased by 1, if SF atomic mass number is reduced by 1 and Z atomic number is increased by 1, if O atomic mass number is reduced by 1 and Z atomic number is increased by 1, if R atomic mass number is reduced by 1 and Z atomic number is increased by 1, if D atomic mass number is reduced by 2 and Z atomic number is reduced by 1, if T atomic mass number is reduced by 3 and Z atomic number is reduced by 1, if Q atomic mass number is reduced by 4 and Z atomic number is reduced by 2
    def decay_mode_out(decay_mode,A,Z):
        if decay_mode == 'A':
            A -= 4
            Z -= 2
        elif decay_mode == 'B-':
            A -= 1
            Z += 1
        elif decay_mode == 'EC':
            A -= 1
            Z += 1
        elif decay_mode == 'IT':
            A -= 1
            Z += 1
        elif decay_mode == 'P':
            A -= 1
            Z += 1
        elif decay_mode == 'N':
            A -= 1
            Z += 1
        elif decay_mode == 'SF':
            A -= 1
            Z += 1
        elif decay_mode == 'O':
            A -= 1
            Z += 1
        elif decay_mode == 'R':
            A -= 1
            Z += 1
        elif decay_mode == 'D':
            A -= 2
            Z -= 1
        elif decay_mode == 'T':
            A -= 3
            Z -= 1
        elif decay_mode == 'Q':
            A -= 4
            Z -= 2
        else:
            print('Invalid decay mode')  
        return A, Z

    split_text = parse_file(filepath)
    decay_time, decay_mode = (parse_text(split_text))
    decay_time_seconds = convert_to_seconds(parse_text_up_to(decay_time,find_time_unit(decay_time)[0]),find_time_unit(decay_time)[0])
    decay_rate = np.log(2)/decay_time_seconds
    decay_mode_out(decay_mode.replace(' ',''),A,Z)
    decay_atomic_number_change, decay_atomic_mass_change = A,Z
    return [float(decay_rate), int(decay_atomic_number_change), int(decay_atomic_mass_change)]


def task_1c_endf_filename_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding endf file name (without any preceding path)
    Note, you do not need to check if the file actually exists
    :param atomic_number: int providing the atomic number
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number
    :returns: Should be a string containing the endf filename  corresponding to the nuclear data (without any preceding path), e.g. dec-006_C_016
    '''
    pass


def task_1c_isomer_name_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding isomer name
    :param atomic_number: int providing the atomic number
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number
    :returns: Should be a string containing the isomer name  corresponding to the nuclear data, e.g. C16m1
    '''
    pass


def task_1c_isomer_nuclear_data_from_name(isomer_name: str):
    '''
    Edit this function as part of Activity 1C
    This function should accept the name of an isomer and return its nuclear data
    :param isomer_name: str containing the name of the nucleus (e.g. "Na24m1")
    :returns: Should be a tuple containing the atomic number, atomic mass and energy state number as ints
    '''
    pass


def task_2a_isomer_chain_from_initial_population(initial_isomer_name: str, initial_isomer_population: float, output_times: list):
    '''
    Edit this function as part of Activity 2A
    This function should accept the name of an isomer and return the populations of this and all daughter isomer sas a function of time
    :param isomer_name: str containing the name of the nucleus (e.g. "Na24m1")
    :param initial_isomer_population: float The number of moles of the initial isomer present
    :param output_times: list[float] The times at which the populations of isomers should be calculated. The first value will always be 0.
    :returns: Should be a dict whose keys are the names of the daughter isomers, and whose values are sequences (lists, tuple, numpy arrays, etc) holding the populations of those isomers at the output times
    '''
    pass
