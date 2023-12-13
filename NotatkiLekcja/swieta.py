napis = "Wesołych Świąt! to są życzenia"
samogloski = "aAeEąĄęĘiIuUoOyY"
licznik = 0
for i in napis:
  if i in samogloski:
    licznik +=1

print(f"liczba samogłosek to {licznik}")


with open("plik.txt","r") as plik:
  dane = plik.read().split()

print(dane)

a,b = dane

print(a)

#print(napis.count(" ")+1)
# wyraz = 1
# for i in napis:
#   if i ==" ":
#     wyraz +=1

# print(wyraz)

napis = "Wesołych Świąt!"
lista = ['a','o','u','i','y','ą','ę','e']
samogloski= "aou.."
licznik = 0
for i in napis.lower():
  if i in lista:
    licznik += 1

print(licznik)

tab = [4,6,5]
a,*b = tab
print(b)
