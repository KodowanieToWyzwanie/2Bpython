# Grupa 1
# Do tabeli wpisz 6 imion - pytając się za każdym razem użytkownika 
# W nowej tabeli wpisz ile ma znaków każde z imion 

#   Grupa 2
# Do tabeli wpisz 6 owoców - pytając się za każdym razem użytkownika o jego ulubiony owoc
# W nowej tabeli wpisz ile ma znaków każdy z owoców


owoce = []
dl = []
for i in range(6):
  owoce.append(input("Podaj owoc\n"))
  dl.append(len(owoce[i]))

print(owoce)
print(dl)
