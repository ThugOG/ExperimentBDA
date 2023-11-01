class BloomFilter:
	def __init__(self, size, hash_functions):
		self.size = size
		self.bit_array = [False] * size
		self.hash_functions = hash_functions
		
	def add(self, item):
		for func in self.hash_functions:
			index = func(item) % self.size
			self.bit_array[index] = True
			
	def __contains__(self, item):
		for func in self.hash_functions:
			index = func(item) % self.size
			if not self.bit_array[index]:
				return False
		return True
		
def importFile(file_path):
	item_list = []
		
	try:
		with open(file_path, 'r') as file:
			for line in file:
				cleaned_line = line.split(",")
				for x in cleaned_line:
					item_list.append(x)
					
	except FileNotFoundError:
		print(f"The file '{file_path}' was not found.")
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		
	return item_list
