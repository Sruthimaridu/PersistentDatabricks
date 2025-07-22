import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
print(a)
print(b)

print(np.zeros((2,3)))        #2x3 array
print(np.ones((3,4)))            # 3x2 array
print(np.eye(3))                #3x3 array
print(np.full((2,2),7))         #2x2 filed with 7
print(np.arange(0,10,2))        #[0,2,4,6,8]
print(np.linspace(0,1,5))     # values from 0 to 5

#array attributes
arr = np.array([[1, 2], [3, 4]])
print(arr)
print(arr.shape )        #(2,2)
print(arr.ndim )        #2
print(arr.size)         #4
print(arr.dtype)         #data type
  
#indexing and slicing
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[0,1] )          #2
print(arr[:,1])            #[2,5] (all rows, column1)
print(arr[1,:])           #[4,5,6] (row 1)

#mathematical operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a)
print(b)

print(a+b)           #[5 7 9]
print(a*b)           #[4  10  18]
print(np.dot(a,b) )  
  
print(np.mean(a) )      #2.9
print(np.std(b) )        #standard deviation
print(np.sum(a) )        #6
print(np.max(b) )        #6

#reshaping and flattening
arr=np.array([[1,2], [3,4]])
import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
print("Array a:", a)
print("Array b:\n", b)

# Special arrays
print("\nSpecial Arrays:")
print("Zeros (2x3):\n", np.zeros((2, 3)))
print("Ones (3x4):\n", np.ones((3, 4)))  # comment corrected
print("Identity matrix (3x3):\n", np.eye(3))
print("Full array (2x2) with 7:\n", np.full((2, 2), 7))
print("Arange from 0 to 10 with step 2:\n", np.arange(0, 10, 2))
print("Linspace from 0 to 1 with 5 values:\n", np.linspace(0, 1, 5))

# Array attributes
arr = np.array([[1, 2], [3, 4]])
print("\nArray Attributes:")
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Dimensions (ndim):", arr.ndim)
print("Size:", arr.size)
print("Data Type (dtype):", arr.dtype)

# Indexing and slicing
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nIndexing and Slicing:")
print("Array arr2:\n", arr2)
print("Element at [0,1]:", arr2[0, 1])
print("All rows, column 1:", arr2[:, 1])
print("Row 1:", arr2[1, :])

# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nMathematical Operations:")
print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a * b (element-wise):", a * b)
print("Dot product:", np.dot(a, b))
print("Mean of a:", np.mean(a))
print("Standard deviation of b:", np.std(b))
print("Sum of a:", np.sum(a))
print("Max of b:", np.max(b))

# Reshaping and flattening
arr3 = np.array([[1, 2], [3, 4]])
print( arr3.reshape(1, 4))
print(arr3.flatten())
