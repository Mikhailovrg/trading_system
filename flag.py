import price
import indicator

class Flag:
	def __init__(self):
		self.Price = price.Price()
		self.Price.parse()
		self.Indicator = indicator.Indicator()

