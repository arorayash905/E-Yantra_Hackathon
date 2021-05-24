import time
import RPi.GPIO as GPIO
trig = 7
echo = 12

time.sleep(0.5)

# Sensor Pin Setup
GPIO.setup(trig, GPIO.OUT)
time.sleep(0.1)
GPIO.setup(echo, GPIO.IN)

# Servo Pin Setup
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

while True:
    while GPIO.input(echo) == 0:
            pass
    start = time.time()
    
    while GPIO.input(echo) == 1:
            pass
    stop = time.time()
    
    # Calculating Distance
    distance_in_cm = (stop-start) * 17000
    
    GPIO.cleanup()
    
    if distance_in_cm <= 4:
        return
    else:
        pass










