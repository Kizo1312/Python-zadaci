import random
import string
def id_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
popis1 = []
popis2 = []

with open("ucenici.txt", "w") as f:
    for i in range (4):
        
        f.write(f"{id_generator()} \n")

with open("za_pretragu.txt", "w") as g:
    for i in range (4):
        
        
        g.write(f"{id_generator()} \n")

with open("ucenici.txt", "r") as h:
    for i in range(4):
        popis1.append(h.readline())

   
with open("za_pretragu.txt", "r") as h:
    for i in range(4):
        popis2.append(h.readline())
for i in range(len(popis1)):
    if popis2[i] in popis1:
        print(popis2[i].strip(), "DA")
    else:
        print(popis2[i].strip(), "NE")

