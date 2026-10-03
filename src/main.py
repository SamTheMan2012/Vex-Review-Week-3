# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Genio2                                                       #
# 	Created:      10/3/2026, 12:14:14 PM                                       #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello IQ2")

rm = Motor(Ports.PORT6,True)
lm = Motor(Ports.PORT1)

dt = DriveTrain(lm, rm)

def moveShape(userInput, Size, Direction,CrankShaft):
    if userInput == "Square":
        for i in range(4):
            dt.drive_for(CrankShaft,Size, MM)
            dt.turn_for(Direction,90, DEGREES)
    elif userInput == "Triangle":
        for i in range(3):
            dt.drive_for(CrankShaft,Size, MM)
            dt.turn_for(Direction,120, DEGREES)
    elif userInput == "Circle":
        dt.drive_for(CrankShaft,Size, MM)
        dt.turn_for(Direction,360, DEGREES)
    elif userInput == "Rectangle":
        for i in range(2):
            dt.drive_for(CrankShaft,Size, MM)
            dt.turn_for(Direction,90, DEGREES)
            dt.drive_for(CrankShaft,Size, MM)
            dt.turn_for(Direction,90, DEGREES)
    else:
        dt.stop()


moveShape("Circle",20,RIGHT,FORWARD)