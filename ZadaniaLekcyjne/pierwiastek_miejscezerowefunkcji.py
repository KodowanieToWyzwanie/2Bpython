ile= 0
for i in range(len(tab)):
  if tab[i] == szukana:
    print("found")
    ile += 1
tab = [1, 2, 3, 4, 5, 6, 7, 8]
szukana = 1
index = tab.index(szukana)
print(f"{szukana} znaleziono na {index} pozycji")
le = 0
pr = len(tab) - 1
while le <= pr:
  sr = (le + pr) // 2
  if szukana == tab[sr]:
    print(f"{szukana} znaleziono na {sr} pozycji")
    break
  else:
    if szukana < tab[sr]:
      pr = sr - 1
    else:
      le = sr + 1
else:
  print("nieznaleziono")

import math
x = 2
print(math.sqrt(2))

# https://informatyka.wsip.pl/informatyka-3/3-metoda-polowienia/
# Podaj x i przyb	x = 2, przyb = 0.001
# Ustal końce przedziału a=0 i b=x	a = 0, b = 2
# Dopóki |b-a| > przyb, wykonuj:
#   Oblicz c = (a+b)/2;
#   Jeżeli c•c > x, przypisz b = c
#   W przeciwnym wypadku przypisz a = c.
#   Wykonywanie pętli, dopóki |b - a| > 0.001
# Wynikiem jest c	Ostatni przebieg pętli:
# 0.0009765625 < 0.001, więc wynikiem jest: 1.4150390625

a = 0
b = 2
x = 2
przyb = 0.00000001
while abs(b - a) > przyb:
  c = (a + b) / 2
  if c * c > x:
    b = c
  else:
    a = c
print(c)

# https://www.youtube.com/watch?v=CTJszKw3Dq4

# Napisz program za pomocą, którego znajdziesz miejsce zerowe funkcji
# f(x =x ** 2 - 60 w przedziale <0,10> z dokładnością do 0.0001
# wykorzystaj algorytm połowienia
# lista kroków:
# 1. zdefiniuj funkcję f(x)
# 2. Zdefiniuj w funkcji miejsce zerowe końce przeciałów a = 0 b 10
# 3. Dopóki abs(b-a)> eps
#   c =  (a+b)/2
#   if f(c) >0 b = c
#   else a=c
# 4. wynikiem jest c


def f(x):
  return (x**2) - 60

a = 0
b = 10
eps = 0.0001
while abs(b - a) > eps:
  c = (a + b) / 2
  if f(c) > 0:
    b = c
  else:
    a = c
print(c)
