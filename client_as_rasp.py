import serial 
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc): # func for making connection
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )

    client.subscribe("ifn649")

def on_message(client, userdata, msg): # Func for Sending msg
    ser = serial.Serial("/dev/rfcomm0", 9600)
    cmd = str(msg.payload.decode("utf-8"))
    ser.write(bytes(" " + cmd, 'utf-8'))
    print(cmd)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("3.26.215.204", 1883, 60)

client.loop_forever()