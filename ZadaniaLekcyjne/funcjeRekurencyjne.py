import time
import timeit


def iloczyn(x,y):
  if y==1:
    return x
  else:
    k = y//2
    z = iloczyn(x,k)
    if y%2==0:
      return z+z
    else:
      return x+z+z

#print(iloczyn(4,5))


def silnia(x):
  if x==1:
    return 1
  else:
    return x*silnia(x-1)

#print(silnia(6))


def iloczyn1(x,y):
  if y==1:
    return x
  else:
    k= y//2
    z = iloczyn(x,k)
    if y%2==0:
      return z+z
    else:
      return x+z+z

#print(iloczyn1(9,10))

def silnia(n):
  if n==1: 
    return 1
  else:
    return n*(silnia(n-1))

def silniaFor(n):
  silnia =1
  for i in range(1,n+1):
    silnia *=i
  return silnia


startTime = timeit.default_timer()
 
silnia(599)
endTime = timeit.default_timer()
print(endTime - startTime)

startTime1 = timeit.default_timer()
silniaFor(599)
endTime1 = timeit.default_timer()
print(endTime1 - startTime1)











