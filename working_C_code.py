import mido
from time import sleep, time
from bhaptics.haptic_player import HapticPlayer

player = HapticPlayer()

# List of octave superior placement
note_to_actuator = {
    'oct1': {
         "semibreve": {24: [9, 10, 11, 15, 18, 19], 26: [9, 10, 15, 18, 19], 28: [9, 10, 11, 14, 18, 19], 29: [9, 10, 11, 14, 15, 18, 19], 31: [9, 10, 14, 15, 18, 19], 33: [9, 11, 14, 18, 19], 35: [9, 11, 14, 15, 18, 19]},
         "minim": {24: [9, 10, 11, 15, 18], 26: [9, 10, 15, 18], 28: [9, 10, 11, 14, 18], 29: [9, 10, 11, 14, 15, 18], 31: [9, 10, 14, 15, 18], 33: [9, 11, 14, 18], 35: [9, 11, 14, 15, 18]},
         "crotchet": {24: [9, 10, 11, 15, 19], 26: [9, 10, 15, 19], 28: [9, 10, 11, 14, 19], 29: [9, 10, 11, 14, 15, 19], 31: [9, 10, 14, 15, 19], 33: [9, 11, 14, 19], 35: [9, 11, 14, 15, 19]},
         "quaver": {24: [9, 10, 11, 15], 26: [9, 10, 15], 28: [9, 10, 11, 14], 29: [9, 10, 11, 14, 15], 31: [9, 10, 14, 15], 33: [9, 11, 14], 35: [9, 11, 14, 15]}
     },
     'oct2': {
         "semibreve": {36: [9, 13, 10, 11, 15, 18, 19], 38: [9, 13, 10, 15, 18, 19], 40: [9, 13, 10, 11, 14, 18, 19], 41: [9, 13, 10, 11, 14, 15, 18, 19], 43: [9, 13, 10, 14, 15, 18, 19], 45: [9, 13, 11, 14], 47: [9, 13, 11, 14, 15]},
         "minim": {36: [9, 13, 10, 11, 15, 18], 38: [9, 13, 10, 15, 18], 40: [9, 13, 10, 11, 14, 18], 41: [9, 13, 10, 11, 14, 15, 18], 43: [9, 13, 10, 14, 15, 18], 45: [9, 13, 11, 14], 47: [9, 13, 11, 14, 15]},
         "crotchet": {36: [9, 13, 10, 11, 15, 19], 38: [9, 13, 10, 15, 19], 40: [9, 13, 10, 11, 14, 19], 41: [9, 13, 10, 11, 14, 15, 19], 43: [9, 13, 10, 14, 15, 19], 45: [9, 13, 11, 14], 47: [9, 13, 11, 14, 15]},
         "quaver": {36: [9, 13, 10, 11, 15], 38: [9, 13, 10, 15], 40: [9, 13, 10, 11, 14], 41: [9, 13, 10, 11, 14, 15], 43: [9, 13, 10, 14, 15], 45: [9, 13, 11, 14], 47: [9, 13, 11, 14, 15]}
     },
    'oct3': {
         "semibreve": {48: [9, 13, 17, 10, 11, 15, 18, 19], 50: [9, 13, 17, 10, 15, 18, 19], 52: [9, 13, 17, 10, 11, 14, 18, 19], 53: [9, 13, 17, 10, 11, 14, 15, 18, 19], 55: [9, 13, 17, 10, 14, 15, 18, 19], 57: [9, 13, 17, 11, 14, 18, 19], 59: [9, 13, 17, 11, 14, 15, 18, 19]},
         "minim": {48: [9, 13, 17, 10, 11, 15, 18], 50: [9, 13, 17, 10, 15, 18], 52: [9, 13, 17, 10, 11, 14, 18], 53: [9, 13, 17, 10, 11, 14, 15, 18], 55: [9, 13, 17, 10, 14, 15, 18], 57: [9, 13, 17, 11, 14, 18], 59: [9, 13, 17, 11, 14, 15, 18]},
         "crotchet": {48: [9, 13, 17, 10, 11, 15, 19], 50: [9, 13, 17, 10, 15, 19], 52: [9, 13, 17, 10, 11, 14, 19], 53: [9, 13, 17, 10, 11, 14, 15, 19], 55: [9, 13, 17, 10, 14, 15, 19], 57: [9, 13, 17, 11, 14, 19], 59: [9, 13, 17, 11, 14, 15, 19]},
         "quaver": {48: [9, 13, 17, 10, 11, 15], 50: [9, 13, 17, 10, 15], 52: [9, 13, 17, 10, 11, 14], 53: [9, 13, 17, 10, 11, 14, 15], 55: [9, 13, 17, 10, 14, 15], 57: [9, 13, 17, 11, 14], 59: [9, 13, 17, 11, 14, 15]}
    },
    'oct4': {
         "semibreve": {60: [13, 10, 11, 15, 18, 19], 62: [13, 10, 15, 18, 19], 64: [13, 10, 11, 14, 18, 19], 65: [13, 10, 11, 14, 15, 18, 19], 67: [13, 10, 14, 15, 18, 19], 69: [13, 11, 14, 18, 19], 71: [13, 3, 11, 14, 15, 18, 19]},
         "minim": {60: [13, 10, 11, 15, 18], 62: [13, 10, 15, 18], 64: [13, 10, 11, 14, 18], 65: [13, 10, 11, 14, 15, 18], 67: [13, 10, 14, 15, 18], 69: [13, 11, 14, 18], 71: [13, 3, 11, 14, 15, 18]},
         "crotchet": {60: [13, 10, 11, 15, 19], 62: [13, 10, 15, 19], 64: [13, 10, 11, 14, 19], 65: [13, 10, 11, 14, 15, 19], 67: [13, 10, 14, 15, 19], 69: [13, 11, 14, 19], 71: [13, 3, 11, 14, 15, 19]},
         "quaver": {60: [13, 10, 11, 15], 62: [13, 10, 15], 64: [13, 10, 11, 14], 65: [13, 10, 11, 14, 15], 67: [13, 10, 14, 15], 69: [13, 11, 14], 71: [13, 3, 11, 14, 15]}
     },
     'oct5': {
         "semibreve": {72: [9, 17, 10, 11, 15, 18, 19], 74: [9, 17, 10, 15, 18, 19], 76: [9, 17, 10, 11, 14, 18, 19], 77: [9, 17, 10, 11, 14, 15, 18, 19], 79: [9, 17, 10, 14, 15, 18, 19], 81: [9, 17, 11, 14, 18, 19], 83: [9, 17, 11, 14, 15, 18, 19]},
         "minim": {72: [9, 17, 10, 11, 15, 18], 74: [9, 17, 10, 15, 18], 76: [9, 17, 10, 11, 14, 18], 77: [9, 17, 10, 11, 14, 15, 18], 79: [9, 17, 10, 14, 15, 18], 81: [9, 17, 11, 14, 18], 83: [9, 17, 11, 14, 15, 18]},
         "crotchet": {72: [9, 17, 10, 11, 15, 19], 74: [9, 17, 10, 15, 19], 76: [9, 17, 10, 11, 14, 19], 77: [9, 17, 10, 11, 14, 15, 19], 79: [9, 17, 10, 14, 15, 19], 81: [9, 17, 11, 14, 19], 83: [9, 17, 11, 14, 15, 19]},
         "quaver": {72: [9, 17, 10, 11, 15], 74: [9, 17, 10, 15], 76: [9, 17, 10, 11, 14], 77: [9, 17, 10, 11, 14, 15], 79: [9, 17, 10, 14, 15], 81: [9, 17, 11, 14], 83: [9, 17, 11, 14, 15]}
     },
     'oct6': {
         "semibreve": {84: [13,17,10,11,15,18, 19], 86: [13,17,10,15,18, 19], 88: [13,17,10,11,14,18, 19], 89: [13,17,10,11,14,15,18, 19], 91: [13,17,10,14,15,18, 19], 93: [13,17,11,14,18, 19], 95: [13,17,11,14,15,18, 19]},
         "minim": {84: [13,17,10,11,15, 18], 86: [13,17,10,15, 18], 88: [13,17,10,11,14, 18], 89: [13,17,10,11,14,15, 18], 91: [13,17,10,14,15, 18], 93: [13,17,11,14, 18], 95: [13,17,11,14,15, 18]},
         "crotchet": {84: [13,17,10,11,15, 19], 86: [13,17,10,15, 19], 88: [13,17,10,11,14, 19], 89: [13,17,10,11,14,15, 19], 91: [13,1710,14,15, 19], 93: [13,17,11,14, 19], 95: [13,17,11,14,15, 19]},
         "quaver": {84: [13,17,10,11,15], 86: [13,17,10,15], 88: [13,17,10,11,14], 89: [13,17,10,11,14,15], 91: [13,1710,14,15], 93: [13,17,11,14], 95: [13,17,11,14,15]}
     },
     'oct7': {
         "semibreve": {96: [17,10,11,15,18, 19], 98: [17,10,15,18, 19], 100: [17,10,11,14,18, 19], 101: [17,10,11,14,15,18, 19], 103: [17,10,14,15,18, 19], 105: [17,11,14,18, 19], 107: [17,11,14,15,18, 19]},
         "minim":{96: [17,10,11,15, 18], 98: [17,10,15, 18], 100: [17,10,11,14, 18], 101: [17,10,11,14,15, 18], 103: [17,10,14,15, 18], 105: [17,11,14, 18], 107: [17,11,14,15, 18]},
         "crotchet": {96: [17,10,11,15, 19], 98: [17,10,15, 19], 100: [17,10,11,14, 19], 101: [17,10,11,14,15, 19], 103: [17,10,14,15, 19], 105: [17,11,14, 19], 107: [17,11,14,15, 19]},
         "quaver": {96: [17,10,11,15], 98: [17,10,15], 100: [17,10,11,14], 101: [17,10,11,14,15], 103: [17,10,14,15], 105: [17,11,14], 107: [17,11,14,15]}
     }
}

