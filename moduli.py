import matematika
import math
import random
from datetime import datetime
print (matematika.kvadrat(3.12,5))
print(math.sqrt(25))
print(math.pi)
print(matematika.korijen(49))
print(math.floor(2.7))
print(math.ceil(2.3))
print(round((3*3)*math.pi, 2))
print(round((2*3)* math.pi, 2))
print(matematika.hipotenuza(3,4))

while(True):
    num= random.randint(1,100)
    if num % 5 == 0:
        
        break
print(num)

trenutno = datetime.now()
print(trenutno)
print(trenutno.date())
print(trenutno.strftime("%H:%M:%S"))    