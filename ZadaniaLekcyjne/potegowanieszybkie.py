#import bibliotek - to ma być na górze
import math #np. do funkcji pow, sqrt
import time #np. do liczenia czasu trwania algorytmu

#potegowanie szybkie
def potega_rek2(a,b):
  if b == 0 :
    return 1
  else:
    wynik = (potega_rek2(a, b//2))
    if b % 2 == 0:
      return wynik * wynik
    else:
      return a * wynik * wynik



#####a to potegowanie rekurencyjnie 

def potega_rek(a,b):
  if b == 0 :
    return 1
  else:
    return a * potega_rek(a, b-1)
    
print(potega_rek(3,4))




# https://kalkicode.com/calculate-power-number-using-recursion
# oblicza potęgę dla liczb ujemnych
# pow_number(number, power):
# if power is 0:
#     return 1
# else if power is negative:
#     return 1 / pow_number(number, -power)
# else:
#     return number * pow_number(number, power - 1)


def power(a,b):
  if b == 0:
    return 1
  elif b<0:
    return 1/power(a, -b)
  else:
    return a * power(a, b-1)

# print(power(3,4))
# print(power(3,-4))
# print(pow(3,-4))


#https://pl.wikipedia.org/wiki/Algorytm_szybkiego_pot%C4%99gowania

def potegowanie_rek(a, b):
  if b ==1:
    return a
  else:
    return a * potegowanie_rek(a, b-1)

def szybkie_potegowanie_rek(a, b):
  if b == 1: 
    return a
  w = szybkie_potegowanie_rek(a, b//2)
  if b % 2 == 0:
    return w * w
  else:
      return a *   w * w


def szybkie_potegowanie_rek1(a,b):
  if b==0:
    return 1
  if b%2 == 1: #gdy n jest nieparzyste
    return a * szybkie_potegowanie_rek1(a, b - 1)
  # aby dwa razy nie wchodzić w tą samą rekurencję
  w = szybkie_potegowanie_rek1(a, b/2)
  return w * w

#sprawdzanie czasu działania algorytmu
start = time.time()
szybkie_potegowanie_rek(3,1_050)
stop = time.time()
czas =stop - start
print(f"{czas} rek w przed if ")

start = time.time()
pow(3,1_050)
stop = time.time()
czas = stop - start
print(f"{czas} pow ")



def potegowanie_ite(a,b):
  wynik = 1
  while b > 0:
    wynik *= a
    b -= 1
  return wynik

# 2**10 = ((2**5))**2 = (2(2**2)**2)**2
def szybkie_potegowanie_ite(a,b):
  wynik = 1
  while b > 0:
    if  b%2 == 1:
      wynik *= a
    a *= a  
    b = b // 2
  return wynik

# print(szybkie_potegowanie_rek(3,5))
# start = time.time()
# print(potegowanie_ite(3,1_000))
# stop = time.time()
# czas =stop - start
# print(f"{czas} iteracyjne ")
# start = time.time()
# print(szybkie_potegowanie_ite(3,1_000))
# stop = time.time()
# czas = stop - start
# print(f"{czas} szybkie iteracyjne ")
# print(szybkie_potegowanie_rek(3,4))