note_on_times = {}

note_duration_to_time = {
    'semibreve': 4000,  # 4 seconds
    'minim': 2000,      # 2 seconds
    'crotchet': 1000,   # 1 second
    'quaver': 500,       # 0.5 seconds
    "zero":0
}

def send_haptic_feedback(note, intensity, note_duration):
    print(f"Sending haptic feedback for {note} with intensity {intensity} based on {note_duration} duration - 1.")
    octave_key = f"oct{note // 12+1}"
    print(f"octave_key: {octave_key}")
        

    if octave_key in note_to_actuator and note in note_to_actuator[octave_key][note_duration]:
        intensity = int(intensity * 1)  # Adjust the intensity value
        actuators = note_to_actuator[octave_key][note]
        duration_ms = note_duration_to_time.get(note_duration, 1000)  # Default to 1 second if not found
        dot_points = [{"Index": actuator, "Intensity": intensity} for actuator in actuators]
        dot_frame = {
            "Position": "VestBack",
            "DotPoints": dot_points,
            "DurationMillis": duration_ms  # Fixed duration for now
        }
        print(f"Sending haptic feedback for {note} with intensity {intensity} for {duration_ms}ms based on {note_duration} duration.")
        player.submit("dotPoint", dot_frame)
        # Exit the loop after handling the note
            
