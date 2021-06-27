products = []

while True:
	name = input('input the product name: ')
	if name == 'q':
		break
	price = input('input the product price: ')
	product = [name, price]
	products.append(product)

for product in products:
	print('The price of ' + product[0] + ' is ' + product[1])

with open('product.txt', 'w') as f:
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')