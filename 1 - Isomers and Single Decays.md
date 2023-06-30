# Isomers and Decays

## Background

### Elements, Isotopes and Isomers

At the centre of every atom lies its nucleus. A nucleus is comprised of protons and neutrons, collectively known as nuclides. Normally these nuclides sit in the lowest energy configuration available to them, known as its "ground state". Sometimes, though, these nuclides are arranged in one of a number of higher energy configurations, known as "excited states". Dependent on the number of different nuclides and their energy state, the nucleus will have different properties. We'll begin with some basic definitions to help our discussion:

* Atomic number: describes the number of protons in a nucleus.
* Atomic mass: describes the number nuclides (protons + neutrons) in a nucleus
* Element: all atoms with the same atomic number are the same element (e.g. all Hydrogen nuclei have 1 proton, all Carbon atoms have 6 protons, etc)
* Isotope: all atoms with the same atomic number and the same atomic mass are the same isotope. There are several isotopes of most elements. For instance, Carbon nuclei will always have 6 protons, but a Carbon-12 nucleus will have 6 neutrons, and Carbon-13 will have 7 neutrons. carbon-12 and Carbon-13 are examples of isotopes of Carbon.
* Isomer: for two nuclei to be the same isomer, they must have the same atomic number and atomic mass, and be in the same energy state.

#### Energy States

For a given isotope, there will be a number of discrete energy levels. Each nucleus of that isotope will exist in one of these energy states. These energy states are labelled such that state 0 is the lowest energy state, state 1 is the second lowest and so on. The energy difference between energy states is typically defined in units of keV (1keV = $1.6\times 10 ^{-16}$ J). If it isn't stated which energy state an isomer is, it is very likely the ground state is being referred to.

### Nuclear Decay

Many isomers are unstable and will decay to a lower energy isomer. This decay will emit one or more particles from the nucleus and may also emit some radiation. Dependent on which particle is emitted, the composition of the nucleus will change accordingly. A table below shows common types of particle which may be emitted and the change this causes to the structure of a nucleus.

| Decay Type      | Change to Atomic Number | Change to Atomic Mass |
| ----------- | ----------- | -- |
| Alpha Emission   | -2  | -4 |
| Beta emission      | +1  | 0  |
| Gamma Emission   | 0  | 0 |
| Electron capture   | -1  | 0 |


For each individual nuclei, it cannot be predicted exactly when it will decay. However, we may observe a large collection of isomers measure the timescales over which they decay occurs and observe which particles are emitted. Xenon-135 (written as Xe $^{135}$ ) decays via electron emission. Xenon has an atomic number of 54 so, consulting the table above, we see that it will turn into a nucleus with an atomic number of 55 and its atomic mass will remain unchanged at 135. This means a nucleus of Xe $^{135}$ will decay to form a nucleus of Cs $^{135}$ . 

We observe that, given a large sample of Xe $^{135}$ , half of the nuclei will have decayed to Cs $^{135}$ after 9.14 hours. As the number of Xe $^{135}$ nuclei that decay each second is proportional to the number of Xe $^{135}$ nuclei present, we may write equations which describe how the number of both Xe $^{135}$ and Cs $^{135}$ change over time due to this decay:

$$ \eqalign{
\frac{\mathrm{d}n_{Xe135}}{\mathrm{d}t} = - \lambda_{Xe135} n_{Xe135},\\
\frac{\mathrm{d}n_{Cs135}}{\mathrm{d}t} = \lambda_{Xe135} n_{Xe135},
}
$$

where $n_{Xe135}$ is the number of moles of Xe $^{135}$ present, $n_{Cs135}$ is the number of moles of Cs $^{135}$ present, $t$ is time and \lambda_{Xe135} is the decay rate of Xe $^{135}$ . For a given isomer, we may obtain its decay rate $\lambda$ from its half-life $t_{\frac{1}{2}}$ using the following equation:

$$
\lambda = \frac{\ln{2}}{t_{\frac{1}{2}}}.
$$

