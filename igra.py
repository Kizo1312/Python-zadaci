from tkinter import *
istina = True



def dodaj_jednako():
    labela.config(text=eval(labela.cget('text')))

def dodaj_znak(znak):
    labela.config(text=f"{labela.cget('text')}{znak}")



root= Tk()
root.title("demo")




plus = Button(root,text="+", command= lambda:dodaj_znak("+") )
plus.grid(row=5, column=0)

jedinica = Button(root, text="1", command=lambda:dodaj_znak("1"))
jedinica.grid(row=3, column=0)


dvojka = Button(root, text="2", command=lambda:dodaj_znak("2"))
dvojka.grid(row=3, column=1)

trojka = Button(root, text="3", command=lambda:dodaj_znak("3"))
trojka.grid(row=3, column=2)

cetvorka = Button(root, text="4", command=lambda:dodaj_znak("4"))
cetvorka.grid(row=2, column=0)

petica = Button(root, text="5", command=lambda:dodaj_znak("5"))
petica.grid(row=2, column=1)

sestica = Button(root, text="6", command=lambda:dodaj_znak("6"))
sestica.grid(row=2, column=2)

sedmica = Button(root, text="7", command=lambda:dodaj_znak("7"))
sedmica.grid(row=1, column=0)

osmica = Button(root, text="8", command=lambda:dodaj_znak("8"))
osmica.grid(row=1, column=1)

devetka = Button(root, text="9", command=lambda:dodaj_znak("9"))
devetka.grid(row=1, column=2)

jednako = Button(root, text="=", command=dodaj_jednako)
jednako.grid(row=4, column=1)

minus = Button(root, text="-", command=lambda:dodaj_znak("-"))
minus.grid(row=3, column=3)

puta = Button(root, text="*", command=lambda:dodaj_znak("*"))
puta.grid(row=2, column=3)

podijeljeno = Button(root, text="/", command=lambda:dodaj_znak("/"))
podijeljeno.grid(row=1, column=3)








labela = Label(root, text="")
labela.grid(row=0, column=0, columnspan=4)

nula = Button(root, text="0", command=lambda:dodaj_znak("0"))
nula.grid(row=4, column=0)


clear = Button(root, text="C", command=lambda: labela.config(text=""))
clear.grid(row=4, column=2)

root.mainloop()
