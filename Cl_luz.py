import csv
import pandas as pd
import time
import asyncio 
from pywizlight import wizlight, PilotBuilder, discovery

ip_saved=[]
class Bulbs:

    def Save_ip_mac(ip, mac):
        df=pd.read_csv('Dir_ligths.csv', sep=r",", header=0)
        position=0
        while True:
            try:
                if mac==df.loc[position,'MAC']:
                    df.loc[position,'IP']=ip
                    df.to_csv("Dir_ligths.csv", index=False)
                    print("♫♫♫ Guardado Exitoso ♫♫♫")
                    break
                if position==3:
                    with open('Dir_ligths.csv', '+a', newline='') as file:
                        write=csv.writer(file, delimiter=',')
                        write.writerow([ip,mac])
                        print("♫♫♫ Guardado Exitoso ♫♫♫")
                    break
                position+=1
            except:
                with open('Dir_ligths.csv', '+a', newline='') as file:
                    write=csv.writer(file, delimiter=',')
                    write.writerow([ip,mac])
                print("♫♫♫ Guardado Exitoso ♫♫♫")
                break
    
    def set_mac():
        df=pd.read_csv('Dir_ligths.csv', sep=r",", header=0)
        data=[]
        for i in range(6):
            data.append(df.loc[i,'MAC'])
        print(data)
        return data

    def test(mac_test):
        async def main():
            df=pd.read_csv('Dir_ligths.csv', sep=r",", header=0)
            for index in range(0,5):
                if mac_test==df.loc[index,'MAC']:
                    await wizlight(str(df.loc[index,'IP'])).turn_on(PilotBuilder(brightness = 255))
                    time.sleep(1)
                    await wizlight(str(df.loc[index,'IP'])).turn_on(PilotBuilder(brightness = 10))
                    time.sleep(1)
                    await wizlight(str(df.loc[index,'IP'])).turn_on(PilotBuilder(brightness = 255))
                    time.sleep(1)
                    await wizlight(str(df.loc[index,'IP'])).turn_on(PilotBuilder(brightness = 10))
                    time.sleep(1)
                    await wizlight(str(df.loc[index,'IP'])).turn_off()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main()) 

    def save_pos(bulb_pos):
        df=pd.read_csv('Dir_ligths.csv', sep=r",", header=0)
        global ip_saved
        for index in range(0,len(bulb_pos)):
            for i in range(5):
                if bulb_pos[index] == df.loc[i,'MAC']:
                    ip_saved.append(df.loc[i,'IP'])

    def loca():
        print(ip_saved)
    

def catch_trigger(trigger):
    formatted_list=[]
    tgg_r=0
    tgg_g=0
    tgg_b=0
    if trigger =="A1":
        formatted_list =[1,3,5,7,9]
        tgg_r=255
        tgg_g =255
        tgg_b=0
    elif trigger =="A3":
        formatted_list=[3,1,5,9,7]
        tgg_r=0
        tgg_g =255
        tgg_b=0
    elif trigger =="A5":
        formatted_list=[5,1,3,7,9]
        tgg_r=0
        tgg_g =255
        tgg_b=255
    elif trigger =="A7":
        formatted_list=[7,1,5,9,3]
        tgg_r=0
        tgg_g =0
        tgg_b=255
    elif trigger =="A9":
        formatted_list=[9,7,5,3,1]
        tgg_r=255
        tgg_g =0
        tgg_b=127
    print(tgg_r,tgg_g,tgg_b)
    list_manager(formatted_list,tgg_r,tgg_g,tgg_b)


#ADMINISTRA LOS CAMBIOS DE COLOR Y LA FORMA EN QUE SE MANDA A ANCENDER LAS LUCES
def list_manager(trigger_list,r_,g_,b_):
    global count
    proc_list =[]
    degraded = 2
    r= r_
    g= g_
    b= b_
    bright = 255
    count = degraded
    for j in range(0,degraded):
        for i in range(len(trigger_list)):
            proc_list.append(trigger_list[i])
            if (proc_list[i] == trigger_list[0]) or (proc_list[i] == trigger_list[3]):
                turnOn_RGB(proc_list[i],r,g,b,bright)
                #print("-----------delay-----------")
                time.sleep(0.3)
            else:
                turnOn_RGB(proc_list[i],r,g,b,bright)
        bright-=255
        count -= 1
        if count ==0:
            turnOff_RGB()
        

        
#ip_saved = ['192.168.16.202', '192.168.16.59', '192.168.16.1', '192.168.16.168', '192.168.16.14']
#ENCIENDE LAS LUCES EN EL ORDEN QUE RECIBE
def turnOn_RGB(_item, _r,_g,_b,brillo):
    global ip_saved
    async def main():
        item = _item
        if item == 1:
            print(item,_r,_g,_b)
            await wizlight(ip_saved[0]).turn_on(PilotBuilder(rgb= (_r,_g,_b),brightness=brillo))
        elif item == 3:
            print(item,_r,_g,_b)
            await wizlight(ip_saved[1]).turn_on(PilotBuilder(rgb= (_r,_g,_b),brightness=brillo))
        elif item == 5:
            await wizlight(ip_saved[2]).turn_on(PilotBuilder(rgb= (_r,_g,_b),brightness=brillo))
            print(item,_r,_g,_b)
        elif item == 7:
            await wizlight(ip_saved[3]).turn_on(PilotBuilder(rgb= (_r,_g,_b),brightness=brillo))
            print(item,_r,_g,_b)
        elif item == 9:
            await wizlight(ip_saved[4]).turn_on(PilotBuilder(rgb= (_r,_g,_b),brightness=brillo))
            print(item,_r,_g,_b)
    print(str(brillo))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def turnOff_RGB():
    async def GetOff():
        await wizlight(ip_saved[0]).turn_off()
        await wizlight(ip_saved[1]).turn_off()
        await wizlight(ip_saved[2]).turn_off()
        await wizlight(ip_saved[3]).turn_off()
        await wizlight(ip_saved[4]).turn_off()
    looff = asyncio.get_event_loop()
    looff.run_until_complete(GetOff())
        

#input()
# catch_trigger("A1")
# time.sleep(2)
# catch_trigger("A3")
# time.sleep(2)
# catch_trigger("A5")
# time.sleep(2)
# catch_trigger("A7")
# time.sleep(2)
# catch_trigger("A9")

        

        



