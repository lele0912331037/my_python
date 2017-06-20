
def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
  
output = filter(is_palindrome, range(1, 1000))  
print(list(output))  

def is_palindrome1(n):
    return str(n)==str(n)[::-1]
output = filter(is_palindrome1, range(1, 1000))
print(list(output))

def is_palindrome2():
    return lambda x:str(x)==str(x)[::-1]
output = filter(is_palindrome2(), range(1, 1000))
print(list(output))

def is_palindrome3(n):
    return lambda x:str(x)==str(x)[::-1]
output = filter(is_palindrome3(1), range(1, 1000))
print(list(output))
