import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, 50)
pwm.start(0)

GPIO.setup(7, GPIO.OUT)
pwma = GPIO.PWM(7, 50)
pwma.start(0)

def SetAngleBase(angle):
    duty = (angle/18)+2
    GPIO.output(3 , True)
    pwm.ChangeDutyCycle(duty)
    sleep(3)

    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)
    
def SetAngleAim(angle):
    duty = (angle/18)+2
    GPIO.output(7 , True)
    pwma.ChangeDutyCycle(duty)
    sleep(3)

    GPIO.output(7, False)
    pwma.ChangeDutyCycle(0)
    
SetAngleBase(0)
SetAngleAim(180)

pwm.stop()
pwma.stop()
GPIO.cleanup()
    