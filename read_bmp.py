import struct 
import sys

#(tries to) read a bmp file and extract basic data out of it  
if not len(sys.argv) == 2:
	print "Usage: python read_bmp.py <file name>" 
	exit()
file = sys.argv[1]
f = open(file, 'rb')

#Header is first 2 chars
header = f.read(2)
print "Header: %s"%header

#file size
f_size = f.read(4)
f_size = struct.unpack('i',f_size)[0]
f_size_f = f_size/1024.0/1024.0
print "File size: %i bytes = %.6f MB"%(f_size,f_size_f)

#junk 
f.read(4)

#data start offset
data_start = f.read(4)
data_start = struct.unpack('i',data_start)[0]
print "Data starts at: 0x%x"%data_start
#header size
header_size = f.read(4)
header_size = struct.unpack('i',header_size)[0]

#image width
width = f.read(4)
width = struct.unpack('i',width)[0]

#image height
height = f.read(4)
height= struct.unpack('i',height)[0]
print "Dimensions: %dx%d pixels"%(height,width)

#nb_plan?
nb_plan = f.read(2)
nb_plan= struct.unpack('h',nb_plan)[0]
print "nb_plan: %d"%nb_plan

#bpp?
bpp = f.read(2)
bpp= struct.unpack('h',bpp)[0]
print "bpp: %d"%bpp

#compression
compress = f.read(4)
compress= struct.unpack('i',compress)[0]
print "Compression: %s" % "Uncompressed" if compress==0 else "Compressed"

#image size
i_size = f.read(4)
i_size= struct.unpack('i',i_size)[0]
i_size_f = i_size/1024.0/1024.0
print "Image size: %i bytes = %.6f MB"%(i_size,i_size_f)