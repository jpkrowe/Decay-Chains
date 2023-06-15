import unittest
import src.test_interfaces as interface
import math

class Test_1B(unittest.TestCase):
    '''
    Tests the code produced for Activity 1B
    '''
    def test_stable(self):
        '''
        Tests if the correct answer is returned when the isomer is stable
        '''
        filename = "dec-001_H_001.endf"

        decay_rate, decay_atomic_number_change, decay_atomic_mass_change = interface.task_1b_decay_data_from_filename(filename)

        self.assertAlmostEqual(decay_rate, 0.0)
        self.assertEqual(decay_atomic_number_change, 0)
        self.assertEqual(decay_atomic_mass_change, 0)

    def test_alpha(self):
        '''
        Tests if the correct answer is returned when the isomer decays via alpha decay
        '''
        filename = "dec-086_Rn_220.endf"

        decay_rate, decay_atomic_number_change, decay_atomic_mass_change = interface.task_1b_decay_data_from_filename(filename)

        self.assertAlmostEqual(decay_rate, math.log(2) / 55.6)
        self.assertEqual(decay_atomic_number_change, -2)
        self.assertEqual(decay_atomic_mass_change, -2)

    def test_beta(self):
        '''
        Tests if the correct answer is returned when the isomer decays via beta decay
        Also tests correct unit conversion for half-life in years
        '''
        filename = "dec-006_C_014.endf"

        decay_rate, decay_atomic_number_change, decay_atomic_mass_change = interface.task_1b_decay_data_from_filename(filename)

        self.assertAlmostEqual(decay_rate, math.log(2) / (5700 * 3.1536e7))
        self.assertEqual(decay_atomic_number_change, 1)
        self.assertEqual(decay_atomic_mass_change, 0)

    def test_electron_capture(self):
        '''
        Tests if the correct answer is returned when the isomer decays via electron capture
        Also tests correct unit conversion for half-life in milliseconds
        '''
        filename = "dec-026_Fe_051.endf"

        decay_rate, decay_atomic_number_change, decay_atomic_mass_change = interface.task_1b_decay_data_from_filename(filename)

        self.assertAlmostEqual(decay_rate, math.log(2) / (0.305))
        self.assertEqual(decay_atomic_number_change, -1)
        self.assertEqual(decay_atomic_mass_change, 0)