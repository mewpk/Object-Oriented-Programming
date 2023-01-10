str = list(input())
print(len(list(filter(lambda x: (x.islower()), str))))
print(len(list(filter(lambda x: (x.isupper()), str))))