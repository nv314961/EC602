// Copyright 2017 Nick VanDeusen nv314961@bu.edu

#include <iostream>
using namespace std;

int main(int argc, char* argv[]){
	// argc: number of arguments present
	// argv[]: character array of the arguments

	// if argc < 5, end for loop at argc rather than '5'
	/* we are ommitting argument 0, so argc <= 5 means
	   the user has entered 4 or less arguments. */
	if(argc <= 5){
		// send first x arguments through stdout (where x is 1-4)
		for(int i=1; i<argc; i++){
			cout << argv[i] << endl;
		}
	}
	else{
		// send first 4 arguments through stdout...
		for(int i=1; i<5; i++){
			cout << argv[i] << endl;
		}
		// ... and the remaining through stderr
		for(int i=5; i<argc; i++){
			cerr << argv[i] << endl;
		}
	}

	return 0;
}