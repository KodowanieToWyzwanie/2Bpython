import random

def bubbleSort():
  list = random.sample(range(10,100),7)
  print(f"nieposortowana {list}")
  n = len(list)
  for i in range(n):
    for j in range(n-i-1):
      if list[j]>list[j+1]:
        list[j],list[j+1]=list[j+1],list[j]
  print(f"posortowana {list}")
  return list

bubbleSort()


#### wersja ze sprawdzaniem czy lista jest posortowana wcześniej
lst = [3,6,7,8,8,2,3,1]

# lst.sort()
# print(lst)
n = len(lst)
j = 0
while j < n-1:
  swapped = False
  for i in range(n-1-j):
    if lst[i]>lst[i+1]:
      #zamień
      lst[i],lst[i+1] = lst[i+1],lst[i]
      swapped = True
  j += 1
  print(lst)
  if not swapped:
    break
      
