products = []
products_check=[]

while True:
	name = input('input the product name: ')
	if name == 'q':
		with open('product.csv', 'w', encoding = 'utf-8') as f:
			f.write('Good,Price\n')
			for product in products:
				f.write(product[0] + ',' + str(product[1]) + '\n')
		break
	price = input('input the product price: ')
	price = int(price)
	product = [name, price]
	products.append(product)

for product in products:
	print('The price of ' + product[0] + ' is ' + str(product[1]))

with open('product.csv' , 'r', encoding = 'utf-8') as file:
			for line in file:
				name, price = line.strip().split(',')
				product = [name, price]
				products_check.append(product)
print(products_check)