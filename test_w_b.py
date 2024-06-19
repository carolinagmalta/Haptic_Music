import mido
import requests
from time import sleep
from pythonosc import udp_client
from bhaptics.haptic_player import HapticPlayer

# Initialize BhapticsPlayer
player = HapticPlayer()

# Ensure the player is connected
if not player.is_connected():
    print("Player is not connected.")
    exit()

# Define mappings for each octave
note_to_actuator = {
    # Octave 1
    24: [1, 2, 3, 7], 26: [1, 2, 7], 28: [1, 2, 3, 6], 29: [1, 2, 3, 6, 7], 31: [1, 2, 6, 7], 33: [1, 3, 6], 35: [1, 3, 6, 7],
    # Octave 2
    36: [1, 5, 2, 3, 7], 38: [1, 5, 2, 7], 40: [1, 5, 2, 3, 6], 41: [1, 5, 2, 3, 6, 7], 43: [1, 5, 2, 6, 7], 45: [1, 5, 3, 6], 47: [1, 5, 3, 6, 7],
    # Octave 3
    48: [1, 5, 9, 2, 3, 7], 50: [1, 5, 9, 2, 7], 52: [1, 5, 9, 2, 3, 6], 53: [1, 5, 9, 2, 3, 6, 7], 55: [1, 5, 9, 2, 6, 7], 57: [1, 5, 9, 3, 6], 59: [1, 5, 9, 3, 6, 7],
    # Octave 4
    60: [5, 2, 3, 7], 62: [5, 2, 7], 64: [5, 2, 3, 6], 65: [5, 2, 3, 6, 7], 67: [5, 2, 6, 7], 69: [5, 3, 6], 71: [5, 3, 6, 7],
    # Octave 5
    72: [1, 9, 2, 3, 7], 74: [1, 9, 2, 7], 76: [1, 9, 2, 3, 6], 77: [1, 9, 2, 3, 6, 7], 79: [1, 9, 2, 6, 7], 81: [1, 9, 3, 6], 83: [1, 9, 3, 6, 7],
    # Octave 6
    84: [5, 9, 2, 3, 7], 86: [5, 9, 2, 7], 88: [5, 9, 2, 3, 6], 89: [5, 9, 2, 3, 6, 7], 91: [5, 9, 2, 6, 7], 93: [5, 9, 3, 6], 95: [5, 9, 3, 6, 7],
    # Octave 7
    96: [9, 2, 3, 7], 98: [9, 2, 7], 100: [9, 2, 3, 6], 101: [9, 2, 3, 6, 7], 103: [9, 2, 6, 7], 105: [9, 3, 6], 107: [9, 3, 6, 7]
}

# Convert velocity to intensity (0-100 scale)
def velocity_to_intensity(velocity):
    return int((velocity / 127.0) * 100)

def send_haptic_feedback(note, intensity):
    if note in note_to_actuator:
        actuators = note_to_actuator[note]
        for actuator in actuators:
            dot_frame = {
                "Position": "VestBack",
                "DotPoints": [
                    {"Index": actuator, "Intensity": intensity}
                ],
                "DurationMillis": 500  # Example duration
            }
            player.submit("dotPoint", dot_frame)

def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        print(f"Note On: {note}, Velocity: {velocity}")

        # Convert velocity to intensity
        intensity = velocity_to_intensity(velocity)

        # Send haptic feedback
        send_haptic_feedback(note, intensity)

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
