imena = list(map(str, input().split()))
ime = input()

def binarno(lista, cilj):
    index_od = 0
    for i in range(len(lista)):
        if lista[i] == cilj:
            index_od = i

    lista.sort()
    count = 0
    lijevo = 0
    desno = len(lista) -1
    while lijevo <= desno:
        count+=1
        sredina = (lijevo + desno) //2
        if lista[sredina] == cilj:
            
            
            return f"index:{index_od}, koraci:{count}"
        elif lista[sredina] < cilj:
           
            lijevo = sredina +1
        else:
            
            desno = sredina -1
    return "nema tog imena"
print(binarno(imena, ime))