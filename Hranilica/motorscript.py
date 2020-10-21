import RPi.GPIO as GPIO
import time

portionDistance = 10


#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
def distance(GPIO_TRIGGER,GPIO_ECHO):
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance

def sipaj():
    GPIO.setmode(GPIO.BCM)

    servoPIN = 17
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    GPIO.output(servoPIN, 1)
    p.start(7.5) # Initialization
    time.sleep(1)
    GPIO.output(servoPIN, 0)
    p.start(2.5)

    f = True
    try:
        GPIO.output(servoPIN, 1)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        GPIO.output(servoPIN, 0)
        print("radi try")
        while f:
            print("asga")

            if distance(GPIO_TRIGGER,GPIO_ECHO) < portionDistance:
                
                GPIO.output(servoPIN, 1)
                p.ChangeDutyCycle(2.5)
                time.sleep(1)
                GPIO.output(servoPIN, 0)
                
                
                f = False
        print(f)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()