n = int(input())
m = int(input())
odrezano =0
lista = []
for i in range(n):
    num = int(input())
    lista.append(num)
visina = max(lista)
while odrezano < m:
    odrezano =0
    visina -=1
    for i in range(len(lista)):
        if lista[i] > visina:
            odrezano = odrezano +(lista[i] - visina)
    
print("visina:",visina)
        

        

