// Copyright 2017 Nick VanDeusen nv314961@bu.edu
// Copyright 2017 Michael Graziano mjgrazia@bu.edu

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <functional>
#include <algorithm>
#include <math.h>

using namespace std;

class obj {
public:
	string id;		// id assigned by user
	double xPos;	// x-position
	double yPos;	// y-position
	double xVel;	// x-velocity
	double yVel;	// y-velocity
	double currentTime; // track status of the ball over time
	double radius = 5; // every object has a fixed radius of 5 units
};

// colliding particles
vector <int> colliders;

// Determine if command line inputs are valid
bool is_number(string s) {
	string::iterator it;
	for (it = s.begin(); it < s.end(); it++) {
		if (!(isdigit(*it) || *it == '.' || *it == '-'))
			return false;
	}
	return true;
}

// Convert string to double; 10 decimal places
double stod_p(string num) {
	stringstream svalue(num);
	double val;

	svalue >> val;

	return val;
}
vector <double> get_times(int argc, char* argv[]) {
	// If user has not entered any time values, exit with return code 2
	if (argc < 2)
		exit(2);

	// Retrieve time values from command line
	vector <double> time;
	for (int i = 1; i < argc; i++) { // ignore argv[0].
									 // time values must be numbers and > 0
		if (is_number(argv[i])) {
			double t = atof(argv[i]);
			if (t > 0)
				time.push_back(t);
			else
				exit(2);
		}
		else
			exit(2);
	}

	// Sort time values in ascending order
	sort(time.begin(), time.end(), less<double>());

	return time;
}

vector <obj> get_objects() {
	vector <obj> particles;	  // vector of particles
	string line;			  // temp; each line of input file
	string currToken;		  // temp; each word within a line
	obj P;				      // create new particle object

	while (getline(cin, line)) {
		int tokenCount = 0;
		istringstream tokens1(line); // convert line string to a string stream
		while (tokens1 >> currToken)		// determine how many tokens are in each line of input
			tokenCount++;
		if (tokenCount != 5)
			exit(1);

		// check validity of data; store in particle object
		istringstream tokens2(line);		// create another stream from line
		vector <double> coords;
		tokens2 >> currToken;			// retrieve first token in string stream
		P.id = currToken;				// assign first token of string to particle ID

										// Ensure the reamining tokens can be represented as a double
		while (tokens2 >> currToken) {
			if (!is_number(currToken))
				exit(1);				// another case of invalid input
										// Store valid coords into a double vector
			coords.push_back(stod_p(currToken));
		}
		tokens2.clear();


		// Store contents of double vector in object
		P.xPos = coords.at(0);
		P.yPos = coords.at(1);
		P.xVel = coords.at(2);
		P.yVel = coords.at(3);
		P.currentTime = 0;

		particles.push_back(P);		// add new particle to particle vector
	}
	return particles;
}

obj collision(obj A, obj B) {
	double sep_dist = A.radius + B.radius;

	double unit_vector_x = (A.xPos - B.xPos) / sep_dist;
	double unit_vector_y = (A.yPos - B.yPos) / sep_dist;

	double diff_xVel = A.xVel - B.xVel;
	double diff_yVel = A.yVel - B.yVel;

	double coef = diff_xVel*unit_vector_x + diff_yVel*unit_vector_y;

	A.xVel = A.xVel - coef*unit_vector_x;
	A.yVel = A.yVel - coef*unit_vector_y;

	return A;
}


// Check if there are upcoming collisions


bool check_direction(double col_time, obj A, obj B) {
	double A_coll_xPos = A.xPos + col_time*A.xVel;
	double A_coll_yPos = A.yPos + col_time*A.yVel;

	double B_coll_xPos = B.xPos + col_time*B.xVel;
	double B_coll_yPos = B.yPos + col_time*B.yVel;

	double test_point_xPos = (abs(B_coll_xPos) - abs(A_coll_xPos)) / 2;
	double test_point_yPos = (abs(B_coll_yPos) - abs(A_coll_yPos)) / 2;

	double A_vector_xPos = test_point_xPos - A_coll_xPos;
	double A_vector_yPos = test_point_yPos - A_coll_yPos;

	double B_vector_xPos = test_point_xPos - B_coll_xPos;
	double B_vector_yPos = test_point_yPos - B_coll_yPos;

	double test_A = A_vector_xPos * A.xVel + A_vector_yPos * A.yVel;
	double test_B = B_vector_xPos * B.xVel + B_vector_yPos * B.yVel;

	return ((test_A >= 0) || (test_B >= 0));
}

