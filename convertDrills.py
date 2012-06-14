#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sy
import string

fin = open('test.nc','r')
fout = open ('test_modified.nc','w')
justMark = True

for line in fin:
	modified = False
	temp = ""
	commands = string.split(line)
	if commands[0] == "G81":
		# Start conversion
		if justMark:
			temp = "G1 Z-0.5 F80\n"
		else:
			temp = "G1 " + commands[3] + " F80\n" 
		modified = True
	
	if commands[0] == "G98":
		modified = True
	
	if commands[0] == "G80":
		temp = "G1 Z3.0\n"
		modified = True
		
	if modified:
		fout.write(temp)
	else:
		fout.write(line)

fin.close()
fout.close()



