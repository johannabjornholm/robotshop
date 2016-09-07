class Product: 
	def __init__(self, price, count,tax):
		self.price = price
		self.count = count
		self.tax = tax



robot = Product(price = 900, count = 2, tax = 1.25)

book = Product(price = 100, count = 1, tax = 1.06)



print(self.price * self.count * self.tax + self.price * self.count * self.tax)