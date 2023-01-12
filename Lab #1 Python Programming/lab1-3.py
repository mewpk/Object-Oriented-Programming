def calculateTime(listNumber):
  listNumber[0] += listNumber[1] / 60
  listNumber[2] += listNumber[3] / 60
  time = listNumber[2] - listNumber[0]
  if time < 0.15:
    return 0
  if time % 1 :
    time += 1
  if time >= 6:
    return 200
  elif time > 4:
    return round((time - 3)) * 20 + 30
  else:
    return round(time) * 10
print(calculateTime(list(map(int, input().split()))))