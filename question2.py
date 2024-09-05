import numpy as np

# Define the list
list_1 = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# 1. Iterate using a for loop
print("Using the for loop:")
for item in list_1:
    print(item)

# 2. Iterate using for loop and range
print("\nUsing for loop with range:")
for i in range(len(list_1)):
    print(list_1[i])

# 3. List Comprehension
print("\nUsing list comprehension:")
squared = [x**2 for x in list_1]
print(squared)

# 4. Enumerate
print("\nUsing enumerate:")
for index, value in enumerate(list_1):
    print(f"Index: {index}, Value: {value}")

# 5. Iter function and next function
print("\nUsing iter and next:")
iterator = iter(list_1)
while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break

# 6. Map function
print("\nUsing map function (adding 1000 to each number):")
m_list = list(map(lambda x: x + 1000, list_1))
print(m_list)

# 7. Using zip
another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nUsing zip:")
zipp = zip(list_1, another_list)
for a, b in zipp:
    print(f"{a}, {b}")

# 8. Using Numpy Module
np_arr = np.array(list_1)
print("\nUsing NumPy:")
print("Original Array:")
print(np_arr)
print("Squared Array:")
print(np_arr ** 2)
print("Sum of Array Elements:")
print(np.sum(np_arr))