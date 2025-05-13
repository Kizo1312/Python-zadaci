from tkinter import *

def spremi():
    title =textBox.get("1.0", "end-1c")
    content= messageBox.get("1.0", "end-1c")
    with open(f"{title}.txt", "w") as f:
        f.write(content)
        spremljene.config(text=f"{title}.txt \n")
        listbox.insert(1, spremljene.cget("text"))
    messageBox.delete("1.0", "end")
    textBox.delete("1.0", "end")
def prikazi_text():
    selected_item = listbox.curselection()
    if selected_item:  
        index = selected_item[0]
        tag_name = listbox.get(index)
    
    messageBox.tag_add(tag_name,"1.0","end")



root=Tk()
root.title ="Osobni dnevnik"

tipka1=Button(root, text="Spremi biljesku", width=5, height=2, command=spremi )
tipka1.grid(row=4, column=1)

biljeske_naslov=Label(root,text="biljeske")
biljeske_naslov.grid(row=5, column=1)

spremljene = Label(root, text = "") 

listbox =Listbox(root,height=10, width=15)
listbox.grid(row=6, column=1)


sadrzaj = Label(root,text="sadrzaj")
sadrzaj.grid(row=2, column=1)

naslov = Label(root, text="Naslov Biljeske")
naslov.grid(row=0,column=1)

textBox=Text(root, height=1, width=10)
textBox.grid(row=1, column=1)

messageBox= Text(root, height=10, width=10)
messageBox.grid(row=3, column=1)

prikazi=Button(root, text="Prikazi biljesku",width=5, height=2, command=prikazi_text)
prikazi.grid(row=7, column=1)



root.mainloop()