double collision_time(obj A, obj B) {
	double delta_xPos = B.xPos - A.xPos;
	double delta_yPos = B.yPos - A.yPos;
	double delta_xVel = B.xVel - A.xVel;
	double delta_yVel = B.yVel - A.yVel;

	double a = delta_xVel*delta_xVel + delta_yVel*delta_yVel;
	double b = 2 * (delta_xPos * delta_xVel + delta_yPos*delta_yVel);
	double c = delta_xPos*delta_xPos + delta_yPos*delta_yPos - (A.radius + B.radius)*(A.radius + B.radius);

	double discriminant = b*b - 4 * a*c;

	if (discriminant > 0) { // two real roots
		double t1 = (-b + pow(discriminant, 0.5)) / (2 * a);
		double t2 = (-b - pow(discriminant, 0.5)) / (2 * a);
		if ((t1 < t2) && (t1 >= 0) && check_direction(t1, A, B))
			return t1;
		else if ((t2 < t1) && (t2 >= 0) && check_direction(t2, A, B))
			return t2;
		else
			return INFINITY;
	}
	else if (discriminant == 0) { // one real root
		double t = (-b + sqrt(discriminant)) / (2 * a);
		if ((t > 0) && check_direction(t, A, B))
			return t;
		else
			return INFINITY;
	}
	else { // complex roots
		return INFINITY;
	}

}

double get_collisions(vector <obj> particles, double last_time) {
	double calc_time = INFINITY;
	double best_time = INFINITY;
	if (particles.size() >= 2) {
		for (int i = 0; i < particles.size(); i++) {
			for (int j = i + 1; j < particles.size(); j++) {
				calc_time = collision_time(particles.at(i), particles.at(j)) + last_time;
				if (calc_time == INFINITY)
					continue;
				else if (calc_time < best_time) {
					best_time = calc_time;
					colliders.clear();
					colliders.push_back(i);
					colliders.push_back(j);
				}
				else if (calc_time == best_time) {
					colliders.push_back(i);
					colliders.push_back(j);
				}
				else
					continue;
			}
		}
	}
	return best_time;
}

// Update positions of particles for each time interval given (no collisions)
vector <obj> update_pos(vector <obj> particles, double time) {
	for (int i = 0; i < particles.size(); i++) {
		particles.at(i).xPos += particles.at(i).xVel*(time - particles.at(i).currentTime);
		particles.at(i).yPos += particles.at(i).yVel*(time - particles.at(i).currentTime);
		particles.at(i).currentTime = time;
	}
	return particles;
}

vector <string> stringOut(vector <obj> particles, vector <string> results, double time) {
	string currentLine;
	obj P;
	currentLine = to_string(time);
	results.push_back(currentLine);

	for (int i = 0; i < particles.size(); i++) {
		P = particles.at(i);
		currentLine = P.id + " " + to_string(P.xPos) + " " + to_string(P.yPos) + " " + to_string(P.xVel) + " " + to_string(P.yVel);
		results.push_back(currentLine);
	}
	return results;
}

int main(int argc, char* argv[]) {

	vector <double> time = get_times(argc, argv);
	vector <obj> objects = get_objects();
	double bestTime = get_collisions(objects, 0);
	bool multi_collide = false;
	double last_collide;

	vector <string> results;

	for (int i = 0; i < time.size(); i++) {
		while ((time.at(i) > bestTime) || multi_collide) {
			objects = update_pos(objects, bestTime);
			for (int j = 0; j < colliders.size(); j = j + 2) {
				obj A = objects.at(colliders.at(j));
				obj B = objects.at(colliders.at(j + 1));
				obj A_copy = A;
				A = collision(A, B);
				B = collision(B, A_copy);
				objects.at(colliders.at(j)) = A;
				objects.at(colliders.at(j + 1)) = B;
			}
			colliders.clear();
			last_collide = bestTime;
			bestTime = get_collisions(objects, bestTime);

			if (last_collide == bestTime)
				multi_collide = true;
			else
				multi_collide = false;
		}
		objects = update_pos(objects, time.at(i));
		results = stringOut(objects, results, time.at(i));
	}
	cout.precision(10);
	// write results to cout
	for (int i = 0; i < results.size(); i++) {
		cout << fixed << results.at(i) << endl;
	}

	return 0;
}