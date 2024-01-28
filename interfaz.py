from tkinter import * 
from tkinter.ttk import Combobox
from Cl_luz import Bulbs
from Searching import initSearch

interface=Tk()
interface.title("Iot Tesis")
interface.geometry("710x375")
interface.resizable(False,False)
txt_box=Entry(interface, font = ("Arial 18"),width=32)
initSearch()
########################################################################################
#                                      Metods
########################################################################################
def test():
    Bulbs.test(mac_test=cbx1.get())

def config():
    Bulbs.save_pos(bulb_pos=[bul1.get(),bul3.get(), bul5.get(),bul7.get(),bul9.get()])
    Bulbs.loca()

def starp():
    print("Cerrar")
   

########################################################################################
#                                     Objects 
########################################################################################
my_mac=Bulbs.set_mac()

#Extra Buttons
cbx1 = Combobox(state="readonly",values=my_mac)
cbx1.grid(row = 2, column= 1, padx=10)

btn_searchingBulbs = Button(interface,text="📡Test Bulb📡",command=test, font=("Arial 14"), width= 18, height=2)
btn_searchingBulbs.grid(row = 4, column= 1, padx=10)

btn_saveUbication = Button(interface, text="💽Save Ubication💽",command=config,font=("Arial 14"), width= 18, height=2)
btn_saveUbication.grid(row = 6, column= 1, padx=10)

btn_Start = Button(interface, text="💻💻Start💻💻",font=("Arial 14"),command=starp, width= 18, height=2)
btn_Start.grid(row = 7, column= 1, padx=10)

#Order of Bulbs
lb_1 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
lb_1.grid(row = 2, column= 3)
bul1 = Combobox(state="readonly",values=my_mac)
bul1.grid(row = 3, column= 3)

lb_2 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
#lb_2.grid(row = 2, column= 4)
bul2 = Combobox(state="readonly",values=my_mac)
#bul2.grid(row = 3, column= 4)

lb_3 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
lb_3.grid(row = 2, column= 5)
bul3 = Combobox(state="readonly",values=my_mac)
bul3.grid(row = 3, column= 5)


lb_4 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
#lb_4.grid(row = 4, column= 3)
bul4 = Combobox(state="readonly",values=my_mac)
#bul4.grid(row = 5, column= 3)

lb_5 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
lb_5.grid(row = 4, column= 4)
bul5 = Combobox(state="readonly",values=my_mac)
bul5.grid(row = 5, column= 4)

lb_6 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
#lb_6.grid(row = 4, column= 5)
bul6 = Combobox(state="readonly",values=my_mac)
#bul6.grid(row = 5, column= 5)


lb_7 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
lb_7.grid(row = 6, column= 3)
bul7 = Combobox(state="readonly",values=my_mac)
bul7.grid(row = 7, column= 3)

lb_8 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
#lb_8.grid(row = 6, column= 4)
bul8 = Combobox(state="readonly",values=my_mac)
#bul8.grid(row = 7, column= 4)

lb_9 = Label(interface, text="💡",font=("Arial 25"),width= 8, height=2)
lb_9.grid(row = 6, column= 5)
bul9 = Combobox(state="readonly",values=my_mac)
bul9.grid(row = 7, column= 5)

interface.mainloop()