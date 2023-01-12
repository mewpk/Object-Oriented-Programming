from math import ceil
def calculateTime(listNumber):
    listNumber[0] += listNumber[1]/60
    listNumber[2] += listNumber[3]/60
    time = ceil(listNumber[2]-listNumber[0])
    if time >= 6 :
        return 200
    elif time >= 4 :
        return (time-3)*20 + 30
    elif listNumber[2]*60 + listNumber[3] - listNumber[0]*60 + listNumber[1] > 15:
        return time*10
    else :
        return 0
print(calculateTime(list(map(int,input().split()))))