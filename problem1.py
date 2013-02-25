#! /usr/bin/env python


result = 0

for count in range(3,1000):
	if (count % 3 == 0) or (count % 5 == 0):
		 result += count
	
print "result == ", result  
