import paho.mqtt.publish as publish

msgs = [{'topic': "ifn649", 'payload': "sth here 1!"}, ("ifn649", "sth here 2?", 0, False), ("ifn649", "sth here 10@", 0, False)]

publish.multiple(msgs, hostname="3.26.215.204")

print("Done")