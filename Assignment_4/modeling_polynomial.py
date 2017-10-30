# Copyright 2017 Nick VanDeusen nv314961@bu.edu
class Polynomial():
# implement a constructor which takes a sequence and 
# assigns the coefficients in the natural (descending order).
	def __init__(self, terms):
		self.terms = dict()
		N = len(terms)
		for i in range(0, N):
			self.terms[N-i-1] = terms[i]
		
# implement a convenient way to print polynomials for debugging purposes		
	def __repr__(self):
		return repr(self.terms)
		
# add two polynomials
	# def __add__():
	
# # subtract two polynomials
	# def __sub__():
	
# # multiply two polynomials
	# def __mul__():
	
# # test for equality between two polynomials
	# def __equals__():
	
# # handle sparse polynomials
	# def __sparse__():
	
# evaluate polynomial given a value for x
	def evalPoly(self, xval):
		sum = 0
		for i in self.terms:
			sum += self.terms[i]*xval**i
		return sum
		
# implement getter, e.g. A[0] would return the first value in Poly A
	def __getitem__(self, index): #in Python, __getitem__ overrides object[index]
		return self.terms[index]
	
# implement setter, e.g. A[0] = 12 would add the key pair [0:12] to the dict
	def __setitem__(self, index, value): #in Python, __setitem__ overrides object[index] = value
		self.terms[index] = value
		
# # compute the derivative of a polynomial
	# return a new list with {power-1: coeff*power, ...}
	#def __deriv__():
	#	for i in self.terms:
	#	
	#	return

def main():
	# create new polynomial as dictionary
	A = Polynomial([2, 1, 3])
	# After passing through constructor, A is a dictionary with the format
	# A = {coeff:power, ...}
	
	# __repr__ allows us to print our polynomial object
	print ("A = ", A)
	
	# print the coefficient corresponding power 0
	print("constant term = ", A[0])

	# test setter: adds 24*x**5 to the polynomial object
	#A[5] = 24
	#print ("A = ", A)
	
	# test neg: adds 2*x**-2 to the polynomial object
	A[-2] = 2
	print ("A = ", A)
	
	# Retreiving the first value of Polynomial A
	#print("A[0] = ", A[0]) # this is valid syntax because of __getitem__

	# test eval method
	result = Polynomial.evalPoly(A, 3)
	print(A, "when x=1 equals", result)
	
	#############################
	
	# create a second polynomial
	B = Polynomial([1, 5, 3, 2, 0, 7])
	print ("B = ", B)
	
	# test add
	#C = A + B
	#print ("C = A + B = ")
	
	# test subtract
	#D = A - B
	#print ("D = A - B = ")
	
if __name__=="__main__":
	main()