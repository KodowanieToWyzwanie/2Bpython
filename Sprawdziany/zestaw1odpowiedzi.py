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

#Zadanie 3
# W liczbie trzycyfrowej została zatarta cyfra dziesiątek: 3*4. Jaka jest cyfra dziesiątek jeżeli wiadomo, że liczba ta jest podzielna przez 6 ale nie jest podzielna przez 9?

# for i in range(0, 10):

#   liczba = 304 + (10 * i)
#   if liczba % 6 == 0 and liczba % 9 != 0:
#     print(liczba)

#zadanie 4
#Dwucyfrowa liczba została podzielona przez sumę swoich cyfr. oblicz resztę tego działania? Sprawdź dla kilku przypadków

# def najwieksza_reszta(liczba):
#   suma = (liczba % 10 ) * 10 + liczba //10
#   return liczba%suma
# print(najwieksza_reszta(54))


# #Zadanie 5 
# # Czy z podanych trzech boków można utworzyć trójkąt?

a = int(input())
b = int(input())
c = int(input())

