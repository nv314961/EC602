# Copyright 2017 Nick VanDeusen nv314961@bu.edu

#!/usr/bin/python

import sys

# sys.argv: a list of present arguments
# len(sys.argv): # of arguments

if len(sys.argv) <= 5:
	# send first x arguments through stdout (where x is 1-4)
	for x in range(1,len(sys.argv)):
		print(sys.argv[x]);
else:
	# send first 4 arguments through stdout...
	for x in range(1, 5):
		print(sys.argv[x]);
	# ... and the remaining through stderr
	for x in range(5, len(sys.argv)):
		sys.stderr.write(sys.argv[x] +'\n');