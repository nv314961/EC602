# Copyright 2017 Nick VanDeusen nv314961@bu.edu
class Polynomial(object):
# implement a constructor which takes a sequence and 
# assigns the coefficients in the natural (descending order).
	def __init__(self, terms=None):
		if terms is None:
			self.terms = {}
		else:
			self.terms = dict()
			N = len(terms)
			for i in range(0, N):
				self.terms[N-i-1] = terms[i]
				
# implement a convenient way to print polynomials for debugging purposes		
	def __repr__(self):
		return repr(self.terms)
		
# add two polynomials
	def __add__(self, polyB):
		result = Polynomial([])
		if max(self.terms.keys()) >= max(polyB.terms.keys()):
			for i in self.terms:
				if i in polyB.terms:
					result[i] = self.terms[i] + polyB.terms[i]
				else:
					result[i] = self.terms[i]
			for i in polyB.terms:
				if i not in self.terms:
					result[i] = polyB.terms[i]
		else:
			for i in polyB.terms:
				if i in self.terms:
					result[i] = self.terms[i] + polyB.terms[i]
				else:
					result[i] = polyB.terms[i]
			for i in self.terms:
				if i not in polyB.terms:
					result[i] = self.terms[i]
		for i in self.terms:
			if i in polyB.terms:
				result[i] = self.terms[i] + polyB.terms[i]
			else:
				result[i] = self.terms[i]
		for i in polyB.terms:
			if i not in self.terms:
				result[i] = polyB.terms[i]		
		return result
	
# subtract two polynomials
	def __sub__(self, polyB):
		result = Polynomial([])
		# since i can't import a library to sort dictionaries,
		# we will determine which polynomial is the higher degree
		if max(self.terms.keys()) >= max(polyB.terms.keys()):
			for i in self.terms:
				if i in polyB.terms:
					result[i] = self.terms[i] - polyB.terms[i]
				else:
					result[i] = self.terms[i]
			for i in polyB.terms:
				if i not in self.terms:
					result[i] = polyB.terms[i]
		else:
			for i in polyB.terms:
				if i in self.terms:
					result[i] = self.terms[i] - polyB.terms[i]
				else:
					result[i] = polyB.terms[i]
			for i in self.terms:
				if i not in polyB.terms:
					result[i] = self.terms[i]
		return result
	
# multiply two polynomials
	def __mul__(self, polyB):
		result = Polynomial([])
		for i in self.terms:
			for j in polyB.terms:
				try:
					result[i+j] += self.terms[i] * polyB.terms[j]
				# a KeyError will occur when one polynomial has a term that does not
				# correspond with the other, e.g. poly A has an x^2 term but poly B does not.
				except KeyError:
					result[i+j] = self.terms[i] * polyB.terms[j]
		return result
		
# test for equality between two polynomials
	def __eq__(self, polyB):
		return self.terms == polyB.terms
	
# evaluate polynomial given a value for x
	def eval(self, xval):
		sum = 0
		for i in self.terms:
			sum += self.terms[i]*xval**i
		return sum
		
# implement getter, e.g. A[0] would return the first value in Poly A
# in Python, __getitem__ overrides object[index]
	def __getitem__(self, index):
		if index not in self.terms:
			return 0
		return self.terms[index]
	
# implement setter, e.g. A[0] = 12 would add the key pair [0:12] to the dict
	def __setitem__(self, index, value): #in Python, __setitem__ overrides object[index] = value
		self.terms[index] = value
		
# compute the derivative of a polynomial
	# return a new list with {power-1: coeff*power, ...}
	def deriv(self):
		result = Polynomial([])
		for i in self.terms:
			if i != 0:
				result[i-1] = i*self.terms[i]
		return result

def main():
	# create new polynomial
	A = Polynomial([8, 7, 3, 4, 1, 7])
	# and another
	B = Polynomial([3, 4, 1, 6])
	
	# After passing through constructor, A is a dictionary with the format
	# A = {power:coeff, ...}

	print("dA/dx = ", A.deriv)
	# __repr__ allows us to print our polynomial object
	print ("A = ", A)
	print ("When x=2, A is: ", A.eval(2))
	#B = A
	print ("B = ", B)
	
	#shared_items = set(A.terms) & set(B.terms) # returns keys that are in both polys
	#print (shared_items)
	
	# test equality
	print("Does A = B? ", A == B)
	
	# test add
	C = A + B
	print ("C = A + B = ", C)
	
	# test subtract
	D = A - B
	print ("D = A - B = ", D)
	
	# test multiply
	E = A * B
	print ("E = A * B = ", E)
	
if __name__=="__main__":
	main()