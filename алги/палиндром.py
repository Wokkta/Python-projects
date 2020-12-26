class palindrome():
	"""docstring for palindrome"""
	def __init__(self,string):
		super(palindrome, self).__init__()
		
		self.string=string
	def as_givved(self,string):
		for i in range(1,len(self.string)//2):
			if self.string[i-1]!=self.string[-i]:
				return False
		return True
	def with_dashes_and_without_elements_without_register(self,string):
		elements="`'/.,_=+-)(*&^%$#@!№;:?"
		self.string=self.string.lower()
		for i in elements:
			if i in self.string:	
				self.string=self.string[:self.string.index(i)]+self.string[self.string.index(i)+1:]
		for i in range(1,len(self.string)//2):
			if self.string[i-1]!=self.string[-i]:
				return False
		return True
	def with_dashes_and_without_elements_with_register(self,string):
		elements="`'/.,_=+-)(*&^%$#@!№;:?"
		for i in elements:
			if i in self.string:	
				self.string=self.string[:self.string.index(i)]+self.string[self.string.index(i)+1:]
		for i in range(1,len(self.string)//2):
			if self.string[i-1]!=self.string[-i]:
				return False
		return True


	def only_letters_and_nums_with_register(self,string):
		elements="`' /.,_=+-)(*&^%$#@!№;:?"
		for i in elements:
			if i in self.string:	
				self.string=self.string[:self.string.index(i)]+self.string[self.string.index(i)+1:]
		for i in range(1,len(self.string)//2):
			if self.string[i-1]!=self.string[-i]:
				return False
		return True
	def only_letters_and_nums_without_register(self,string):
		self.string=self.string.lower()
		elements="`' /.,_=+-)(*&^%$#@!№;:?"
		for i in elements:
			if i in self.string:	
				self.string=self.string[:self.string.index(i)]+self.string[self.string.index(i)+1:]
		for i in range(1,len(self.string)//2):
			if self.string[i-1]!=self.string[-i]:
				return False
		return True


test="q q "
test=palindrome(test)
print(test.only_letters_and_nums_with_register(test))
print(test.with_dashes_and_without_elements_with_register(test))

'''not ready'''