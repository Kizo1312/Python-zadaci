try:
    with open("novooo.txt", "x+") as f:
        
        f.write("Prvi zapis \n")        
        f.seek(0)
        print(f.readline())
except FileExistsError:
    with open("novooo.txt", "a+")as f:
        while True:
            novo = input("unesi ime")
            if novo == "Kraj":
                break
            if novo.count(",") == 2:
                ime, prezime,ocjena = map(str,novo.split(","))
                if ocjena.strip().isdigit() == True:
                    if int(ocjena)>0 and int(ocjena) < 6:
                        f.write(novo + "\n")
                    else:
                        f.write("Kriva ocjena")
                else:
                    f.write("mora biti broj")
                
            
            
