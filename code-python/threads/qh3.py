from itertools import filterfalse

x=int(input ("Introduz um número"))
def IsPrime(x):
    for u in range(2, x-1):
        if x%u==0:
            return False
    return True

if IsPrime(x):
    print(x, " é primo")
else:
    print(x, "não é primo")