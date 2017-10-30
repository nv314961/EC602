#include <iostream>
#include <vector>

using namespace std;

#include "bigint.cpp"

int main()
{ 

  BigInt A,B;

  cout << "Enter multiplicand: ";
  cin >> A;
  
  cout << "Enter multiplier: ";
  cin >> B;

  cout << A << " * " << B << "= ";
  cout << multiply_int(A,B) << endl;

}