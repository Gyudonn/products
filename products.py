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