Note that the decay constant has units of s $^{-1}$ so the half-life should be converted into seconds before this calculation takes place. So, for Xe $^{135}$ , we get:

$$
\lambda_{Xe135} = \frac{0.6931}{9.14\mathrm{h} \times 3600\mathrm{sh}^{-1}} = 2.1065 \times 10 ^{-5} \mathrm{s}^{-1}.
$$

This means that, form every million nuclei of Xe $^{135}$ present, around 21 of them will decay each second.

We can return the differential equations we defined earlier for the rate of change of the number of moles of Xe $^{135}$ and Cs $^{135}$ and solve these by a number of different means to describe the number of moles of these two isotopes over a period of time. We can plot the number of moles of the isotopes present as a function of time giving an initial population of 1 mole of Xe $^{135}$ :

<p align="center">
  <img src="https://github.com/coolernato/Decay-Chains/blob/main/resources/Xe_135_Cs_135.jpg" />
</p>

The production of data like these can help us to predict the populations of radioactive isotopes in practical settings.

### The ENDF Decay Dataset

In order to perform simulations like this, we need data relating to how fast isomers decay and how the decay. There are several datasets available which provide this information. The ENDF dataset is provided by the [National Nuclear Data Centre (NNDC)](https://www.nndc.bnl.gov/sigma/index.jsp?as=239&lib=endfb7.0&nsub=10). The dataset as a whole contains a lot of information relating to various properties of different nuclei. Copies of the files relating to radioactive decay are included in the ```decay_data``` directory of this repository.

The filename for a given isomer is ```dec-```, followed by the atomic number of the isomer (padded with leading zeroes so it's three digits long), a ```_```, the atomic symbol for the element (e.g. ```He``` for Helium), another ```_```, then atomic mass of the isomer (padded with leading zeroes so it's three digits long), and finally ```.endf```. Files in this format all relate to the ground state isomers of an isotope. Files which correspond to a higher state have an additional ```m1``` for the first excited stated, ```m2``` for the second excited state and so on immediately before the ```.endf```. To give a few examples:

* Data relating to the ground state of Carbon-14 (atomic number 6) if found in ```dec-006_C_014.endf```
* Data relating to the ground state of Mendelevium-255 (atomic number 101) is found in ```dec-101_Md_255.endf```
* Data relating to the first excited state of Cadmium-111 (atomic number 48) is found in ```dec-048_Cd_111m1.endf```

Each data file contains a large amount of data, but don't be alarmed - most of it isn't relevant to this project. In fact, for now, we only care about two pieces of information in this file: the half-life and the decay mode. Let's examine the first few lines of the file ```dec-054_Xe_135.endf```:

<p align="center">
  <img src="https://github.com/coolernato/Decay-Chains/blob/main/resources/Xe-135-ENDF.png" />
</p>

In this file, we only care about the section highlighted in red. 

#### Obtaining the Half-Life

The line that has the phrase "Parent half-life" describes the half-life of Xe$^{135}$ by providing first the numerical value of 9.14, then the units ```H``` which refers to the number of hours. We can ignore the ```2``` following the ```H``` and the rest of the line.  The different characters to describe the units and the corresponding units are:

| Character     | Unit | Number of Seconds |
| ----------- | ----------- | -- |
| PS | Picoseconds  | $1\times 10^{-12}$ |
| NS | Nanoseconds  | $1\times 10^{-9}$ |
| US | Microseconds  | $1\times 10^{-6}$ |
| MS | Milliseconds  | $1\times 10^{-3}$ |
| S | Milliseconds  | $1$ |
| H | Hours  | $3.6\times 10^{3}$ |
| D | Days  | $8.64\times 10^{4}$ |
| Y | Years  | $3.1536\times 10^{7}$ |

Some files (such as ```dec-082_Pb_208.endf```) may also say ```Parent half-life: STABLE```. This means that the isomer does not decay at all.

#### Obtaining the Decay Mode

The decay mode is contained on the line beginning ```Decay mode:```. In the example above, the ```B-``` tells us Xe $^{135}$ decays by electron emission. There is more complexity to what may appear on this line but, for now, we can restrict ourselves to the following decay modes:

| ENDF Decay Code     | Decay Mode | 
| ----------- | ----------- |
| A | Alpha Emission  | 
| B- | Beta Emission  |
| EC | Electron Capture  |

## Activities

For each of the activities below, complete the code in your ```src``` directory in whatever way you wish, organising your code however you think makes most sense. The tasks are deliberately vague in terms of how the code should be organised, so use whatever structure of functions, classes, modules, etc that you think is best. 

For each activity there are tests in the ```tests``` directory which relate to the activity. For instance ```tests/test_1A``` contains the tests relating to Activity 1A. In order to allow these tests to check your code, you will need to edit the relevant functions in these file ```src/test_interfaces.py``` so they use your code. This should give you some more idea of what your code should do, as well allowing you to test that your code is working correctly.

As a reminder, these activities can be undertaken in parallel if you're working in a group, so feel free to split up on work on different activities together.

### Activity 1A

Write code able to solve differential equations such as those above in the "Nuclear Decay" section. We'll start with the simplest scenario - where Isomer 1 is decaying into Isomer 2, which is stable. Your code should be able to accept an initial number of moles of both isotopes and a decay rate for Isomer 1, then provide the number of moles of each isomer at a set of provided time-steps.

For example:
* If Isomer 1 has a decay rate of 0/s and an initial population of 10and values are requested at t=0, and t=100s: Isomer 1 should have a population of ```(10, 10)``` and Isomer 2 should have a population of ```(0, 0)```.
* If Isomer 1 has a decay rate of 5/s and an initial population of 2 and values are requested at t=0, t=0.5s and t=1s, Isomer 1 should have the populations ```(2, 0.164, 0.0135)``` and Isomer 2 should have the populations ```(0, 1.836, 1.9865)```

Hint: this type of problem is often referred to as an "initial value problem" as you have the initial state of the system and want to calculate the future states of the system by solving the ordinary differential equations forward in time.

### Activity 1B 

Write code able to read the ENDF data files and extract the half-life and decay mode of a given isomer. Given the name of a file (without any path prefix) your code should be able to open the file and find:
* the half-life and convert it to a decay rate in units of 1/s (noting this will be zero for stable isomers)
* the decay mode and so the effect this has on the atomic number, atomic mass, and energy state number of the decaying isomer. If the isomer is stable, the change on the atomic number and atomic mass should both be considered zero.

For instance:
* Providing the filename ```dec-002_He_004.endf``` should be found to have a decay rate of 0/s and a corresponding change to atomic number of 0 and atomic mass of 0
* Providing the filename ```dec-002_He_006.endf``` should be found to have a decay rate of $\frac{\ln{2}}{806.7\textrm{ms}}$ = 0.859/s and a corresponding change to atomic number of +1 and atomic mass of 0

### Activity 1C

It's important to be able to make conversions between different bits of data relating to the isomers. Write pieces of code which can:
* generate the name of the ENDF file name for an isomer from its atomic number, atomic mass, and energy group number,. For instance:
  * providing an atomic number of 8, atomic mass of 16 and an energy state of 0 should produce ```dec-008_O_016.endf```,
  * providing an atomic number of 21, atomic mass of 42 and an energy state of 1 should produce ```dec-021_Sc_042m1.endf```.
* generate the name of an isomer (e.g. ```Xe135``` or ```Na24m1```) from its atomic number, atomic mass, and energy group number. For instance:
  * providing an atomic number of 50, atomic mass of 120 and an energy state of 0 should produce ```Sn120```,
  * providing an atomic number of 56, atomic mass of 135 and an energy state of 1 should produce ```Ba135m1.endf```.
* generate the atomic number, atomic mass and energy state number of an isomer given its name. For instance:
  * providing a name of ```Au197``` should produce an atomic number of 79, atomic mass of ```197``` and energy state of ```0```
  * providing a name of ```Cu70m2``` should produce an atomic number of 29, atomic mass of ```70``` and energy state of ```2```
