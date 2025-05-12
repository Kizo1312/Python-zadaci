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

def fibonacci(num):
    if num == 1:
        return 1
    elif num==2:
        return 1
    
    
    else:
        return fibonacci(num-1) + fibonacci(num-2)

popis = []
while n > 0:
    popis.append(fibonacci(n))
    n-=1

popis.sort()
print(popis)
