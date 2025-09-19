# we understand properties and operations 

# shape size and type 








#                   SHAPE :== dimension finding 


# this is used to understand how is our data is how many rows and the column and much more yarrr !! 

import numpy as np 


array_2d = np.array([[23,45,6,4,3],
                    [23,55,54,3,2],
                    [1,21,45,21,1]]) 

array_3d = np.array([[[2,3,4,5]
                      ,[6,7,8,9],
                      [10,11,23,45]]])

print("Rows and Columns  of two array  array is :==  ",array_2d.shape)   # tell the number size and the length of the array  means how many rows and the column first one tells the rows and the second one tells the number of columns 

# o/p :== (3, 5)



print("Total number of column and the rows are :== " , array_3d.shape)


#               SIZE  :== tells the total number of elements in the array !!!!! 


print("Total_number of elemetns in 2d array is the array ",array_2d.size)

print("Total number of element in 3d array  is :== " , array_3d.size)




#                           ndim :====---  tells the dimension of the array !!! 

print("Tells the number of dimension in 2d   array :== ", array_2d.ndim )


print("Tells the number of dimension in 3d   array :== ", array_3d.ndim )









#      .dtype :== tells the data type of the individual array elements 

print("The data type of 2d array is :== " , array_2d.dtype)

print("The data type of 3d array is :== " , array_3d.dtype)





# changing the data type of the array 



                                 # .astype()

                                 # converting the one data type to another data type 


# Syntax  !!  array.astype(New.type)


float_data_type = np.array([[12.1,13.2,11.21,14.67],
                           [12.1,56.5,89.0,16.1]])
print("The data type of the array is :== " , float_data_type)
print("The data type of the array is :== " , float_data_type.dtype) 

# now i have to change the data type of the array !!


float_data_type = float_data_type.astype(int)
print("Now changing the data type of the array are :== ",float_data_type)


# now the data type is changed yarrr !!!! 

print("Look at the changed data type is :== " , float_data_type.dtype )