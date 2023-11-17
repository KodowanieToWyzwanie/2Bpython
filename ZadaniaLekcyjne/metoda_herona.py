#filmik omawiający metodę https://www.youtube.com/watch?v=C_FFlau09_8

def metoda_herona(p,eps):
  b = p # przypisujemy boku wartość pola
  while abs(b - p/b) > eps:  #sprawdzamy czy jest większe od przybliżenia 
    b = (b + p/b)/2 #zmiejszamy w każdej iteracji
  return (b + p/b)/2

print(metoda_herona(9, 0.000001))
