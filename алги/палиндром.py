class palindrome():
	"""docstring for palindrome"""
	def __init__(self,string):
		super(palindrome, self).__init__()
		
		self.string=string
	def with_dashes_and_without_elements(self,string):
			return self.string
	def only_letters_or_nums(self,string):
		elements="`' /.,_=+-)(*&^%$#@!№;:?"
		for i in elements:
			if i in self.string:
				print(i)
				self.string=self.string[:self.string.index(i)]+self.string[self.string.index(i)+1:]
		return(self.string)
test='123!@#321'
test=palindrome(test)
test=test.only_letters_or_nums(test)
print(test)
'''not ready'''