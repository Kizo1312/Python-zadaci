from tkinter import *
from datetime import datetime
import time
root = Tk()
labela = Label(root )
labela.grid(row=0, column=0, columnspan=4)
labela.pack()


def azuriraj():
    now = time.strftime("%H:%M:%S")
    
    labela.config(text=now)
    labela.after(1000,azuriraj)
    return now

    
azuriraj()

root.mainloop()



