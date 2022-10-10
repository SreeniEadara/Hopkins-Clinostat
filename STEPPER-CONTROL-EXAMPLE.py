############
# IMPORTS
############
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

############
# Motor Setup
############
dir_pin = 13
step_pin = 19
Enable_pin = 26

stepMotor = RpiMotorLib.A4988Nema(dir_pin, step_pin, (21,21,21), "DRV8825") ####################################################################################
GPIO.setup(Enable_pin,GPIO.OUT) # set enable pin as output ####################################################################################

#dir_Bools = [False,True]
#dir_Bools[ii%2] #Can do 2 cup dispensing

GPIO.output(Enable_pin,GPIO.LOW) # pull enable to low to enable motor

############
# Server Motor Control
############

for i in range(10):
  stepMotor.motor_go(False,"Full",200, .0005, False,.05)