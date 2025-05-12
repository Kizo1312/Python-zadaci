from tkinter import *
istina = True
brojevi = []

def funkcija():
    labela.config(text=unos.get())
def zbroji():
    oznaka.config(text=f"{int(broj1.get()) +int(broj2.get())}")
    
def podijeli():
     oznaka.config(text=f"{int(broj1.get()) /int(broj2.get())}")
     






root= Tk()
root.title("demo")



unos = Entry(root, width=30)
unos.grid(row=0, column=0)



broj2= Entry(root, width=50)
broj2.grid(row=1, column=1)

broj1= Entry(root, width=50)
broj1.grid(row=0, column=1)


tipka1 = Button(root, text="zbroji", command=zbroji)
tipka1.grid(row=2, column=1)

oznaka =Label(root, text="zbroj brojeva")
oznaka.grid(row=3, column=1)

podjela = Button(root,text="Podijeli", command=podijeli )
podjela.grid(row=2, column=2)


tipka = Button(root, text="tipka", command=funkcija)
tipka.grid(row=1, column=0)

labela = Label(root, text="prikaz teksta")
labela.grid(row=2,column=0)

Button(root, text="quir", command=root.destroy).grid(column=3, row=5)




root.mainloop()
