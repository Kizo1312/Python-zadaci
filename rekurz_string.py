
def obrni(rijec):
    
   
    
    if len(rijec) ==0:
        return ""
    else:
        return rijec[-1] + obrni(rijec[:-1]) 
print(obrni("toma"))
