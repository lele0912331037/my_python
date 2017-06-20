

def ziranshu():
    n=1
    while True:
        n+=1
        yield n
        if n > 10:
            break
print('111', list(ziranshu()))
print('222', next(ziranshu()))
#求素数方法1
def prime(s):
    for n in range(2,s):
        if s % n==0:
            return False
    return True

print(list(filter(prime,range(2,101))))

#素数方法2
def is_odd(n):
    return lambda x:x%n>0
def qishu():
    b=ziranshu()
    while True:
        c=next(b)
        yield c
        b=filter(is_odd(c),b)
for i in qishu():
    if i<10:
        print(i,end=" ")
    else:
        break
#奇数
def is_odd1(n):
    return n%2>0
def qishu1():
    #b=ziranshu()
    c=filter(is_odd1,ziranshu())
    for x in c:
        yield x
print('\n')
for i in qishu1():
    if i<10:
        print('this is :%s' % i)
    else:
        break
