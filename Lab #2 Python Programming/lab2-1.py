listNumber = list(map(int, input().split()))
listNumber.sort()
temp = False
for index in range(len(listNumber)):
  if listNumber[index] == 0:
    temp = True
  elif listNumber[index] > 0 and temp:
    listNumber[0] = listNumber[index]
    listNumber[index] = 0
    break
print(''.join(map(str,listNumber)))