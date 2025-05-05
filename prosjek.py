ocjene = list(map(int, input().split(" ")))
zbroj = 0
count =0
for i in range (len(ocjene)):
    zbroj+=ocjene[i]

prosjek = round(zbroj / len(ocjene), 2)

for i in range(len(ocjene)):
    if ocjene[i] == 1:
        count+=1
print(count)


if count >0:
    print("nedovoljan")
elif prosjek >= 4.5:
    print(prosjek, "odlican")
elif prosjek >= 3.5 and prosjek <4.5:
    print(prosjek, "vrlo dobar")
elif prosjek >= 2.5 and prosjek <3.5:
    print(prosjek, " dobar")
elif prosjek >= 1.5 and prosjek <2.5:
    print(prosjek, "dovoljan")
else:
    print(prosjek, "nedovoljan")
