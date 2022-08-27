import serial
import time
import string
import paho.mqtt.publish as publish

ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        publish.single("ifn649", cookedserial, hostname="3.26.215.204")

print("Done")