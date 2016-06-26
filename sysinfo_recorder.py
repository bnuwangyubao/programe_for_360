#!/usr/bin/env python

import time
import os

totalLine=0

if os.path.exists("CPUInformation"):
	os.remove("CPUInformation")
while (1):
	f = open('/proc/stat')
	lines=f.readlines();
	f.close()
	for line in lines:
		line=line.lstrip()
		if line.startswith('cpu'):
			break;
	if totalLine<100:
		fwrite_append=file("CPUInformation","a+")
		fwrite_append.write(line)
		fwrite_append.close()
		totalLine=totalLine+1
	else:
		fwrite_new=file("CPUInformation","w+")
		fwrite_new.write(line)
		fwrite_new.close()
		totalLine=1
	time.sleep(1)
