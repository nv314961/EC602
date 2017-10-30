// Copyright 2017 Nick VanDeusen nv314961@bu.edu
#include <iostream>
#include <cmath>

using namespace std;

int main(){
	
	// Estimated number of atoms in the Earth
	double atomCount = 1*pow(10,50);
	
	// The major components of Earth (%)
	double nitrogen = 0.78;
	double oxygen = 0.21;
	double water = 0.01;
	
	// Electron counts
	int n_electrons = 7; // number of electrons in a nitrogen atom
	int o_electrons = 8; // number of electrons in an oxygen atom
	int w_electrons = 8; // number of electrons in an h2o atom
	
	// Estimated "bits"
	double bits = atomCount*(nitrogen*n_electrons + oxygen*o_electrons + water*w_electrons);
	
	// Convert bits to terabytes
	double Tbytes = bits/(8*pow(10,12));
	
	// Calc upper and lower bounds; print results
	double upper = Tbytes + Tbytes/2;
	double lower = Tbytes - Tbytes/2;
	cout << Tbytes << endl;
	cout << lower << endl;
	cout << upper << endl;
	
	return 0;
}