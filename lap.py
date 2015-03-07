import wiringpi
from time import sleep

shutterpin = 17
motorpin = 23

framecount=5
pulse_length=0.1
settling_time=0.5
shutter_length=2
interval_delay=0.2

gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
gpio.pinMode(shutterpin,gpio.OUTPUT)
gpio.pinMode(motorpin,gpio.OUTPUT)
wiringpi.pinMode(shutterpin,1)
wiringpi.pinMode(motorpin,1)

for i in range(0,framecount):
    gpio.digitalWrite(motorpin,gpio.HIGH)
    sleep(pulse_length)
    gpio.digitalWrite(motorpin,gpio.LOW)
    sleep(settling_time)
    
    print "Fotografia" , str (i+1) + " de " + str (framecount)
    
    gpio.digitalWrite(shutterpin,gpio.HIGH)
    sleep(shutter_length)
    gpio.digitalWrite(shutterpin,gpio.LOW)
    sleep(interval_delay)
