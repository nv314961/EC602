#include <iostream>
#include <vector>

using namespace std;

#include "polyops.cpp"

int main(){ 
  int Alen,Blen;

  cout << "Length of Vector A: ";
  cin >> Alen;
  cout << "Length of Vector B: ";
  cin >> Blen;

  Poly A(Alen,0),B(Blen,0);

  cout << "Enter coefficients of Polynomial A, starting with the highest power:" << endl;
  for (auto& e : A)
     cin >> e;
 
  cout << "Enter coefficients of Polynomial B, starting with the highest power:" << endl;
  for (auto& e : B)
     cin >> e;

  cout << "A + B = ";
  for (auto e : add_poly(A,B))
     cout << e << " ";
  cout << endl;

  cout << "A * B = ";
  for (auto e : multiply_poly(A,B))
     cout << e << " ";
  cout << endl;  


}