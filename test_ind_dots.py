"""
import mido
import requests

from time import sleep

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 5005)

# Replace 'Your MIDI Port Name' with the exact name of your virtual MIDI port
midi_port_name = 'LoopBe Internal MIDI 0'
bhaptics_url = 'http://localhost:15881/api/tactile'

# Function to map MIDI note to actuator index
def get_actuator_index(note):
    # Define a base mapping for one octave (C to B)
    base_mapping = {
        0: 0,  # C
        2: 1,  # D
        4: 2,  # E
        5: 3,  # F
        7: 4,  # G
        9: 5,  # A
        11: 6  # B
    }
    # Calculate the note within an octave (C is 0, C# is 1, ..., B is 11)
    note_in_octave = note % 12
    # Use the base mapping to get the actuator index, adding an offset for the octave
    if note_in_octave in base_mapping:
        return base_mapping[note_in_octave] + (note // 12) * 7
    else:
        return None  # Return None if the note does not map to a defined actuator

def send_haptic_feedback(note, intensity):
    actuator = get_actuator_index(note)
    if actuator is not None:
        haptic_feedback = {
            "key": f"note_{note}",
            "durationMillis": 100,  # duration in milliseconds
            "positions": [{"index": actuator, "intensity": intensity}]
        }
        response = requests.post(bhaptics_url, json=haptic_feedback)
        print(response.status_code, response.text)

def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        print(f"Note On: {note}, Velocity: {velocity}")

        # Convert velocity to intensity
        intensity = velocity / 127.0  # Scale velocity to [0, 1]

        # Send haptic feedback to the specific actuator
        send_haptic_feedback(note, intensity)
        print(note, intensity)

def main():
    # Open the MIDI input port
    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            print(message)
            handle_midi_message(message)

if __name__ == "__main__":
    main()

    """
    
    
    
import mido
import requests
from pythonosc import udp_client

# Setup UDP client for OSC communication (if needed)
client = udp_client.SimpleUDPClient("127.0.0.1", 5005)

# Replace 'Your MIDI Port Name' with the exact name of your virtual MIDI port
midi_port_name = 'LoopBe Internal MIDI 0'
bhaptics_url = 'http://localhost:15881/api/tactile'

# Function to map MIDI note to actuator index
def get_actuator_index(note):
    # Define a base mapping for one octave (C to B)
    base_mapping = {
        0: 0,  # C
        2: 1,  # D
        4: 2,  # E
        5: 3,  # F
        7: 4,  # G
        9: 5,  # A
        11: 6  # B
    }
    # Calculate the note within an octave (C is 0, C# is 1, ..., B is 11)
    note_in_octave = note % 12
    # Use the base mapping to get the actuator index, adding an offset for the octave
    if note_in_octave in base_mapping:
        return base_mapping[note_in_octave] + (note // 12) * 7
    else:
        return None  # Return None if the note does not map to a defined actuator

def send_haptic_feedback(note, intensity):
    actuator = get_actuator_index(note)
    if actuator is not None:
        haptic_feedback = {
            "key": f"note_{note}",
            "durationMillis": 100,  # duration in milliseconds
           # "positions": [{"index": actuator, "intensity": intensity}]
            "positions": [{"index": actuator}]

        }
        response = requests.post(bhaptics_url, json=haptic_feedback)
        print(response.status_code, response.text)

def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        print(f"Note On: {note}, Velocity: {velocity}")

        # Convert velocity to intensity
        intensity = velocity / 127.0  # Scale velocity to [0, 1]
        # Send haptic feedback to the specific actuator
        send_haptic_feedback(note, intensity)
        print(note, intensity)
        #send_haptic_feedback(note)
        #print(note)
        
        
def main():
    # Open the MIDI input port
    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            print(message)
            handle_midi_message(message)

if __name__ == "__main__":
    main()
