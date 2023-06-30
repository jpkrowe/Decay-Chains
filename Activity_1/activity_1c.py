#write an intro to the program
print("This program will calculate the activity of a radioactive sample.")
# Generate the ENDF filename for a particular atom

# dictionary
element_symbols = {
        1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
        11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca',
        21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn',
        31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr',
        41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn',
        51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd',
        61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb',
        71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg',
        81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th',
        91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm',
        101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Ds',
        111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'
    }

# Function for element symbol
def get_element_symbol(atomic_number):
    
    
    if atomic_number in element_symbols:
        return element_symbols[atomic_number]
    else:
        return "Unknown"
    
# crete funciton to return energy level as string or empty string
def get_energy_level(energy_level):
    if energy_level == 0:
        return ""
    else:
        return "m"+str(energy_level)

# create frunction to geeratue the filename
def get_filename(atomic_number, atomic_mass, energy_level):
    # check all input values are integers
    if not isinstance(atomic_number, int):
        raise TypeError("Atomic number must be an integer")
    if not isinstance(atomic_mass, int):
        raise TypeError("Atomic mass must be an integer")
    if not isinstance(energy_level, int):
        raise TypeError("Energy level must be an integer")
    # check all input values are positive
    if atomic_number < 0:
        raise ValueError("Atomic number must be positive")
    if atomic_mass < 0:
        raise ValueError("Atomic mass must be positive")
    if energy_level < 0:
        raise ValueError("Energy level must be positive")
    # check atomic number is less than atomic mass
    if atomic_number > atomic_mass:
        raise ValueError("Atomic number must be less than atomic mass")
    # get element symbol from atomic number
    element_symbol = get_element_symbol(atomic_number)
    # get energy level as string
    energy_level_str = get_energy_level(energy_level)
    # generate filename
    # convert integer to three digit string
    atomic_number_str = str(atomic_number).zfill(3)#
    atomic_mass_str = str(atomic_mass).zfill(3)
    filename = "dec-"+atomic_number_str+"_"+element_symbol+"_"+atomic_mass_str+ energy_level_str + ".endf"
    return filename

# function to generate name of isomer from atomic number, atomic mass and energy level
def get_isomer_name(atomic_number, atomic_mass, energy_level):
    # check all input values are integers
    if not isinstance(atomic_number, int):
        raise TypeError("Atomic number must be an integer")
    if not isinstance(atomic_mass, int):
        raise TypeError("Atomic mass must be an integer")
    if not isinstance(energy_level, int):
        raise TypeError("Energy level must be an integer")
    # check all input values are positive
    if atomic_number < 0:
        raise ValueError("Atomic number must be positive")
    if atomic_mass < 0:
        raise ValueError("Atomic mass must be positive")
    if energy_level < 0:
        raise ValueError("Energy level must be positive")
    # check atomic number is less than atomic mass
    if atomic_number > atomic_mass:
        raise ValueError("Atomic number must be less than atomic mass")
    # get element symbol from atomic number
    element_symbol = get_element_symbol(atomic_number)
    # get energy level as string
    energy_level_str = get_energy_level(energy_level)
    # generate filename
    # convert integer to three digit string
    atomic_number_str = str(atomic_number).zfill(3)#
    atomic_mass_str = str(atomic_mass)
    # generate isomer name as element symbol + atomic mass + energy level
    isomer_name = element_symbol + atomic_mass_str + energy_level_str
    return isomer_name

