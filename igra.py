from tkinter import *
istina = True



def dodaj_jednako():
    labela.config(text=eval(labela.cget('text')))

def dodaj_znak(znak):
    labela.config(text=f"{labela.cget('text')}{znak}")
def obrisi():
    labela.config(text="")



root= Tk()
root.title("kalkulator")




buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('=', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = Button(root, text=text, width=5, height=2, command=dodaj_jednako)
    elif text == 'C':
        btn = Button(root, text=text, width=5, height=2, command=obrisi)
    else:
        btn = Button(root, text=text, width=5, height=2, command=lambda t=text: dodaj_znak(t))
    btn.grid(row=row, column=col)







labela = Label(root, text="")
labela.grid(row=0, column=0, columnspan=4)



root.mainloop()
