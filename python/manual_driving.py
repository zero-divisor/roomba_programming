# requires sshkeyboard
from sshkeyboard import listen_keyboard, stop_listening
import time
import irobot_create

# Connect to roomba
roomba = irobot_create.Roomba('/dev/ttyUSB0')
# Instructions
print("Benutze Pfeiltasten (<, ^, v, >) um den roomba zu steuern")
print("c um Bürsten zu Starten")
print("o um Bürsten zu Stoppen")
print("q zum Beenden")

def press(key):
    if key == "left":
        roomba.set_drive_spin_ccw(200)
        print('<')
    elif key == "right":
        roomba.set_drive_spin_cw(200)
        print('>')
    elif key == "up":
        roomba.set_drive_straight(200)
        print('^')
    elif key == "down":
        roomba.set_drive_backwards(200)
        print('v')
    elif key == 'c':
        roomba.set_cleaning_all()
        print("Starting Brushes")
    elif key == 'o':
        roomba.set_cleaning_off()
        print("Stoping Brushes")
    elif key == "q":
        print("exiting")
        roomba.set_cleaning_off()
        roomba.close()
        stop_listening()

def release(key):
    roomba.set_drive_stop()
    print('stop')

listen_keyboard(
    on_press=press,
    on_release=release,
)
