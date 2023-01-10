text = list(input())
print(len(list(filter(lambda x: (x.islower()), text))))
print(len(list(filter(lambda x: (x.isupper()), text))))