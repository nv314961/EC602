# Copyright 2017 Nick VanDeusen nv314961@bu.edu

from numpy import zeros, exp, array, pi #, fft, set_printoptions, allclose

# x: valid sequence of numbers
# N: length/size of x
def DFT(x):
	# ensure input is some type of sequence (must have a "length" attribute)
	# exception here is dict; do not accept an input of type 'dict'
	if not hasattr(x, '__len__') or isinstance(x, dict):
		print("input is not a sequence at all!")
		raise ValueError
	
	N = len(x)
	# ensure each element of the input is a number
	for i in range(N):
		# If current entry is a string or some type of list, it's not a valid number
		if isinstance(x[i], str) or hasattr(x[i],'__len__'):
			print("sequence contains a non-number entry")
			raise ValueError
			
	X = zeros((N,), dtype=complex)
	
	# Compute DFT
	for k in range(N):
		for n in range(N):
			X[k] += x[n]*exp(-1j * 2*pi * k * n / N)

	return X

def main():
	#x = 5
	x  = (1,2,3,4,5,6,7,8)
	#x = array([1,2,3,"4",5,6,7,8])
	#print(type(x))
	DFT(x)
	
if __name__ == '__main__':
    main()