import statistics
ocjena = list(map(int, input().split(" ")))
zbroj = 0



print(statistics.mean(ocjena))
print(statistics.median(ocjena))
print(statistics.mode(ocjena))