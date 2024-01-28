import asyncio
from Cl_luz import Bulbs
from pywizlight import discovery


def initSearch():
    async def busqueda():
        print("aqui")
        ligths = await discovery.discover_lights(broadcast_space="192.168.16.255")
        print("lel")
        try:
            print("here again")
            for index in range(6): 
                print (ligths[index].ip)     
                Bulbs.Save_ip_mac(ligths[index].ip, ligths[index].mac)
        except:
            print("No se detectan mas focos")
        return ligths
    loop1 = asyncio.new_event_loop()
    loop1.run_until_complete(busqueda())
    loop1.close()
    