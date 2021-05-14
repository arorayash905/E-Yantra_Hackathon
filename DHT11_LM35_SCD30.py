import Adafruit_DHT
import RPi.GPIO as GPIO
from upm import pyupm_lm35
import board
import adafruit_scd30
import time

GPIO.setmode(GPIO.BCM)

DHT11_pin = 17 # DHT11 sensor connected to GPIO pin 17
LM35_pin = 27 # DHT11 sensor connected to GPIO pin 27

GPIO.setup(DHT11_pin, GPIO.IN)
GPIO.setup(LM35_pin, GPIO.IN)

i2c = board.I2C() # uses board.SCL and board.SDA ---> GPIO 2 and GPIO 3
scd30 = adafruit_scd30.SCD30(i2c)

def DHT11():
    while True:
        humidity, room_temprature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT11_pin)
        return room_temprature

def LM35():
    sensorLM35 = pyupm_lm35.LM35(LM35_pin)
    body_temprature = sensorLM35.getTemprature()
    return body_temprature
    
def SCD30():
    co2, temprature, humidity = scd30.CO2, scd30.temperature, scd30.relative_humidity
    return co2, temprature, humidity


while True:
    def main():
        room_temprature_DHT11 = DHT11()
        body_temprature = LM35()
        co2, temprature_SCD30, humidity_SCD30 = SCD30()
