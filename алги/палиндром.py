class palindrome():
	"""docstring for palindrome"""
	def __init__(self,string):
		super(palindrome, self).__init__()
		
		self.string=string
	def with_dashes_and_without_elements(string):
			return string
	def only_letters_or_nums(string):
		elements="`' /.,_=+-)(*&^%$#@!№;:?"
		for i in elements:
			if i in string:
				print(i)
				string.remove(i)
		return(string)
test='123!@#321'
test=test.only_letters_or_nums(test)
print(test)
'''not ready'''