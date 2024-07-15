#TEST MIDI PORTS
#import mido
# List available MIDI input ports
#print("Available MIDI input ports:")
#for name in mido.get_input_names():
#   print(name)
    
    
#TEST GET ACTUATORS
"""
import unittest
from test_ind_dots import get_actuator_index

# Define base_mapping in this file, or import it from the module where it's defined
base_mapping = {
    # Add your note-index pairs here
}

class TestGetActuatorIndex(unittest.TestCase):
    def test_base_mapping(self):
        for note, expected_index in base_mapping.items():
            with self.subTest(note=note):
                self.assertEqual(get_actuator_index(note), expected_index)

    def test_not_in_base_mapping(self):
        # Choose a note that's not in the base mapping
        note = 1
        self.assertIsNone(get_actuator_index(note))

    def test_outside_midi_range(self):
        # Choose a note outside the valid MIDI range
        note = -1
        self.assertEqual(get_actuator_index(note), -1)
if __name__ == '__main__':
    unittest.main()
    """