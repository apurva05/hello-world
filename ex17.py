from sys import argv
from os.path import exists

script, src, dest = argv

print "copying from %r file to %r file.." % (src, dest)

fromfile = open(src).read()
#fromdata = fromfile.read()
print "the length of source file is %s " % len(src)
print "does the destination file exists? %s " % exists(dest)
tofile = open(dest, 'w+r')
tofile.write(fromfile)

print "Copying done!!!"
fromfile.close()
tofile.close
