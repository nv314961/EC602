// Copyright 2017 Nick VanDeusen nv314961@bu.edu
#include <vector>

using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a,const Poly &b){
	Poly c;
	
	// Determine length of C, based on
	// length of A & B
	int lenC;
	if(a.size() >= b.size())
		lenC = a.size();
	else
		lenC = b.size();
	
	// Perform element-by-element addition
	for(int i=0; i < lenC; i++)
		c.push_back(a[i] + b[i]);
	
	return c;
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a, const Poly &b){
	Poly c( (a.size()+b.size()-1),0);
	
	
	for (int i=0; i < a.size(); i++){
		for(int j=0; j < b.size(); j++){
			c[i+j] += a[i]*b[j];
		}
	}
	
	return c;
}

// multiply:
// (a2x^2 + a1x + a0)(b2x^2 + b1x + b0)
// = (a2*b2)x^4 + (a1*b2 + a2*b1)x^3 + (a0*b2 + a1*b1 + a2*b0)x^2 + (a0*b1 + a1*b0)x + (a0*b0)