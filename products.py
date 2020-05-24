products = []



# 讀取檔案 
def read_file(filename):
	import os # operating system
	if os.path.isfile(filename): # 檢查檔案在不在資料夾
		print('yeah! 找到檔案了')
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品, 價格' in line:
					continue #繼續=跳到下一迴圈
				product_name, product_price = line.strip().split(',') #split為切割函數，遇到','就切割 strip 為移除換行符號
				products.append([product_name, product_price])
		print(products)
	else:
	print('找不到檔案...')
	return products

# 讓使用者輸入資料 (二維度清單)
def user_input(products):
	while True:
		product_name = input('請輸入商品名稱: ')
		if product_name == 'q':
			break
		product_price = input('請輸入商品價格: ')
		# p = []
		# p.append(product_name)
		# p.append(product_price)
		# 上面三行也可以寫成 p = [product_name, product_price]
		products.append([product_name, product_price])
	print(products)
	return products	

# products[0][0] #找第一個清單的第一個

# 印出所有商品購買紀錄
def print_product(products):
	for product in products:
		#print(product)
		print(product[0], '的價格是', product[1])

# 'abc' + '123' = 'abc123' 字串合併
# 'abc' * 3 = 'abcabcabc' 字串乘法

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:  # 'w'寫入模式
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')

	with open(filename, 'w', encoding = 'utf-8') as f:  # 'w'寫入模式，encoding 寫入utf-8編碼
		f.write('商品, 價格' + '\n')
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')


products = read_file('products.csv')
products = user_file(products)
print_product(products)
write_file('products.csv', products)



# 練習作業 整數存成檔案		
# data = [1, 3, 5, 7, 9]
# with open('test.txt', 'w') as f:
# 	for i in data:
# 		f.write(str(i) + '\n')