# requires sshkeyboard
from sshkeyboard import listen_keyboard, stop_listening
import time
import irobot_create

# Connect to roomba
roomba = irobot_create.Roomba('/dev/ttyUSB0')
# driving speed in mm/s
speed = 150
brush_status = False

# Instructions
print("Use Arrow keys (<, ^, v, >) to drive")
print("c to toggle brushes")
print("s to set speed")
print("q to quit")

def press(key):
    global speed
    global brush_status

    if key == "left":
        roomba.set_drive_spin_ccw(speed)
        print('<')
    elif key == "right":
        roomba.set_drive_spin_cw(speed)
        print('>')
    elif key == "up":
        roomba.set_drive_straight(speed)
        print('^')
    elif key == "down":
        roomba.set_drive_backwards(speed)
        print('v')
    elif key == "s":
        speed = int(input("enter speed in mm/s (number only): "))
        # keep speed in range
        # 20mm/s is the minimum at wich the roomba still drives
        # 500mm/s is the maximum speed defined by the specs 
        speed = min(speed, 500)
        speed = max(speed, 20)
        print('speed set to: ' + str(speed) + 'mm/s')
    elif key == 'c':
        if brush_status:
            roomba.set_cleaning_off()
        else:
            roomba.set_cleaning_all()
        brush_status = not brush_status
        print("Brushes on") if brush_status else print("Brushes off")
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
    sequential=True,
)
