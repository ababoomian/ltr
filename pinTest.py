import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
for i in range(2, 6):
    for j in range(2, 6):
        if i == j:
            continue
        GPIO.setup([2, 3, 4, 5], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(i, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(j, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        sleep(0.1)
        if GPIO.input(j):
            l.add(tuple(sorted((i, j))))
print(l)