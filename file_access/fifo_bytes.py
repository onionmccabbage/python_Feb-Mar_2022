# Python can read and write byte files (as well as the default text files)
b = bytes( range(0,256) ) # 0-255 are the first 256 characters
# print(b)

fout = open('bfile', 'wb') # 'w' to (over)write 'b' for bytes
fout.write(b)
fout.close()

# read bytes in
fin = open('bfile', 'rb')
r = fin.read()
fin.close()

print(r)