lst = [2,3,45,7,2,1,3,4,5]
# print(lst)
#print(sorted(lst))

for j in range(len(lst)):
  swapped = False #to żeby nie trzeba było sortować nie potrzebnie 
  for i in range(len(lst)-1-j):
    if lst[i] > lst[i+1]:
      lst[i],lst[i+1] = lst[i+1],lst[i]
      swapped = True
  if not swapped:
    break
  #print(lst)


szukana = 90

le = 0
pr = len(lst) - 1 #bo chcemy dodawać indeksy
while le <= pr: #dopóki nie podzielę całej tablicy
  c = (le+pr)//2  #biorę środkowy index
  if szukana == lst[c]:# porównuję 
    print(f"znaleziono na pozycji {c}") #jeśli znajdę to wyświetlam index
  if szukana > lst[c]: #jeśli szukana jest większa 
      le = c + 1 #skracam tablicę lewy index przesuwam na środek plus 1
  else:
      pr = c - 1 
else: #jeśli cała pętla się zrobi i nie znajdę 
  print("nie znaleziono")