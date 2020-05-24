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

products[0][0] #找第一個清單的第一個



