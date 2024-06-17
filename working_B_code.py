import mido
from time import time
from bhaptics import BhapticsPlayer

player = BhapticsPlayer()

#bhaptics connection
if not player.is_connected():
    print("Player is not connected.")
    exit()
    
# list of oct and the actuators 

oct1 ={
	24: [1,2,3,7], 26: [1,2,7], 28: [1,2,3,6], 29: [1,2,3,6,7], 31: [1,2,6,7], 33: [1,3,6], 35: [1,3,6,7]
}
oct2 = {
	36: [1,5,2,3,7], 38: [1,5,2,7], 40: [1,5,2,3,6], 41: [1,5,2,3,6,7], 43: [1,5,2,6,7], 45: [1,5,3,6], 47: [1,5,3,6,7]
}
oct3 = {
	48: [1,5,9,2,3,7], 50: [1,5,9,2,7], 52: [1,5,9,2,3,6], 53: [1,5,9,2,3,6,7], 55: [1,5,9,2,6,7], 57: [1,5,9,3,6], 59: [1,5,9,3,6,7]
}
oct4 = {
	60: [5,2,3,7], 62: [5,2,7], 64: [5,2,3,6], 65: [5,2,3,6,7], 67: [5,2,6,7], 69: [5,3,6], 71: [5,3,6,7]
}
oct5 = {
	72: [1,9,2,3,7], 74: [1,9,2,7], 76: [1,9,2,3,6], 77: [1,9,2,3,6,7], 79: [1,9,2,6,7], 81: [1,9,3,6], 83: [1,9,3,6,7]
}
oct6 = {
	84: [5,9,2,3,7], 86: [5,9,2,7], 88: [5,9,2,3,6], 89: [5,9,2,3,6,7], 91: [5,9,2,6,7], 93: [5,9,3,6], 95: [5,9,3,6,7]
}
oct7 = {
	96: [9,2,3,7], 98: [9,2,7], 100: [9,2,3,6], 101: [9,2,3,6,7], 103: [9,2,6,7], 105: [9,3,6], 107: [9,3,6,7]
}

#making a list of lists
note_to_actuator = {**oct1, **oct2, **oct3, **oct4, **oct5, **oct6, **oct7}
note_on_times = {}

# Function to send to suit
def send_haptic_feedback(note, intensity, duration):
    if note in note_to_actuator:
        actuators = note_to_actuator[note]
        dot_points = [{"Index": actuator, "Intensity": intensity} for actuator in actuators]
        dot_frame = {
            "Position": "VestBack", 
            "DotPoints": dot_points,
            "DurationMillis": duration
        }
        player.submit("dotPoint", dot_frame)

# Midi messsage
def handle_midi_message(message):
    if message.type == 'note_on':
        note = message.note
        velocity = message.velocity
        note_on_times[note] = time()
        print(f"Note On: {note}, Velocity: {velocity}")

    elif message.type == 'note_off':
        note = message.note
        if note in note_on_times:
            duration = int((time() - note_on_times[note]) * 1000)  # Calculate duration in milliseconds
            del note_on_times[note]
            intensity = int((message.velocity / 127.0) * 100)  # Convert velocity to intensity (0-100 scale)
            print(f"Note Off: {note}, Duration: {duration} ms, Intensity: {intensity}")
            # Send haptic feedback
            send_haptic_feedback(note, intensity, duration)

# Connection
def main():
    midi_port_name = 'LoopBe Internal MIDI 0'

    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            print(message)
            handle_midi_message(message)

if __name__ == "__main__":
    main()
