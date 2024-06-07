import mido
import requests
from time import sleep
from pythonosc import udp_client
from bhaptics.haptic_player import HapticPlayer

# Setup UDP client for OSC communication (if needed)
client = udp_client.SimpleUDPClient("127.0.0.1", 5005)

# Replace 'Your MIDI Port Name' with the exact name of your virtual MIDI port
midi_port_name = 'LoopBe Internal MIDI 0'
bhaptics_url = 'http://localhost:15881/api/tactile'

# Mapping of MIDI notes to actuators (for all C, D, E, F, G, A, B notes across all octaves)
#DEFAULT
"""note_to_actuator = {
    # C notes
    0: 0, 12: 0, 24: 0, 36: 0, 48: 0, 60: 0, 72: 0, 84: 0, 96: 0, 108: 0,
    # D notes
    2: 1, 14: 1, 26: 1, 38: 1, 50: 1, 62: 1, 74: 1, 86: 1, 98: 1, 110: 1,
    # E notes
    4: 2, 16: 2, 28: 2, 40: 2, 52: 2, 64: 2, 76: 2, 88: 2, 100: 2, 112: 2,
    # F notes
    5: 3, 17: 3, 29: 3, 41: 3, 53: 3, 65: 3, 77: 3, 89: 3, 101: 3, 113: 3,
    # G notes
    7: 4, 19: 4, 31: 4, 43: 4, 55: 4, 67: 4, 79: 4, 91: 4, 103: 4, 115: 4,
    # A notes
    9: 5, 21: 5, 33: 5, 45: 5, 57: 5, 69: 5, 81: 5, 93: 5, 105: 5, 117: 5,
    # B notes
    11: 6, 23: 6, 35: 6, 47: 6, 59: 6, 71: 6, 83: 6, 95: 6, 107: 6, 119: 6
}"""

#CASO 1 DIAGONAL
"""
note_to_actuator = {
    # C notes
    0: 16, 12: 16, 24: 16, 36: 16, 48: 16, 60: 16, 72: 16, 84: 16, 96: 16, 108: 16,
    # D notes
    2: 13, 14: 13, 26: 13, 38: 13, 50: 13, 62: 13, 74: 13, 86: 13, 98: 13, 110: 13,
    # E notes
    4: 10, 16: 10, 28: 10, 40: 10, 52: 10, 64: 10, 76: 10, 88: 10, 100: 10, 112: 10,
    # F notes
    5: 7, 17: 7, 29: 7, 41: 7, 53: 7, 65: 7, 77: 7, 89: 7, 101: 7, 113: 7,
    # G notes
    7: 8, 19: 8, 31: 8, 43: 8, 55: 8, 67: 8, 79: 8, 91: 8, 103: 8, 115: 8,
    # A notes
    9: 5, 21: 5, 33: 5, 45: 5, 57: 5, 69: 5, 81: 5, 93: 5, 105: 5, 117: 5,
    # B notes
    11: 2, 23: 2, 35: 2, 47: 2, 59: 2, 71: 2, 83: 2, 95: 2, 107: 2, 119: 2
}
"""
#CASO 2 U INVERTIDO
note_to_actuator = {
    # C notes
    0: 12, 12: 12, 24: 12, 36: 12, 48: 12, 60: 12, 72: 12, 84: 12, 96: 12, 108: 12,
    # D notes
    2: 8, 14: 8, 26: 8, 38: 8, 50: 8, 62: 8, 74: 8, 86: 8, 98: 8, 110: 8,
    # E notes
    4: 4, 16: 4, 28: 4, 40: 4, 52: 4, 64: 4, 76: 4, 88: 4, 100: 4, 112: 4,
    # F notes
    5: 1, 17: 1, 29: 1, 41: 1, 53: 1, 65: 1, 77: 1, 89: 1, 101: 1, 113: 1,
    # G notes
    7: 2, 19: 2, 31: 2, 43: 2, 55: 2, 67: 2, 79: 2, 91: 2, 103: 2, 115: 2,
    # A notes
    9: 7, 21: 7, 33: 7, 45: 7, 57: 7, 69: 7, 81: 7, 93: 7, 105: 7, 117: 7,
    # B notes
    11: 11, 23: 11, 35: 11, 47: 11, 59: 11, 71: 11, 83: 11, 95: 11, 107: 11, 119: 11
}

note_to_actuator_2 = {
    0:12, 2:8, 4: 4, 5: 1, 7: 2,9:7, 11:11
}
# expandir para todas as oitavas
for key in note_to_actuator_2:
    for i in range(10):
        note_to_actuator_2[key+12*i] = note_to_actuator_2[key]



# Function to send haptic feedback
player = HapticPlayer()  # Create an instance of the HapticPlayer class

def send_haptic_feedback(note, intensity):
    if note in note_to_actuator:
        actuator = note_to_actuator[note]
        dot_frame = {
            "Position": "VestBack",
            "DotPoints": [
                {"Index": actuator, "Intensity": intensity}
            ],
            "DurationMillis": 1000
        }
        player.submit("dotPoint", dot_frame)  # Call the submit method on the player instance

# Handle incoming MIDI messages
def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        print(f"Note On: {note}, Velocity: {velocity}")
        
        # Convert velocity to intensity (0-100 scale)
        intensity = int((velocity / 127.0) * 100)
        
        # Send haptic feedback
        send_haptic_feedback(note, intensity)

# Main function to listen to MIDI input
def main():
    # Replace 'Your MIDI Port Name' with the name of your MIDI port
    midi_port_name = 'LoopBe Internal MIDI 0'
   

    # Open the MIDI input port
    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            print(message)
            handle_midi_message(message)

if __name__ == "__main__":
    main()
