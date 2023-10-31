#!/usr/bin/env python

import sys

row_a, col_b = 5,5

for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "A":
	    for i in xrange(0,col_b):
		key = row + "," + str(i)
		print("%s\t%s\t%s"%(key,col,value))
	else:
	    for j in xrange(0,row_a):
		key = str(j) + "," + col 
	    	print("%s\t%s\t%s"%(key,row,value))
