# ** math.pow
# 2 * 2 * 2  *  
def potega(a, b):
  wynik = 1
  for _ in range(b, 0, -1): #z pętlą for działa szybciej
    wynik *= a  
  # while b > 0:
  #   wynik *= a
  #   b -= 1
  return wynik


def szybkie_potegowanie_ite(a,b):
  wynik = 1
  
  while b > 0:
    if  b%2 == 1:
      wynik *= a
    a *= a  
    b = b // 2
  return wynik
  
print(szybkie_potegowanie_ite(2,11))
#print(potega(2, 11))

#jak działają funkcje
def dodawanie(a, b):
  return a + b

wynik = dodawanie(6,8)
print(wynik)
def nwd(a,b):
  while b !=0:
    a,b = b, a%b
  return a

print(nwd(14,24))
