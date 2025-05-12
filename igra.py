from tkinter import *
istina = True


def dodaj1():
    
    labela.config(text=f"{labela.cget("text")} 1")
def dodaj2():
    labela.config(text=f"{labela.cget("text")} 2")
def dodaj3():
    labela.config(text=f"{labela.cget("text")} 3")
def dodaj4():
    labela.config(text=f"{labela.cget("text")} 4")
def dodaj5():
    labela.config(text=f"{labela.cget("text")} 5")
def dodaj6():
    labela.config(text=f"{labela.cget("text")} 6")
def dodaj7():
    labela.config(text=f"{labela.cget("text")} 7")
def dodaj8():
    labela.config(text=f"{labela.cget("text")} 8")
def dodaj9():
    labela.config(text=f"{labela.cget("text")} 9")
def dodaj_plus():
    labela.config(text =f"{labela.cget("text")} +")
def dodaj_jednako():
    labela.config(text=eval(labela.cget("text")))

def dodaj_minus():
    labela.config(text =f"{labela.cget("text")} -")

def dodaj_puta():
    labela.config(text =f"{labela.cget("text")} *")

def dodaj_divide():
    labela.config(text =f"{labela.cget("text")} /")




root= Tk()
root.title("demo")



unos = Entry(root, width=30)
unos.grid(row=0, column=0)
plus = Button(root,text="+", command=dodaj_plus )
plus.grid(row=5, column=0)

jedinica = Button(root, text="1", command=dodaj1)
jedinica.grid(row=0, column=3)

dvojka = Button(root, text="2", command=dodaj2)
dvojka.grid(row=1, column=3)

trojka = Button(root, text="3", command=dodaj3)
trojka.grid(row=2, column=3)

cetvorka = Button(root, text="4", command=dodaj4)
cetvorka.grid(row=3, column=3)

petica = Button(root, text="5", command=dodaj5)
petica.grid(row=4, column=3)

sestica = Button(root, text="6", command=dodaj6)
sestica.grid(row=5, column=3)

sedmica = Button(root, text="7", command=dodaj7)
sedmica.grid(row=6, column=3)

osmica = Button(root, text="8", command=dodaj8)
osmica.grid(row=7, column=3)

devetka = Button(root, text="9", command=dodaj9)
devetka.grid(row=8, column=3)

jednako = Button(root, text="=", command=dodaj_jednako)
jednako.grid(row=9, column=3)

minus = Button(root, text="-", command=dodaj_minus)
minus.grid(row=6, column=0)

puta = Button(root, text="*", command=dodaj_puta)
puta.grid(row=7, column=0)

podijeljeno = Button(root, text="/", command=dodaj_divide)
podijeljeno.grid(row=8, column=0)






labela = Label(root, text="")
labela.grid(row=2,column=0)

Button(root, text="quit", command=root.destroy).grid(column=3, row=5)




root.mainloop()
