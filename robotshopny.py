class Product: 
	def __init__(self, price, count,tax):
		self.price = price
		self.count = count
		self.tax = tax
	
	def price_with_tax(self):
		total_price = self.price * self.count * self.tax
		if total_price > 500: 
			return 0.9 * total_price
		else: 
			return total_price

	
products = [Product(price = 900, count = 2, tax = 1.25), Product(price = 100, count = 1, tax = 1.06)]
total_price = 0


for p in products:
	total_price = total_price + p.price_with_tax()

	

print(total_price)






