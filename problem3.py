#! /usr/bin/env python

result = 2
value = 0
previous = 2
secondLast = 1

while value < 4000001:
	value = previous + secondLast
	secondLast = previous
	previous = value

	if value & 1 != 1:
		result += value

print "Sum =", result
