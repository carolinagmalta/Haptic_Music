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
    return base_mapping[note % 12]  # Use modulo to map notes from other octaves

# Open the MIDI input port
with mido.open_input(midi_port_name) as inport:
    for msg in inport:
        if msg.type == 'note_on':
            # Map the note to an actuator index
            index = get_actuator_index(msg.note)
            # Prepare the data to be sent
            data = {
                'index': index,
               # 'intensity': msg.velocity,  # This can be changed as needed
                'intensity': msg,  # This can be changed as needed

                'duration': int(msg.time * 1000)  # Convert time to milliseconds
            }
            # Print the data
            print(f"Sending data to Bhaptics Tactsuit: {data}")
            # Send a request to the Bhaptics API to activate the actuator
            requests.post(bhaptics_url, json=data)