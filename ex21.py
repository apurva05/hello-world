def add(a,b):
    print"add %r+%r"%(a,b)
    return a+b
    
def sub(a,b):
    print "subtracting %r-%r"%(a,b)
    return a-b
    
def mul(a,b):
    print "multiplying %r*%r" %(a,b)
    return a*b
    
def div(a,b):
    print "dividing %r/%r" %(a,b)
    return a/b
    
p=add(30,8)
q=sub(56,90)
r=mul(55,9)
s=div(67,6)

what=add(p,mul(q,(div(r,sub(s,2)))))
print what
