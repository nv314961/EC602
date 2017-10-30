// Copyright 2017 Nick VanDeusen nv314961@bu.edu
#include <vector>
#include <string>
#include <cmath>
using namespace std;

typedef string BigInt;

BigInt multiply_int(const BigInt &a, const BigInt &b){
	// initialize string for the product
	/* a product of any two ints a and b can't have more than
	   a + b digits. */
	BigInt prod(a.size() + b.size(), '0'); 
	
	// store the sum of each pass through the multipland as an entry in this
	// int vector
	vector<int> int_prod(b.size(), 0);
	
	// index used to store values in int_prod
	int i_a = 0;
	
	// To-do: Check if either term is 0
	
	// Start with the ones digit in 'b'
	for(int i = b.size()-1; i >= 0; i--){
		// initialize (or re-initialize) carry 
		int carry = 0;
		// initialize (or reinitialize) sum
		int sum = int_prod[i];
		// initialize digit multiplier
		int place = 0;
		
		// store current digit of b as an integer
		int curB = b[i] - '0'; // neat trick to convert char -> int
		
		// Also start with ones digit in 'a'
		for(int j = a.size() - 1; j >= 0; j--){
			// store current digit of 'a' as an integer
			int curA = a[j] - '0';
			// Compute sum, based on previous carry
			sum += curB*curA + carry;
			carry = sum/10;
			int_prod[i] += sum*pow(10,place);
			place++;
		}
		int_prod[i] = sum;
	}
	
	// add up each entry in int_prod; store in string; return
	int total = 0;
	for(int i = 0; i < int_prod.size(); i++)
		total += (int_prod[i]);
	prod = to_string(total);
	return prod;
}