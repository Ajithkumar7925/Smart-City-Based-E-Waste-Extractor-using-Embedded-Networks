import RPi.GPIO as GPIO
from urllib.request import urlopen
import time

# Enter Your API key here
myAPI = 'R5W9NKRFEMU0UALO'
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 16

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    while True:
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        time.sleep(2)

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0: pass
        pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1: pass
        pulse_end_time = time.time()

        pulse_duration = (pulse_end_time - pulse_start_time) * 0.5
        distance = round(pulse_duration * 17150, 2)
        # distance = distance/2.54 (for inches)
        conn = urlopen(baseURL + '&field1=%f' % (distance))
        conn.close()

except KeyboardInterrupt:
    print("\nThank you, visit again")

finally:
    GPIO.cleanup()
