stvari = list(map(str,input().split(" ")))
x = str(input())
def postoji(lista,cilj):
    count = 0
    for i in range(len(lista)):
        if stvari[i] == cilj:
            print(f"pronaden na poziciji {i} u {count+1} koraka")
            break
        else:
        
            count+=1

    if count == len(lista):
        print("nije pronadjen")
postoji(stvari,x)