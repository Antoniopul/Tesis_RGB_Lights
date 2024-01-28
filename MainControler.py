from time import sleep
import paho.mqtt.client as mqtt
import Cl_luz as clluz
import interfaz as iz

#-------------------[__VARIABLES__]---------------------#
comparation_list =[]
#-------------------[__FUNCIONES__]---------------------#
def function_compare(tocompare):
    global comparation_list
    comparation_list.append(tocompare)
    leds_area = set(comparation_list)
    if len(comparation_list) ==1 and len(leds_area)==1:
        are_name = str((list(leds_area)[0]))
        print("------------Lampara encendida en " + are_name)
        clluz.catch_trigger(are_name)
        comparation_list.clear()
    elif len(comparation_list) >=3 and len(leds_area)>=2:
        comparation_list.clear()
    else:
        print("NO hay area coincidente")
        print(str(comparation_list))
       

#-------------------[__CALLBACKS__]---------------------#
def On_connect(client, userdata, flagas, rc):
    print("Se conectó con mqtt "+ str(rc))
    client.subscribe("Tesis_ESP/#")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def On_message(client, userdata, msg):
    raw_area =msg.payload.decode()
    print("Mensaje recibido de " + str(msg.topic)+ ": " + str(raw_area))
    function_compare(raw_area)

#-------------------[__ASIGNACIÓN AL OBJETO CLIENTE__]---------------------#

client = mqtt.Client()
client.on_connect = On_connect
client.on_message=On_message
client.connect("192.168.16.230")
#-----------------------[__LOOP__]---------------------#
client.loop_forever()
#client.loop_start()
#client.loop_forever()
#client.loop_stop()

