t = int(input())
u = input()
def pretvorba(temp, unit):
    if unit == "C":
        temp = temp *(9/5) + 32
    else:
        temp = (temp - 32) * 5/9
    
    return round(temp, 2)
print(pretvorba(t, u))

