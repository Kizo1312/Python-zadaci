
def obrni(rijec):
    
   
    
    if len(rijec) ==0:
        return ""
    else:
        return rijec[-1] + obrni(rijec[:-1]) 
print(obrni("toma"))


def palindrom(rijec):
    if len(rijec) ==0 or len(rijec) == 1:
        return True
    elif rijec[0]!=rijec[-1]:
        return False
        
    else: return palindrom(rijec[1:-1])

    
print(palindrom("radar"))