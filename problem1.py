#! /usr/bin/env python


result = 0
count = 3

while count < 1001:
	if (count % 3) == 0 || (count % 5) == 0:
		 result += count
	count++
	
print "result == " + count
