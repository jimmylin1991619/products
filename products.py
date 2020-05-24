# 二維度清單
products = []
while True:
	product_name = input('請輸入商品名稱: ')
	if product_name == 'q':
		break
	product_price = input('請輸入商品價格: ')
	p = []
	p.append(product_name)
	p.append(product_price)
	# 上面三行也可以寫成 p = [product_name, product_price]
	products.append(p)
print(products)	

 # products[0][0] #找第一個清單的第一個

for product in products:
	#print(product)
	print(product[0], '的價格是', product[1])

# 'abc' + '123' = 'abc123' 字串合併
# 'abc' * 3 = 'abcabcabc' 字串乘法

with open('products.txt', 'w') as f:  # 'w'寫入模式
	for product in products:
		f.write(product[0] + ',' + ' 商品價格: ' + product[1] + '\n')

with open('products.csv', 'w') as f:  # 'w'寫入模式
	for product in products:
		f.write(product[0] + ',' + ' 商品價格: ' + product[1] + '\n')
