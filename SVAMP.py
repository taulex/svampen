import time
import board
import adafruit_dht
import psutil
import RPi.GPIO as GPIO
import datetime

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
# GPIO.cleanup()
time.sleep(1.0)

tid1 = "09:37"
tid2 = "09:39"
tid3 = "09:41"
hum1 = 80
hum2 = 85

sdfgfdghokfghkjfgoihjfogijh


tider = [tid1, tid2, tid3]


def loggValues():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    logfile_name = "svamplogg.csv"
    with open(logfile_name, "a") as logfile:
        logfile.write(date + ";" + "Humidity;" + str(humidity) + ";" + "Temperature;" + str(temp) + "\n")


def fanklocka():
    now = datetime.datetime.now()
    date = now.strftime("%H:%M")
    if date in tider:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)


def humiditysens():
    if humidity < hum1:
        GPIO.output(6, 1)
    elif humidity > hum2:
        GPIO.output(6, 0)


while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    humiditysens()
    fanklocka()
    loggValues()

    time.sleep(3.0)
