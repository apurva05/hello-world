from sys import argv

scr, username = argv
prompt = "> "

print "Hi %s, I am the %s" % (username, scr)
print "i would like to ask u few questions"
print "do u like me?"
likes = raw_input(prompt)

print "where do u live %s" % username
lives= raw_input(prompt)

print "what kind of computer do u have?"
comp = raw_input(prompt)

print"""Alright, %s
    u said %s about liking me
    u live in %s (not sure where that is)
    and u have %s computer. Nice""" % (username,likes,lives,comp) 
