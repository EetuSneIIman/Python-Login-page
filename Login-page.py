import os
os.system("cls")

from tkinter import *
from tkinter import ttk


#Teksti kun kirjaudut sisään

def painallus():
    kirjautuminen = Label(text = "Kirjauduit sisään!", fg="white", bg="black", heigh=1, width=20)
    kirjautuminen.place(x=175, y=340)
    print("Kirjauduit sisään!")
    
    syoteik = syote_temp.get()


    syote2.delete(0, END)
    syote.delete(0, END)

def show_hide_psd():
    if(check_var.get()):
        syote.config(show="")
    else:
        syote.config(show="*") 






#Määritetään sovelluksen nimi
ikkuna = Tk()


ikkuna.title("Sisäänkirjautuminen")

ikkuna.geometry("500x1000")

#Otsikko
otsikko = Label(text="Tervetuloa!", fg="white", bg="black")


otsikko.pack(fill= X)


#Käyttäjänimen laatikko
kayttajanimi = Label(text="Käyttäjänimi", fg="white", bg="black", heigh=2, width=20)


kayttajanimi.place(x=100, y=150)

#Käyttäjänimen syöte
syote_temp = StringVar()
syote2 = Entry(textvariable=syote_temp)
syote2.place(x=270, y=160)

#Salasanan laatikko
salasana = Label(text="Salasana", fg="white", bg="black", heigh=2, width=20)


salasana.place(x=100, y=195)
#Salasanan syöte

syote = Entry(ikkuna, show="*")
syote.place(x = 270, y = 205)

#Kirjaudu sisään painike

painikeNimi = Button(ikkuna, text="Kirjaudu sisään", heigh=0, width=15, command=painallus)
painikeNimi.place(x=190, y=300)


#Checkbutton
check_var = IntVar()
nappi = Checkbutton(ikkuna, text = "Näytä salasana", variable = check_var, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 15, command = show_hide_psd)
nappi.place(x = 105, y = 235)


#Suoritus
ikkuna.mainloop()

#EOF