n = int(input())
x = int(input())
z = int(input())
cijena=0
indexi = []
stanice = []
putnici =[]
def create_passenger(index, vrata):
    passenger = {
        "stanice":0,
        "index": index,
        "vrata1": vrata,
        "vrata2":0

    }
    return passenger
for i in range(z):
    z1,z2,z3 = map(int, input().split(" "))
    if z2 in indexi:
        for j in range(len(indexi)):
            if putnici[j]["index"] == z2:
                price = putnici[j]["stanice"]*5
                cijena+=price



        
    else:
        indexi.append(z2)
        putnici.append(create_passenger(z2, z3))
        for j in range(indexi):
            if putnici[j]["index"] ==j:
                putnici[j]["stanice"] +=1
        
print(putnici)

