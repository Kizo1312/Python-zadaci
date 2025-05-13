n = int(input())
popis = []
rezultati = []
imena =[]
prezimena = []
for i in range(n):
    student = input().split()
    popis.append(student)

for i in range(len(popis)):
    rezultati.append(popis[i][2])
    imena.append(popis[i][0])
    prezimena.append(popis[i][1])

imena.sort(reverse=True)
prezimena.sort(reverse=True)
rezultati.sort(reverse=True)

print (rezultati)
count =0
while count < n:
    for i in range(n):
    
        if popis[i][2]== rezultati[count]:
            print(popis[i])
    count +=1
             
    

    

