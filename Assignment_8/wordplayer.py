# Copyright 2017 Nick VanDeusen nv314961@bu.edu

import sys

# check if user included the wordlist.txt as a command line argument
if len(sys.argv) < 2:
	print("Please include the wordist text file\n")
	exit(1)

# we expect the wordlist text file to be the first command line argument
wordfile = open(sys.argv[1], 'r')
	
# read input from user
letters, length = input().split()

# format input parameters
letters = set(letters)
length = int(length)

while (length != 0):
	wordlist = []

	# insert contents of wordlist to a list
	for line in wordfile:
		line = line.strip()
		if len(line) == length:
			wordlist.append(line)

	print(wordlist)
	for word in wordlist:
		if (letters & set(word)) and (len(word) == length):
			print(word)
	print('.')
	
	# read in the next request from user
	letters, length = input().split()
	letters = set(letters)
	length = int(length)
	
wordfile.close()
exit(0)