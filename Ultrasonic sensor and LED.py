import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
 
TRIG = 20
ECHO = 21

print("Distance Measurement In Progress")

GPIO.setwarnings(False) 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
 
def measure():
        GPIO.output(TRIG, False)
        time.sleep(.5)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
 
        while GPIO.input(ECHO)==0:
                pulse_start = time.time()
 
        while GPIO.input(ECHO)==1:
                pulse_end = time.time()
 
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
 
        print ("Measured Distance = %.1f cm" % distance)
        
        if distance > 9.5:
                print("LED on")
                GPIO.output(12,GPIO.HIGH)
                time.sleep(1)               
                print("LED off")
                GPIO.output(12,GPIO.LOW)
                
                r = requests.post('https://maker.ifttt.com/trigger/Water_Level29/with/key/brLTFT8o6pmB2h-yMaSeyH')
 
while True:
        measure()