// Copyright 2017 Nick VanDeusen nv314961@bu.edu

#include <iostream>
#include <math>

using namespace std;

class obj {
public:
	double xPos;	// x-position
	double yPos;	// y-position
	double xVel;	// x-velocity
	double yVel;	// y-velocity

private:
	int radius = 5;	// every object has a fixed radius of 5 units
};

// distance: Math.abs( pow((x1-x2),2) + pow((y1-y2),2) )