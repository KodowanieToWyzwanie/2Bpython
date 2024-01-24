# tab = [a**a for a in range(10)]
# print(tab)

with open("bieg.txt", "r") as plik:
  dane = [map(int,i.split()) for i in plik]

# print(dane)
#jeśli pierwsza liczba większa od drugiej to "trzymaj tak dalej", jeśli nie to drukuj "bierz się  do roboty"
for i in range(len(dane)):
  # a,b = map(int,dane[i])
  a,b = dane[i]
  # a,b = int(a), int(b)
  if a > b:
    print("trzymaj tak dalej")
  else:
    print("bierz się  do roboty")


  

# tab = [1,2,3,4,5]
# tab = [[2,4],1,5]
# tab = [[1,2,3], [3,77,1],  [2,3,10]]
# a,b,c = tab
# print(c)
# print("dlugość tablicy ",len(tab))
#10
# print(tab[2][2])
# print(tab[1][1])
# pierwszy nawias - która tablica
# który element w tej tablicy
#unapacking
# a, c = int(input()), int(input())
# print(a,c)
# a, c = input().rstrip().split()
# print(a,c)
# a, c = int(a), int(c)
# print(type(c))

# a, b = map(int, input().split())
# print(a,b)


# tab = [1,2,3]
# a, *b = tab
# print(a, b)













# with open("bieg.txt", "r") as plik:
#   dane = [map(int, i.split()) for i in plik]
# #[map(int, i.split()) for i in plik]
# print(dane)

# for i in range(len(dane)):
#   a,b = map(int, dane[i])
  
  
