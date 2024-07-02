import mido
import requests
from time import sleep
from pythonosc import udp_client
from bhaptics.haptic_player import HapticPlayer

"""
para atualizar o codigo, basta correr o comando:
`git add *.py`
depois:
`git commit -m "mensagem"`
e por fim:
`git push origin main`
e dar a senha da chave ssh
"""



# Setup UDP client for OSC communication (if needed)
client = udp_client.SimpleUDPClient("127.0.0.1", 5005)

# Replace 'Your MIDI Port Name' with the exact name of your virtual MIDI port
midi_port_name = 'LoopBe Internal MIDI 0'
bhaptics_url = 'http://localhost:15881/api/tactile'

# Mapping of MIDI notes to actuators (for all C, D, E, F, G, A, B notes across all octaves)
#CASO 1 DIAGONAL
"""
note_to_actuator = {
    0: 16, 2: 13, 4: 10, 5: 7, 7: 8, 9: 5, 11: 2
}
note_keys = list(note_to_actuator.keys())
# expandir para todas as oitavas
for key in note_keys:
    for i in range(10):
        note_to_actuator[key+12*i] = note_to_actuator[key]
"""

#CASO 2 U INVERTIDO
"""
note_to_actuator = {
    0: 12, 2: 8, 4: 4, 5: 1, 7: 2, 9: 7, 11: 11
}
note_keys = list(note_to_actuator.keys())
# expandir para todas as oitavas
for key in note_keys:
    for i in range(10):
        note_to_actuator[key+12*i] = note_to_actuator[key]
"""

#CASO 3 L INVERTIDO
"""
note_to_actuator = {
    0: 16, 2: 12, 4: 8, 5: 4, 7: 0, 9: 1, 11: 2
}
note_keys = list(note_to_actuator.keys())
# expandir para todas as oitavas
for key in note_keys:
    for i in range(10):
        note_to_actuator[key+12*i] = note_to_actuator[key]
"""

#CASO 4 L ESPELHADO
"""
note_to_actuator = {
    0: 17, 2: 18, 4: 19, 5: 15, 7: 11, 9: 7, 11: 3
}
note_keys = list(note_to_actuator.keys())
# expandir para todas as oitavas
for key in note_keys:
    for i in range(10):
        note_to_actuator[key+12*i] = note_to_actuator[key]
"""

#CASO 5 TWO LINE
#"""
note_to_actuator = {
    0: 12, 2: 8, 4: 4, 5: 0, 7: 15, 9: 11, 11: 7
}
note_keys = list(note_to_actuator.keys())
# expandir para todas as oitavas
for key in note_keys:
    for i in range(10):
        note_to_actuator[key+12*i] = note_to_actuator[key]
#"""

# Function to send haptic feedback
player = HapticPlayer()  # Create an instance of the HapticPlayer class

def send_haptic_feedback(note, intensity):
    if note in note_to_actuator: #mudar mediante o caso
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
