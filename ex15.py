#imports sys module (library written by other programmers)
from sys import argv

#unpacking of arguments
scr, filename =argv

print "here is your file %s " % filename
#open the specified file name and creats a file object txt
txt = open(filename)

#reading the file by giving read command to file object that is txt
print txt.read()

print "lets do it again!!!"

print("type file name again")

#again taking file name from user, this time using raw_input
file_again = raw_input('> ')

#opne the specified file name and creats the file object txt2

#read the file and print by giving read command to the file object that is txt2 
print txt2.read()
