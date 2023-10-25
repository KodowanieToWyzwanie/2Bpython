# 1. napisz funkcję, która podaje wynik podaje:
#   Fizz dla licz podzielnych przez 3, 
#   Buzz dla licz podzielnych przez 5, 
#   Fizz Buzz dla liczb podzielnych przez 3 i przez 5 (nie można użyć 15!) oraz 
#   oraz podany argument dla wszystkich pozostałych 
# wywołaj funkcję:
# print(FizzBuzz(5))
# print(FizzBuzz(3))
# print(FizzBuzz(15))
# print(FizzBuzz(7))
# *program działa po kolei
# 2. Wyświetl tabliczkę mnożenia od 1 do 10
# 3.wersja 1 Wyświetl kolejnych 20 lat przestępnych - najbliższy rok przestępny w 2024
# Wersja 2 Wyświetl lata przestępne od roku 2024 do 1582
# Obecnie powszechnie stosuje się rachubę zgodną z kalendarzem gregoriańskim, wprowadzonym w 1582 roku bullą papieża Grzegorza XIII („Inter gravissimas”), w której wprowadzono następującą modyfikację kalendarza juliańskiego: nie uznaje się lat przestępnych wypadających na koniec wieku, z wyjątkiem tych, w których liczba stuleci jest podzielna przez 4. Inaczej mówiąc w myśl tej reguły latami przestępnymi są te, których numeracja:

# jest podzielna przez 4
# jest podzielna przez 400
# latami przestępnymi nie są te podzielne przez 100

# Dotychczas według tej reguły lata 1600 i 2000 były przestępnymi, a lata 1700, 1800, 1900 nie. W przyszłości rok 2100 nie będzie rokiem przestępnym.


#przykładowe rozwiązanie


def FizzBuzz(a):
  if a%5 ==0 and a%3 ==0:
    return "Fizz Buzz"
  if a%3 ==0:
    return "Fizz"
  if a%5 ==0:
    return "Buzz"
  return a

def multiplicationTable():
  for i in range(1,11):
    for j in range(1,11):
      if i*j<10:
        print(f" {i*j}",end=" ")
      else:
        print(i*j,end=" ")
    print()

def leapYear():
  for i in range(2024, 1582, -4):
    if i%400==0:
      print(i,end="\n\n")
    elif i%100==0:
      print("\n")
      continue
    else:
     print(i,end=' ')

def leapYearInFuture():
  print("\n")
  i=1
  leapYear=2024
  while i<=40:
    if leapYear%400==0:
      print(leapYear,end="\n\n")
    elif leapYear%100==0:
      print("\n\n")
    else:
      print(leapYear,end=' ')
    i+=1
    leapYear+=4



print(FizzBuzz(5))
print(FizzBuzz(3))
print(FizzBuzz(15))
print(FizzBuzz(7))
multiplicationTable()

leapYear()
leapYearInFuture()

leapYearInFuture()








