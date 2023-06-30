import os 
import re
import numpy as np
'function that asks for filename adn sets value' 
def get_filename():
    filename = input('Enter a filename: ')
    return filename

'parse text to get string after the word ''Parent half-life: '' from a text file'
def parse_file(filename):
    filename =  os.path.join('../decay_data/',filename)
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

# filename = get_filename()
filename  = 'dec-002_He_006.endf'
split_text = parse_file(filename)
decay_time, decay_mode = (parse_text(split_text))
decay_time_seconds = convert_to_seconds(parse_text_up_to(decay_time,find_time_unit(decay_time)[0]),find_time_unit(decay_time)[0])
decay_rate = np.log(2)/decay_time_seconds
print(decay_rate)
print(decay_mode_out(decay_mode.replace(' ',''),A,Z))

#dec-002_He_006.endf
# dec-004_Be_010.endf