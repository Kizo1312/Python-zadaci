import tkinter


num = int(input())

def faktorijel(n):
    if n==1:
        return 1
    else:
        return n + faktorijel(n -1)
print(faktorijel(5))

def znamenke(n):
    1
    if n < 10:
        return 1
    else:
        return 1+ znamenke(n//10)
    
   
print(znamenke(num))