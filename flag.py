import price
import indicator
#I CAN do here whatever I want because I am MASTER
class Flag:
	def __init__(self):
		self.Price = price.Price()
		self.Price.parse()
		self.Indicator = indicator.Indicator()

