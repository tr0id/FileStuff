import sys
import os
import math 

if not len(sys.argv) == 2:
	print "Usage: hexDump.py filename"
	exit()

file = sys.argv[1]
f = open(file, "rb")

if f == 0:
	print "Failed. Cannot open file."
	exit()
cols = 16
size = os.path.getsize(file)
rows = int((size+cols*1.0)/cols*1.0)


counter = 0
bytes_count = 0
sys.stdout.write(" "*10)
for i in xrange(cols):
	sys.stdout.write("%3.2x"%counter)
	counter += 1
sys.stdout.write("\n")
counter = 0
out_buff = ""
space = "| "
for i in xrange (rows):
	out_buff += ("%-9.8x  " % counter)
	buff = [0]*cols
	buff = bytearray(buff)
	if ((bytes_count+cols) >= size):
		space = " "*(((cols-(size-bytes_count))*3))
		space += "| "
		cols = size-bytes_count

	for j in xrange(cols):
		buff [j] = f.read(1);
		bytes_count += 1
		out_buff += ("%-3.2x" % buff[j])
	out_buff += space
	for k in xrange (cols):
		if int(buff[k] < 0x7f and buff[k] > 0x20):
			out_buff += (chr(int(buff[k])))
		else: 
			out_buff += ('.')
	out_buff += ('\n')
	counter += cols
print out_buff