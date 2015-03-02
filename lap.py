import wiringpi
from time import sleep

shuterpin = 17
motorpin = 23

framecount=50 #Numero total de fotografias
pulse_length=0.1 #Tiempo de movimiento del motor
settling_time=0.5 #Tiempo desde que termina de moverse el motor hasta que vuelve a iniciar (tiene que ser mayor tiempo que interval_delay)
shutter_length=2 #Tiempo que esta abierto el obturador (Tiempo por fotografia)
interval_delay=0.5 #Tiempo desde que termina la foto hasta que empieza la siguiente

gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
gpio.pinMode(shutterpin,gpio.OUTPUT)
gpio.pinMode(motorpin,gpio.OUTPUT)
wiringpi.pinMode(shutterpin,1)
wiringpi.piMode(motorpin,1)

for i in range(0,framecount)
    gpio.digitalWrite(motorpin,gpio.HIGH)
    sleep(pulse_length)
    gpio.digitalWrite(motorpin,gpio.LOW)
    sleep(settling_time)
    
    print "Fotografia" , str (i+1) + " de " + str (framecount)

    gpio.digital(shutterpin,gpio.HIGH)
    sleep(shutter_length)
    gpio.digitalWriter(shutterpin,gpio.LOW)
    sleep(interval_delay)
