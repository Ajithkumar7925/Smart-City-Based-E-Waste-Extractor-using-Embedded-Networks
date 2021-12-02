import sys
import os
import time
from time import sleep
from urllib.request import urlopen
#import urllib2
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
#Setup our API and delay
myAPI = "3CUMOGTM5V2JA2CL" # API Key from thingSpeak.com channel
myDelay = 15 #how many seconds between posting data
def getSensorData():
    MQ2 = 0
    print('Reading ADS1x15 values, press Ctrl-C to quit...')
    # Print nice channel column headers.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
    print('-' * 37)
    try:

        while True:

            values = [0] * 4
            for i in range(4):
                    values[i] = adc.read_adc(i, gain=GAIN)
                    MQ2 = values[0]

            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | '.format(*values))
            return (str(MQ2))
    except KeyboardInterrupt:
         print(" Quit")


def main():
    print('starting...')
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print(baseURL)
    while True:
        try:
            print("Reading Sensor Data now")
            MQ2 = getSensorData()
            print(MQ2 + " ")
            f = urlopen(baseURL + "&field1=%s" % (MQ2))
            print(f.read())
            f.close()
            sleep(int(myDelay))
        except Exception as e:
            print(e)
            print('exiting.')
            break


if __name__ == '__main__':
    main()