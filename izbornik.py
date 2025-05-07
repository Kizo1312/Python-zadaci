lista=[]
istina= False
import os
try:
    with open("evidencija.txt", "x+") as f:
        for i in range(5):
            ucenik = input("Unesi ucenika:")
            ime,prezime,ocjena= map(str,ucenik.split(","))
            lista.append([ime,prezime,ocjena])

            f.write(ucenik +"\n")        
            f.seek(0)
            print(f.readline())
except:
    with open("evidencija.txt", "a+") as f:
        while True:
            unos = int(input("1: Dodavanje novih zapisa\n 2: Prikaz svih zapisa\n 3: Pretrazi po prezimenu\n 4:Brisanje datoteke"))
            if unos == 0:
                continue
            if unos == 1:
                ucenik = input("Unesi ucenika:")
                ime,prezime,ocjena= map(str,ucenik.split(","))
                f.write(ucenik + "\n")        

                lista.append([ime,prezime,ocjena])
            elif unos == 3:
                search = input("Upisi prezime")
                for i in range(len(lista)):
                    for j in range(len(lista[i])):
                        if lista[i][1] == search:
                            
                            istina= True
                    if istina== True:
                        print(lista[i])
                        istina = False
                        break
                else:
                    print(search, "nije na popisu")
            elif unos== 2:
                print(f.readline())
            elif unos == 4:
                if os.path.exists("evidencija.txt"):
                    os.remove("evidencija.txt")
                else:
                    print("The file does not exist")
                break


        

                            
                
            


