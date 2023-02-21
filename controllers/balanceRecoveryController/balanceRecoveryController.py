from controller import Robot, Motor, Node
from math import pi, sin

TIME_STEP = 32

robot = Robot()

nDevices = robot.getNumberOfDevices()
for i in range(nDevices):
    device = robot.getDeviceByIndex(i)
    name = device.getName()
    type = device.getNodeType()
    # do something with the device
    print("Device #{} name = {}\n".format(i, name))
    if (type == Node.CAMERA):
        # do something with the camera
        print("Device #{} is a camera\n".format(i))

motor = robot.getDevice("Neck")
F = 2.0   # frequency 2 Hz
t = 0.0   # elapsed simulation time

while robot.step(TIME_STEP) != -1:
    # print("Simulation time is: {}".format(t))
    position = sin(t * 2.0 * pi * F)
    motor.setPosition(position)
    t += TIME_STEP / 1000.0
