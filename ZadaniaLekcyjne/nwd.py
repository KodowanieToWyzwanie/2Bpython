a = int(input("Podaj liczbę "))
b = int(input("Podaj liczbę "))
#Algorytm Euklidesa
#metoda nieoptymalna 
# while a != b:
#   if a > b:
#     a = a-b
#   else:
#     b = b-a
# print(a)
#czynność


def nwd(a,b):
  while b !=0:
    a, b = b, a%b
  return a 
#funkcja rekurencyjna
def nwd_rek(a,b):
  if b == 0: #warunek bazowy
    return a 
  else:
    return nwd_rek(b, a%b) #wywołanie samej siebie

n = nwd(a,b)
print(n)

    


