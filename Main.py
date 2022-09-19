from typing import List

def insertionSort(array) -> List[int]:
  for i in range(1,len(array)):
      min=array[i]
      j=i-1
      while j>=0 and min<array[j]:
        array[j+1]=array[j]
        j-=1
      array[j+1]=min
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
