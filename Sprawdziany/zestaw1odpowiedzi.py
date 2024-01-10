# Zadanie 1
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej. Podaj dwa największe dzielniki otrzymanej liczby. Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr.

# liczba  = 47
# lustrzana = (liczba % 10)*10 + liczba//10
# suma = liczba +lustrzana 
# i = suma 
# licznik = 0
# while i > 0 and licznik <2:
#   if suma % i == 0:
#     print(i, end=" ")
#     licznik += 1
#   i -= 1


# Zadanie 2
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej.  Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr. sprawdz czy dla kliku wybranych liczb otrzymana suma dzieli się przez sumę cyfr jednej z liczb dwucyfrowej - tj. czy np. 42 +24 dzieli się przez 6


# x = input()
# y = x[::-1]

# def funkcja(x,y):
#   suma = int(x) + int(y)
#   liczba = int(x[-1]) + int(y[-1])
#   print(liczba)
#   return suma % liczba == 0
# print(funkcja(x,y))

# zwierze = input().lower()
# palindrom = zwierze[::-1]
# if zwierze == palindrom:
#   print("zdecydowanie")
# else:
#   print("bruh")


#Liczba lustrzana
# def lbstr(a):
#   L = []
#   for _ in str(a): 
#     L.append(_)
#   L.reverse()
#   x = ""
#   for a in L:
#     x += a
#   return int(x)

# Zadanie 1
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej. Podaj dwa największe dzielniki otrzymanej liczby. Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr.
def lbstr(a):
  lustrzana = (a % 10)*10 + a//10
  return lustrzana
def sum(a):
  if a < 100:
    al = lbstr(a)
    sum = a+al
    idx = 1
    print(f"{a} i lustrzana {al} ich suma {sum}")
    for i in range(sum, 1, -1):
      if idx <= 2 and sum%i == 0:
        print(f"{idx} dzielnik: {i}")
        idx += 1
sum(45)
sum(32)   


# Zadanie 2
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej.  Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr. sprawdz czy dla kliku wybranych liczb otrzymana suma dzieli się przez sumę cyfr jednej z liczb dwucyfrowej - tj. czy np. 42 +24 dzieli się przez 6

def lbstr(a):
  lustrzana = (a % 10)*10 + a//10
  return lustrzana
def sum(a):
  sum = 0
  if a < 100:
    al = lbstr(a)
    sum = a+al
  return sum
def suma_cyfr(a):
  return a//10+a%10 
def czy_dzieli(a):
  return sum(a)%suma_cyfr(a) ==0

print(czy_dzieli(45))
print(czy_dzieli(89))



#Zadanie 3
# W liczbie trzycyfrowej została zatarta cyfra dziesiątek: 3*4. Jaka jest cyfra dziesiątek jeżeli wiadomo, że liczba ta jest podzielna przez 6 ale nie jest podzielna przez 9?
for i in range(10):
  liczba = (304 + (i*10))
  if liczba % 6 == 0 and liczba % 9 != 0:
    print(liczba)  

#zadanie 4
#Dwucyfrowa liczba została podzielona przez sumę swoich cyfr. oblicz resztę tego działania? Sprawdź dla kilku przypadków
suma=0
x=int(input())
suma=(x % 10 + x//10)
print(x%suma)



# #Zadanie 5 
# # Czy z podanych trzech boków można utworzyć trójkąt?


a = int(input())
b = int(input())
c = int(input())
if (a+b > c) and (a+c > c) and (b+c > a):
  print("tak")
else:
  print("nie")
