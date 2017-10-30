# Copyright 2017 Nick VanDeusen nv314961@bu.edu

#!/bin/sh

# compiles the C++ program to an executable called "fourargs"
g++ fourargs.cpp -o fourargs

# runs the python program with 6 arguments
python fourargs.py one two three four five six

# runs the python program with 3 arguments
python fourargs.py one two three

# runs the C++ program with 6 arguments
fourargs one two three four five six

# runs the C++ program with 3 arguments
fourargs one two three