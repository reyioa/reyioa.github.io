import random

def set_theory():
  rand_size = random.randint(5, 10)
  arr1 = set()
  arr2 = set()
  arrS = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  intersectArr = ()
  for i in range(rand_size):
      arr1.add(random.randint(1, 10))
      arr2.add(random.randint(1, 10))
    
  set_type = random.randint(0, 3)
  if set_type == 0:
    #   Union
      print(f"A: {arr1}")
      print(f"B: {arr2}")
      print("What is AuB")
      intersectArr = arr1.union(arr2)
      
      x = input()
      print(f"the answer is {intersectArr}")  
  elif set_type == 1:
    #   intersection
      print(f"A: {arr1}")
      print(f"B: {arr2}")
      print("What is AnB ")
      intersectArr = arr1.intersection(arr2)
      x = input()
      print(f"the answer is {intersectArr}")
  elif set_type == 2:
      print(f"Let S = {arrS}")
      print(f"Let A = {arr1}")
      print(f"Let B = {arr2}")
      print("")
      if random.randint(0, 1) == 0:
          print("What is A'")
          intersectArr = arrS - arr1
      else:
          print("What is B'")
          intersectArr = arrS - arr2
          
      x = input()
      print(f"the answer is {intersectArr}")  
  else:
      print(f"Let S = {arrS}")
      print(f"Let A = {arr1}")
      print(f"Let B = {arr2}")
      if random.randint(0, 1) == 1:
          print("What is (AnB)'")
          intersectArr = arrS - arr1.intersection(arr2)
      else:
          print("What is (AuB)'")
          intersectArr = arrS - arr1.union(arr2)
      x = input()
      print(f"the answer is {intersectArr}")  
