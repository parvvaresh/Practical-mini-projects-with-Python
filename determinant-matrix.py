from numpy.core.numeric import array_equal
import numpy as np
def tilde(array, i , j):
  array_test = np.zeros((len(array) - 1,len(array) - 1))

  list1 = []

  for c in range(0, len(array)):
    for r in range(0, len(array)):
      if c == i or r == j:
        continue
      list1.append(array[c][r])

  array_test = np.array(list1)
  array_test = array_test.reshape(len(array) - 1,len(array) - 1)
  return array_test



def determinant(array):
  if len(array) == 1:
    return array[0][0]
  if len(array) == 2:
    return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])

  j = 0
  determinant_calucte = 0


  while (j <= len(array) - 1):
    determinant_calucte += determinant(tilde(array,0,j))  * array[0][j] * pow(-1,0 + j + 2) 
    j = j + 1

  return determinant_calucte   

    



  
size = int(input("Enter your matrix size : "))
array = np.zeros((size,size))

value = 0

print("Enter matrix valleys one by one : ")
for i in range(0, size):
  for j in range(0, size):
    value = int(input())
    array[i][j] = value



print("Matrix : ")
print(array)    
print("----------------------------------")


i = int(input("i  : "))
j = int(input("j : "))

print(f"tide(array, {i}, {j})")
print(tilde(array, i - 1, j - 1))
print("----------------------------------")
print("determinant : ")
print(determinant(array))