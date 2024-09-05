import itertools

# Define the list
list_1 = ['A', 'B', 'C', 'D', 'E']

# Calculate combinations
combinations = []
for r in range(len(list_1) + 1):
    combinations.extend(itertools.combinations(list_1, r))

# Calculate permutations
permutations = []
for r in range(len(list_1) + 1):
    permutations.extend(itertools.permutations(list_1, r))

# Print results
print("Combinations:")
for combination in combinations:
    print(combination)

print("\nPermutations:")
for permutation in permutations:
    print(permutation)