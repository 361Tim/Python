import RPi.GPIO as GPIO
input = input()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


while True:

    if input == 'e':
        GPIO.output(18,True)
    if input == 'a':
        GPIO.output(18,False)
