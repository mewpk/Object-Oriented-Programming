products = []
for number1 in range(100,1000):
  for number2 in range(100,1000):
    products.append(number1*number2)
print(max(filter(lambda product: str(product) == str(product)[::-1], products)))
# print(products)