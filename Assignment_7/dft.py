from numpy import zeros, exp, array, pi #, fft, set_printoptions, allclose

# x: valid sequence of numbers
# N: size of x
def DFT(x):
	# ensure input is a valid numerical sequence
	# raise ValueError
	
	N = x.size
	X = zeros((N,), dtype=complex)
	for k in range(N):
		for n in range(N):
			X[k] += x[n]*exp(-1j * 2*pi * k * n / N)

	#set_printoptions(suppress=True)
	#print(X)
	#Y = fft.fft(x)
	#print(Y)
	#print(allclose(X,Y))

	return X

def main():
	x = array([1,2,3,4,"B",6,7,8])
	DFT(x)
	
if __name__ == '__main__':
    main()