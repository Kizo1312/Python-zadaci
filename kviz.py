from tkinter import *
import random
pitanja = ["prvo","drugo","trece","cetvrto","peto","šesto"]
odgovori =[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)]
tocni_odgovori =[1,2,3,4,5,6]
root=Tk()
root.title ="Kviz"
root.geometry("500x300")

def konacan_odgovor():
    print(tocni_odgovori[2])
    print(btn.cget("value") )
    if btn.cget("value") == tocni_odgovori[2]:
        oznaka_za_odgovor.configure(text="Odgovor je: Tocan!!")
    else:
        oznaka_za_odgovor.configure(text="Odgovor je: Netocan :(")


pitanje_label = Label(root, text=f"{pitanja[0]}")
pitanje_label.grid(row=1,column=1)

btn1 = Radiobutton(root,text=f"{odgovori[0][1]}", value=odgovori[0][1], width=5, height=2)

btn2 = Radiobutton(root,text=f"{odgovori[0][2]}", value=odgovori[0][2], width=5, height=2)

btn3 = Radiobutton(root,text=f"{odgovori[0][3]}", value=odgovori[0][3], width=5, height=2)

submit = Button(root,text="odgovori",width=5, height=2, command=konacan_odgovor )
submit.grid(row=5, column=2)

oznaka_za_odgovor= Label(root, text="Odgovor je: " )
oznaka_za_odgovor.grid(row=6, column=2)



root.mainloop()