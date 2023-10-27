#import math

#Zadanie 1
def ciagSzescianow(n):
  for i in range (1,n+1):
    print(i**3+3, end=" ")
  print("\n") 

#ciagSzescianow(5)
#Zadanie 2
def podzielne15():
  for i in range(100,1000,15):
    print(i, end="  ")
  print("\n")
#podzielne15()

#Zadanie 3
def dzielniki(n):
  print("dzielniki liczby to:")
  #bo podłoga- match.floor to za mało
  for i in range (1,n//2+1):
    if n%i ==0:
      print(i,end=", ")

#dzielniki(20)

#Zadanie 4
def sumaDwucyfrowych():
  suma=0
  for i in range (10,100):
    suma +=i
  print(suma)

#sumaDwucyfrowych()

#Wypisywanie ciągu od tyłu 
# for i in range (20,0,-1):
#   print(i,end=" ")

#Zadanie 5
def bajtus(x,n):
  for i in range (1,n+1):
    if i!=x:
      print(i)

#bajtus(4,5)

#Zadanie 6
#ciag fibbonaciego z petla for
def ciagFib(n):
  a,b=1,1
  print(f"Ciąg Fibbonaciego\n{a} {b} ",end="")
  for _ in range (2,n+1):
    a,b=b,a+b
    print(b,end=" ")

ciagFib(10)

