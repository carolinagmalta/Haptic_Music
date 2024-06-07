import argparse
from http import client
import math
from time import sleep

from bhaptics import haptic_player
from pythonosc import dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer


player = haptic_player.HapticPlayer()

def handle_front(unused_addr, args, volume):
    print(f"Front: {volume}")

def handle_back(unused_addr, args, volume):
    print(f"Back: {volume}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/vest_front", handle_front)
    dispatcher.map("/vest_back", handle_back)

    server = ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print(f"Serving on {server.server_address}")
    server.serve_forever()

    def handle_new_command(unused_addr, args, value):
        print(f"New command received: {value}")

for x in range(10):
    print('send front {0}'.format(x))
    client.send_message("/vest_front", '{0},{1}'.format(x, 100))
    sleep(1)
    print('Send back {0}'.format(x))
    client.send_message("/vest_back", '{0},{1}'.format(x, 100))
    sleep(1)
    

# In your main function:
dispatcher.map("/new_command", handle_new_command)