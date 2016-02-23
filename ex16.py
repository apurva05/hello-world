from sys import argv

script, filename = argv

print "opening the file..."
txt = open(filename,'w+r')

print "truncating the file"
#txt.truncate()

print "now i am going to ask u 3 lines"

line1 = raw_input('line1: ')
line2 = raw_input('line2: ')
line3 = raw_input('line3: ')

print "writing to file"
txt.write(line1)
txt.write('\n')
txt.write(line2)
txt.write('\n')
txt.write(line3)
txt.write('\n')
print txt.read()
print "and finally close it"
txt.close()
