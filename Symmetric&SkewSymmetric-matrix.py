import numpy as np

  

   

def transpose(A):
    n = np.shape(A)
    array_z = np.zeros((n[1],n[0]))
  
    for i in range(0,n[0]):
        for j in range(0, n[1]):
          array_z[j][i] = A[i][j]
            
    return array_z   


def isSymmetric(B):
     S =  transpose(B)
    
     n = np.shape(B)
     for i in range(0, n[0]):
        for j in range(0, n[1]):
          if B[i][j] !=  S[i][j]:
            return False
     return True      


def isSkewSymmetric(A):
  S = transpose(A)
  n = np.shape(A)    
  for i in range(0, n[0]):
        for j in range(0, n[1]):
          if  A[i][j] != -1 * S[i][j]:
            return False
  return True  

     
  
A = np.array([ [1, 1, 1, 1],
               [2, 2, 2, 2],
               [3, 3, 3, 3],
               [4, 4, 4, 4] ])


B = np.array([ [1,2,3],
               [2,3,4],
               [3,4,1] ])



C = np.array([ [0,-2,4],
               [2,0,-2],
               [-4,2,0] ])


print("matrix A : ")
print(A)
print("----------------------------------------------------------------------------------")
print("transpose A : ")
print(transpose(A))


print("----------------------------------------------------------------------------------")
print("matrix B : ")
print(B)

print("----------------------------------------------------------------------------------")
if isSymmetric(B) == True:
  print("matrix B is symmetric : True")
else:
  print("matrix B is symmetric : False")
print("----------------------------------------------------------------------------------")  
if isSkewSymmetric(B) == True:
  print("matrix B is skew symmetric : True")
else:
  print("matrix B is skew symmetric : False")  

print("----------------------------------------------------------------------------------")
print("matrix C : ")
print(C)


print("----------------------------------------------------------------------------------")
if isSymmetric(C) == True:
  print("matrix C is symmetric : True")
else:
  print("matrix C is symmetric : False")
print("----------------------------------------------------------------------------------")  
if isSkewSymmetric(C) == True:
  print("matrix C is skew symmetric : True")
else:
  print("matrix C is skew symmetric : False")  