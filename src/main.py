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

bp = Bumper(Ports.PORT12)

# def moveShape(userInput, Size, Direction,CrankShaft):
#     if userInput == "Square":
#         for i in range(4):
#             dt.drive_for(CrankShaft,Size, MM)
#             dt.turn_for(Direction,90, DEGREES)
#     elif userInput == "Triangle":
#         for i in range(3):
#             dt.drive_for(CrankShaft,Size, MM)
#             dt.turn_for(Direction,120, DEGREES)
#     elif userInput == "Circle":
#         lm.spin_for(CrankShaft, 3, RotationUnits) and rm.spin_for(CrankShaft, 180, DEGREES) # pyright: ignore[reportUnusedExpression]
#     elif userInput == "Rectangle":
#         for i in range(2):
#             dt.drive_for(CrankShaft,Size, MM)
#             dt.turn_for(Direction,90, DEGREES)
#             dt.drive_for(CrankShaft,Size, MM)
#             dt.turn_for(Direction,90, DEGREES)
#     else:
#         dt.stop()


# moveShape("Circle",20,RIGHT,FORWARD)

# def pushBumper(movingDistance):

#     loopCounter = 0
#     while bp.pressing() == False:
#         loopCounter += 1
#         dt.drive_for(FORWARD, movingDistance, MM)
#         if bp.pressing() == True:
#             dt.drive_for(REVERSE, movingDistance, MM)
#             loopCounter = 0 
            

#     pushBumper(10)


def buttonEvent():
    while True:
        if bp.pressing():
            brain.screen.clear_screen(Color.WHITE)
            wait(1, SECONDS)
            brain.screen.clear_screen(Color.RED)
            wait(1, SECONDS)
            brain.screen.clear_screen(Color.ORANGE)
            wait(1, SECONDS)
            brain.screen.clear_screen(Color.YELLOW)
            wait(1, SECONDS)
            brain.screen.clear_screen(Color.GREEN)
            wait(1, SECONDS)
            brain.screen.clear_screen(Color.PURPLE)


# Blink the screen while turning
move_event = Event()

def blink_screen():
    while True:
        brain.screen.clear_screen(Color.RED)
        wait(0.5, SECONDS)
        brain.screen.clear_screen()
        wait(0.5, SECONDS)

def turning():
    dt.turn(RIGHT)

# Register multiple functions to the Event object
move_event(buttonEvent)
move_event(turning)

move_event.broadcast()
