import paho.mqtt.publish as publish

publish.single("ifn649", "LED_ON", hostname="3.26.215.204")

print("Cmds sent!")