class Price:
	def __init__(self):
		self.Date = []
		self.Open = []
		self.High = []
		self.Low = []
		self.Close = []
		self.Volume = []
		self.Adj_Close = []
	def parse(self, csv_file='table.csv'):
		import csv
		with open(csv_file, 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				self.Date.append(row[0])
				self.Open.append(row[1])
				self.High.append(row[2])
				self.Low.append(row[3])
				self.Close.append(row[4])
				self.Volume.append(row[5])
				self.Adj_Close.append(row[6])
			self.__reverse()
			self.__format()
	def __reverse(self):
		self.Date = self.Date[:0:-1]
		self.Open = self.Open[:0:-1]
		self.High = self.High[:0:-1]
		self.Low = self.Low[:0:-1]
		self.Close = self.Close[:0:-1]
		self.Volume = self.Volume[:0:-1]
		self.Adj_Close = self.Adj_Close[:0:-1]
	def __format(self):
		# Do we need to work with date?
		self.Open = [float(val) for val in self.Open]
		self.High = [float(val) for val in self.High]
		self.Low = [float(val) for val in self.Low]
		self.Close = [float(val) for val in self.Close]
		self.Volume = [float(val) for val in self.Volume]
		self.Adj_Close = [float(val) for val in self.Adj_Close]



if __name__ == "__main__":
	price = Price()
	price.parse()
	print price.Date





