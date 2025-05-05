n = int(input())
x = int(input())
klime = []
upaljeni = 0
ugaseni= 0
def create ():
    klima = {
    "on": False,
    "index": 0,
    "count":0
}
    return klima



for i in range(n):
    klime.append(create())
    
   
for i in range(len(klime) ):
    klime[i]["index"] =i+1

print(klime)
print(len(klime))

for i in range (x):
    si = int(input())
    if si == klime[i]["index"]:
        klime[i]["count"] +=1
        if klime[i]["count"] %2 == 0:
            klime[i]["on"]= False
        else:
            klime[i]["on"]= True

print(klime)
for i in range( len(klime)):
    if klime[i]["on"] == True:
        upaljeni += 1

    else:
        ugaseni+=1
print(upaljeni)






