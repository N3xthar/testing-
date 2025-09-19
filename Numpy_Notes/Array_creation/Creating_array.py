# Creating the array from the python list !! 
import numpy as np 

    # METHOD 01 CREATION OF THE ARRAY !! 

# if you already has a list !! 

# list 
l = [12,3,45,6,78,9,0,11]
print(l)
print("data type of the list is :== ",type(l))
print("\n")

#converting into the array !! 


array = np.array(l)
print(array)
print("The data type of the array is :== ",type(array))


# METHOD 02 CREATION OF THE ARRAY USING THE DEFAULT VALUES 


                          # ZEROS ARRAY 


# Zeros function by default with the inbuilt data filled with the zeros !! 


# for the 1d array (shape) = (length )
# for 2d array (shape) = (length , length)


#  1 D ARRAY

print("1D array")

zeros_array = np.zeros(3)  # for the one dimensional array !! 
print(zeros_array)


# 2 D array  
print("2D array !! ")

zeros_array = np.zeros([3,3])
print(zeros_array)



            # ONES ARRAY

# 1D array 

print("\n")
print("Ones array !! in one dimensional array !! ")
ones_array = np.ones(10)
print(ones_array)

# 2 D array 
print("2D array !!! ")
ones_2d_array = np.ones([3,4])    # first ones tell the rows and the second one tell the column 
print(ones_2d_array)


#  FULL FUNCTIONS ARRAY [(SHAPE) , DIGIT_JIS_DATA_FILL_KRANA_HAI]

# one dimensional

one_d = np.full(3,999)
print("Full function is := ",one_d)
print(one_d)

# now the 2d array !! 
two_d = np.full([5,6] , 69)
print("\n The 2d full array is : = \n")
print(two_d)



# CREATING THE SEQUENCES OF THE NUMBER  IN THE NUMPY !!  

#  THAT IS ARANGER FUNCTION  
# arange(start , stop , step )



# one dimensional array !!



print("Arange fucntion !! \n")
array_arange = np.arange(10,20,2)
print(array_arange)



# two dimensional array



# now its time for the identity matrix brother 
print("Identity_matrix_is:-- \n")
iden_mat= np.eye(4)
print(iden_mat)