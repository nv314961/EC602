# Copyright 2017 Nick VanDeusen nv314961@bu.edu

#!/usr/bin/python

Table = "{:<6} {:<22} {:<22} {:<22}"

print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))

for x in range(1, 9): # 1-8 bytes
	bytes = x
	max_unsigned = 2**(8*x)-1 # (2^(# of bytes)) - 1
	min_signed = int(-(2**(8*x))/2) # int() used to truncate the 0 after the decimal.
	max_signed =  int(((2**(8*x))/2))-1
	print(Table.format(bytes, max_unsigned, min_signed, max_signed))