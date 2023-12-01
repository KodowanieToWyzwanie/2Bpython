def czy_pierwsza(n):
  for i in range(2, n//2+1):
    if n%i ==0:
      print("złożona")
      break
  else:
    print("pierwsza")

czy_pierwsza(n)

def czy_pierwsza1(n):
  for i in range(2, n//2+1):
    if n%i ==0:
      return False
  return True
print(czy_piewsza(6))

def czy_pierwsza(a):
    return all(a % i != 0 for i in range(2, a // 2 + 1))