"""        
def handle_midi_message(message, base_intensity):
    global intensity
    velocity = message.velocity
    if message.type == 'note_on':
        note = message.note
        if velocity > 100:
            intensity = base_intensity * 1.25
            duration = "semibreve"
        elif velocity > 75:
            intensity = base_intensity
            duration = "minim"
        elif velocity > 50:
            intensity = base_intensity * 0.75
            duration = "crotchet"
        elif velocity > 0:
            intensity = base_intensity * 0.5
            duration = "quaver"
        # Convert velocity to a modifier (0-1 scale)
        velocity_modifier = velocity / 127.0
        # Calculate final intensity by applying the velocity modifier to the base intensity
        final_intensity = int(base_intensity * velocity_modifier)
        # Store note on time for duration calculation
        note_on_times[note] = time()
        # Send haptic feedback with the calculated final intensity
        send_haptic_feedback(note, final_intensity, 0)  # Use 0 for duration initially
    elif message.type == 'note_off':
        note = message.note
        if note in note_on_times:
            duration = int((time() - note_on_times[note]) * 1000) 
            velocity = message.velocity
            print(f"Note On: {note}, Velocity: {velocity}")
            send_haptic_feedback(note, 0, duration) 
            """
def handle_midi_message(message, base_intensity):
    global intensity
    duration = 0  # Initialize duration to 0

    if message.type == 'note_on':
        note = message.note
        velocity = getattr(message, 'velocity', 0)  # Safely get velocity, default to 0 if not present

        if velocity > 100:
            intensity = base_intensity * 1.25
            duration = "semibreve"
        elif velocity > 75:
            intensity = base_intensity
            duration = "minim"
        elif velocity > 50:
            intensity = base_intensity * 0.75
            duration = "crotchet"
        elif velocity > 0:
            intensity = base_intensity * 0.5
            duration = "quaver"

        # Convert velocity to a modifier (0-1 scale)
        velocity_modifier = velocity / 127.0
        # Calculate final intensity by applying the velocity modifier to the base intensity
        final_intensity = int(base_intensity * velocity_modifier)
        # Store note on time for duration calculation
        note_on_times[note] = time()
        # Send haptic feedback with the calculated final intensity
        send_haptic_feedback(note, final_intensity, 0)  # Use 0 for duration initially

    elif message.type == 'note_off':
        note = message.note
        if note in note_on_times:
            duration = int((time() - note_on_times[note]) * 1000)
            velocity = getattr(message, 'velocity', 0)  # Safely get velocity, default to 0 if not present
            print(f"Note On: {note}, Velocity: {velocity}")
            send_haptic_feedback(note, 0, duration)
            
def get_intensity():
    valid_intensities = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    while True:
        try:
            desired_intensity = int(input("Enter desired vibration intensity (0-100): "))
            if 0 <= desired_intensity <= 100:
                # Find the closest valid intensity
                closest_intensity = min(valid_intensities, key=lambda x: abs(x - desired_intensity))
                return closest_intensity
            else:
                print("Invalid intensity value. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def main():
    midi_port_name = 'LoopBe Internal MIDI 0'
    intensity = get_intensity()  # Get the desired intensity at the start
    with mido.open_input(midi_port_name) as port:
        print(f"Listening on {midi_port_name}...")
        for message in port:
            handle_midi_message(message, intensity)  # Call the handle_midi_message function with the message and intensity


            
             
if __name__ == "__main__":
    main()