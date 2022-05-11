import irobot_create

# Connect to roomba
roomba = irobot_create.Roomba('/dev/ttyUSB0')
# Instructions
roomba.set_seek_dock()