# function to get atomic number, atomic mass and energy state from isomer name
def get_atomic_number(isomer_name):
    # check isomer name is a string
    if not isinstance(isomer_name, str):
        raise TypeError("Isomer name must be a string")
    # check isomer name is not empty
    if len(isomer_name) == 0:
        raise ValueError("Isomer name cannot be empty")
    # get atomic mass from isomer name
    # check for number of characters before integers appear
    for i in range(len(isomer_name)):
        if isomer_name[i].isdigit():
            end_isomer_name = i
            break
    # check for number of intigers after end of isomer name
    for i in range(end_isomer_name, len(isomer_name)):
        if not isomer_name[i].isdigit():
            end_atomic_mass = i
            break
        if i == len(isomer_name)-1:
            end_atomic_mass = len(isomer_name)
    # check for number of characters after atomic mass
    if(end_atomic_mass == len(isomer_name)):
        # zero energy level
        energy_level = 0
    else:
        # non-zero energy level
        energy_level = int(isomer_name[end_atomic_mass+1:])
    # get atomic number from isomer name using element symbol array
    for i in range(1, len(element_symbols)+1):
        if isomer_name[0:end_isomer_name] == element_symbols[i]:
            atomic_number = i
            break
    # get atomic mass from isomer name
    atomic_mass = int(isomer_name[end_isomer_name:end_atomic_mass])
    return atomic_number, atomic_mass, energy_level

# define function to ask user whether they would like to input an isomer name or atomic number, atomic mass and energy level
def get_user_input():
    # ask user whether they would like to input an isomer name or atomic number, atomic mass and energy level
    user_input = input("Would you like to input an isomer name or atomic number, atomic mass and energy level? (isomer/atomic): ")
    # check if user says boom
    if user_input == "boom":
        # call boom function
        boom()
    # check user input is valid
    if user_input != "isomer" and user_input != "atomic":
        raise ValueError("User input must be 'isomer' or 'atomic'")
    # select appropriate function
    if user_input == "isomer":
        get_isomer_name_input() 
    else:
        get_atomic_number_input()
    return


# define funciton for when user selects atomic number, atomic mass and energy level
def get_atomic_number_input():
    # promt user for input
    atomic_number = int(input("Enter the atomic number: "))
    atomic_mass = int(input("Enter the atomic mass: "))
    energy_level = int(input("Enter the energy level: "))
    # find filename
    filename = get_filename(atomic_number, atomic_mass, energy_level)
    # print filename
    print("The filename is: " + filename)
    # find isomer name
    isomer_name = get_isomer_name(atomic_number, atomic_mass, energy_level)
    # print isomer name
    print("The isomer name is: " + isomer_name)
    return

#define function for when user selects isomer name
def get_isomer_name_input():
    # promt user for input
    isomer_name = input("Enter the isomer name: ")
    # find atomic number, atomic mass and energy level
    atomic_number, atomic_mass, energy_level = get_atomic_number(isomer_name)
    # print atomic number, atomic mass and energy level
    print("The atomic number is: " + str(atomic_number))
    print("The atomic mass is: " + str(atomic_mass))
    print("The energy level is: " + str(energy_level))
    return

# define function for setting off nuclear explosion
def boom():
    # set off a nuclear explosion
    print("BOOM!")
    # add animation of nuclear explosion using ascii art
    # get explosion ascii art from google
    # explosion ascii art from https://www.asciiart.eu/weapons/explosives
    print("       _.-^^---....,,--       ")
    print("   _--                  --_   ")
    print("  <                        >) ")
    print("  |                         | ")
    print("   \._                   _./  ")
    print("      ```--. . , ; .--'''       ")
    print("            | |   |             ")
    print("         .-=||  | |=-.   ")
    print("         `-=#$%&%$#=-'   ")
    print("            | ;  :|      ")
    print("       _____| :__;_____ ")


# promt user for input
get_user_input()

# q: what would you do if you ruled the world?
# a: I would make everyone learn python
# q: what if someone didn't want to learn python?
# a: I would set off a nuclear explosion
# q: what would that look like?
# a: BOOM!
# set off a nuclear explosion
# add animation of nuclear explosion using ascii art
# get explosion ascii art from google
# explosion ascii art from https://www.asciiart.eu/weapons/explosives
print("       _.-^^---....,,--       ")
print("   _--                  --_   ")
print("  <                        >) ")
print("  |                         | ")
print("   \._                   _./  ")
print("      ```--. . , ; .--'''       ")
print("            | |   |             ")
print("         .-=||  | |=-.   ")
print("         `-=#$%&%$#=-'   ")
print("            | ;  :|      ")
print("       _____| :__;_____ ")




# end of program









    