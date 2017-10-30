// Copyright 2017 Nick VanDeusen nv314961@bu.edu

#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;

int main(){
	uint16_t b16 = 1;
	
	clock_t start_clock, end_clock;
	
	// Measure time elapsed from 0 to overflow
	// for a 16-bit integer (in microseconds)
	start_clock = clock();
	
	while (b16 > 0)
		b16++;

	end_clock = clock();

	double b16_time = (static_cast<double>(end_clock - start_clock) / CLOCKS_PER_SEC)*pow(10,6);
	
	// Estimate time elapsed from 0 to overflow
	// for an 8-bit integer (in nanoseconds)
	double b8_time = (b16_time/pow(2,8))*1e3;
	
	// Estimate time elapsed from 0 to overflow
	// for a 32-bit integer (in seconds)
	double b32_time = (b16_time*pow(2,16))/1e6;
	
	// Estimate time elapsed from 0 to overflow
	// for a 64-bit integer (in years)
	double b64_time = (b16_time*pow(2,48))/(1e6*3600*24*365);
	//conversions: [us -> s], [s -> hr], [hr -> day], [day -> year]

	cout << "estimated int8 time (nanoseconds): "
            << b8_time << endl;
	cout << "measured int16 time (microseconds): "
			<< b16_time << endl;
	cout << "estimated int32 time (seconds): "
			<< b32_time << endl;
	cout << "estimated int64 time (years): "
			<< b64_time << endl;
			
	return 0;
}