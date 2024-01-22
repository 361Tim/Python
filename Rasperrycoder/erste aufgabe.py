import RPi.GPIO as GPIO
import time
input = input()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


while True:
        GPIO.output(18,True)
        time.sleep(5)
        GPIO.output(18, True)
        time.sleep(1)


