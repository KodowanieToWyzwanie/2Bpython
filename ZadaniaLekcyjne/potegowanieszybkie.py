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
