import mido
import requests

from time import sleep

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 5005)


# Replace 'Your MIDI Port Name' with the exact name of your virtual MIDI port
midi_port_name = 'LoopBe Internal MIDI 0'  # Example: 'loopMIDI Port'
bhaptics_url = 'http://localhost:15881/api/tactile'



def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        print(f"Note On: {note}, Velocity: {velocity}")

        # Convert note and velocity to haptic feedback
        intensity = velocity / 127.0  # Scale velocity to [0, 1]

        # Example: send simple pulse feedback to bHaptics
        haptic_feedback = {
            "key": "example",
            "intensity": intensity,
            "durationMillis": 100,  # duration in milliseconds
            "actuator": "all"
        }
        response = requests.post(bhaptics_url, json=haptic_feedback)
        print(response.status_code, response.text)

def main():
    # Open the MIDI input port
    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            print(message)
            handle_midi_message(message)

if __name__ == "__main__":
    main()
