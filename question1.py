# Define matrices using python lists.
A = [[3.7827, 3.3454, 3.2341],
     [2.2122, 3.5678, 3.9087],
     [1.1234, 2.8934, 5.9087]]

B = [[3.1234, 3.0987, 3.1234],
     [2.1111, 3.2222, 3.3333],
     [1.0987, 1.3456, 5.1234]]

C = [[3.1243, 3.0989, 3.1256],
     [2.6721, 3.6785, 3.9017],
     [1.1254, 2.8956, 5.9187]]

# Function to add two matrices
def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Function to subtract two matrices
def subtract_matrices(mat1, mat2):
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

# Operations for 
sum_AB = add_matrices(A, B)
difference_AB = subtract_matrices(A, B)
product_AB = multiply_matrices(A, B)

print("Sum of A and B:")
print(sum_AB)

print("Difference of A and B:")
print(difference_AB)

print("Product of A and B:")
print(product_AB)