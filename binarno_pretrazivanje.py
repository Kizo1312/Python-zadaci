brojevi = list(map(int, input().split()))
broj = int(input())

def binarno(lista, cilj):
    count = 0
    lijevo = 0
    desno = len(lista) -1
    while lijevo <= desno:
        count+=1
        sredina = (lijevo + desno) //2
        if lista[sredina] == cilj:
            
            
            return f"index:{sredina}, koraci:{count}"
        elif lista[sredina] < cilj:
           
            lijevo = sredina +1
        else:
            
            desno = sredina -1
    return "nema tog borja"
print(binarno(brojevi, broj))