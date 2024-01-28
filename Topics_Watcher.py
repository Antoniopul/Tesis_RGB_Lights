import paho.mqtt.client as mqtt

def fxOn_connect(client, userdata, flagas, rc):
    print("Se conectó con mqtt "+ str(rc))
    #client.subscribe("Tesis_ESP/#")
    client.subscribe("WatchData/#")

def fxOn_message(client, userdata, msg):
    raw_area =msg.payload.decode()
    #msg.topic == "Tesis_ESP/Node1" and 
    # if (raw_area != "---"):
    print("Mensaje recibido de " + str(msg.topic)+ ": " + str(raw_area))

client = mqtt.Client()
client.on_connect = fxOn_connect
client.on_message=fxOn_message

client.connect("servermqtt.local")
client.loop_forever()