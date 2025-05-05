t = float(input())
u = input()
def pretvorba(temp, unit):
    if unit == "C":
        temp = temp *(9/5) + 32
        unit = "F"
    else:
        temp = (temp - 32) * 5/9
        unit= "C"
    
    print(f"{round(temp, 2)}°{unit} ") 
pretvorba(t,u)

