n = int(input())
a = 1
b = 1
num = 0
lista = [a,b]
for i in range(2,n):
    
    num = a+b
    lista.append(num)
    a= lista[i-1]
    b= lista[i]
print(lista)
