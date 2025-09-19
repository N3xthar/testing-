# element wise operation in the numpy array 
# 
#  
import numpy as np 

arr = np.array([2,2,3,4,56,7,8,9])
print(arr**2)
print(arr+2)
print(arr-2)
print(arr/2)     # do the division 
print(arr//2)       # while gives  the quotient 



#               Agression function !!! 


arr = np.array([[23,34,5,66],
                [11,23,43,5],
                [1,1,1,1]])

print("Agressesion function results are !! ")
print(np.sum(arr))  
print(np.max(arr))  
print(np.min(arr))  
print(np.std(arr))    # to calculate the standard devitation of the array
print(np.var(arr))      # to calculate the variance of the array
