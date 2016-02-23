from sys import argv

script, filename = argv

#fun() to read the file through read() command
def readfile(f):
    print f.read()

#fun() to adjust the pointer. the value in seek() command is offset(for number of bytes). By default it is set to 0 that is start of the file.
def rewind(f):
    f.seek(10)

#this fun() reads the file by reading 1 line at a time. the command readline() reads a single line.
#The file f responsible for maintaining the current position in the file after each readline() call.
position in the fi le after each readline()
def read_a_line(line_cnt, f):
    print line_cnt, f.readline(),
    
cfile= open(filename)

print "let's print the file..."

readfile(cfile)

print "rewinding it..."
rewind(cfile)
cline=1
print "now printing line by line..."
read_a_line(cline,cfile)
cline+=1
read_a_line(cline, cfile)
cline+=1
read_a_line(cline,cfile)
