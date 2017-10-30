// Copyright 2017 Nick VanDeusen nv314961@bu.edu
// Definitions:
// Rs = factor by which float is better than int at representing small numbers
// Rm = factor by which float is better than int at representing large numbers
// Ri = factor by which int is better than float at representing integers
//
// Formulas:
//
// Rs = 1 / smallest_float_greater_than_zero
// Rm = maximum_float_value / largest_int_value
//
// Ri = largest_int_value / N
// where N is the largest integer such that all integers 1,2,3,...,N can be
// represented without loss of accuracy by a float of this size.

#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>

int main(){

  double Rs,Ri,Rm;

  // calculate Rs, Ri, and Rm for half/binary16 vs int16_t
  float smallest16 = pow(2,-14); //exponent: 0s everywhere except 1 in LSB; mantissa: 0 across.
  float max_value16 = (2-pow(2,-10))*pow(2,15); // from half-precision wikipedia page
  int16_t max_int16 = pow(2,15)-1; // maximum SIGNED 16-bit integer
  int16_t N16 = pow(2,11);

  Rs = 1/smallest16;	
  Ri = max_int16/N16;			
  Rm = max_value16/max_int16;
  
  std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
  float smallest32 = pow(2,-126); // from single-precision wikipedia page
  float max_value32 = (1-pow(2,-24))*pow(2,128); // from single-precision wikipedia page
  int32_t max_int32 = pow(2,31)-1; // maximum SIGNED 32-bit integer
  int32_t N32 = pow(2,24); 
  
  Rs = 1/smallest32;	
  Ri = max_int32/N32;
  Rm = max_value32/max_int32;
  
  std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for double/binary64 vs int64_t
  double smallest64 = pow(2,-1022); // from double-precision wikipedia page
  double max_value64 = (1+(1-pow(2,-52)))*pow(2,1023); // from double-precision wikipedia page
  int64_t max_int64 = pow(2,63)-1; // maximum SIGNED 64-bit integer
  int64_t N64 = pow(2,53);
  
  Rs = 1/smallest64;	
  Ri = max_int64/N64;
  Rm = max_value64/max_int64;
  
  std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;
  
  return 0;
}