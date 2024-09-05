import numpy as np

# Define matrices A, B, and C
A_num = np.array([[3.7827, 3.3454, 3.2341],
              [2.2122, 3.5678, 3.9087],
              [1.1234, 2.8934, 5.9087]])

B_num = np.array([[3.1234, 3.0987, 3.1234],
              [2.1111, 3.2222, 3.3333],
              [1.0987, 1.3456, 5.1234]])

C_num = np.array([[3.1243, 3.0989, 3.1256],
              [2.6721, 3.6785, 3.9017],
              [1.1254, 2.8956, 5.9187]])

#Operations for above matrices
sum_AB = A_num + B_num
difference_AB = A_num - B_num 
product_AB = np.dot(A_num, B_num )

print("Sum of A and B:")
print(sum_AB)

print("Difference of A and B:")
print(difference_AB)

print("Product of A and B:")
print(product_AB)