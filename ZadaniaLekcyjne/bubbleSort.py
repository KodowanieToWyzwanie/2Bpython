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
