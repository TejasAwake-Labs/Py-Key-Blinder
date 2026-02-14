import RPi.GPIO as GPIO
from time import sleep
from multiprocessing.connection import Listener

R = Listener(('localhost',5000)).accept()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, 50)
pwm.start(0)

GPIO.setup(5, GPIO.OUT)
pwma = GPIO.PWM(5, 50)
pwma.start(0)

base = None
aim = None

def SetAngleBase(angle):
    duty = (angle/18)+2
    GPIO.output(3 , True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    pwm.ChangeDutyCycle(0)

def SetAngleAim(angle):
    duty = 2.5 + (angle / 18)
    GPIO.output(5 , True)
    pwma.ChangeDutyCycle(duty)
    sleep(0.5)
    pwma.ChangeDutyCycle(0)
 
try:
    while True:
        x , y = R.recv()
        base = x
        aim = y
        print(x,y)
        if x > 180:
            print("this is the reason your servo burnt")
        
        else:
            SetAngleBase(base)
            SetAngleAim(aim)
except KeyboardInterrupt:
    print("Stopping...")
    SetAngleBase(97)
    SetAngleAim(99)
finally:
    pwm.stop()
    pwma.stop()
    GPIO.cleanup()
    
    


    