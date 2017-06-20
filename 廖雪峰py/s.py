def ziranshu():
    n=0
    while True:
        n=n+1
        yield n
        if n>100:
            break
def _is_odd(s):
    for n in range(2,s):
        print (s,'#')
        print (n,'*')
#        if s % n==0:
#            return False
#    return True
    #return lambda x:x%s>0
b=list(ziranshu())
#print (b)
a=list(filter(_is_odd(3),range(3,10)))
print (a)
