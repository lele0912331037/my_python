n=0
j=0
while n<9:
    n=n+1
    while j<9:
        j=j+1
        print (j,'*',n,"=",n*j,end=" ")
        if n==j:
            j=0
            break
    print ('\t')
