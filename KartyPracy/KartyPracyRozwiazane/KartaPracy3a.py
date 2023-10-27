#Karta Pracy 3A
##################dodatki
#https://www.tutorialstonight.com/python/pattern-program-in-python
#Zad1
def szlaczek1(n):
  for i in range (n):
    print("*-|",end="")
#Zad 2
def szlaczek2(n):
  for i in range (1,n,2):
    print(i*"*","||",(i+1)*"*","--",end="")


#Zad 3
def szlaczek3(n):
  for i in range (0,n,2):
    print("*",(i+1)*"|","*" , 2*i*"-",end="")  


#Zad 4
def szlaczek4(n):
  for i in range(n):
      for j in range(n):
          if i-j==n//2 or j-i==n//2 or i+j==n//2 or i+j==3*(n//2):
              print("*", end="")
          else:
              print(" ", end="")
      print()

#zad 5 krzyż
def szlaczek5(n):
  for i in range(n):
      for j in range(n):
          if j == n//2:
              print("*",end="")
          if i==n//2:
            print("?",end="")
          else:
              print(" ",end="")
      print()

#zad 6
def szlaczek6(size):
    for i in range(size):
      for j in range(size):
        if i==j:
          print ("*",end="")
        elif i+j==size-1:
          print ("?",end="") 
        else:
          print("   ",end="")
      print()


#zad 7
def szlaczek7(size):
  for i in range(size):
    for j in range(size):
      if i==0 or i==size-1 or j==0 or j==size-1 or i==j==size//2:
        print ("*",end="")
      else:
        print(" ",end="")
    print()




