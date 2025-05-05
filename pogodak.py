
import random
num = random.randint(1,10)
count=0

while True:
    n = int(input())
    count+=1
    if n == num: 
        print("Bravo")
        break
    else:
        print("pokusaj ponovno")
print(f"Pogodili ste u {count}. pokusaju")
      
