def get_combinations(lst):
    if len(list_1) == 0:
        return [[]]
    result = []
    first_element = list_1[0]
    rest_elements = list_1[1:]
    for combination in get_combinations(rest_elements):
        result.append([first_element] + combination)
        result.append(combination)
    return result

def get_permutations(list_1):
    if len(list_1) == 1:
        return [list_1]
    result = []
    for i in range(len(list_1)):
        current_element = list_1[i]
        rest_elements = list_1[:i] + list_1[i+1:]
        for permutation in get_permutations(rest_elements):
            result.append([current_element] + permutation)
    return result

# Define list
list_1 = ['A', 'B', 'C', 'D', 'E']

# Calculate combinations
combinations = get_combinations(list_1)
print("Combinations:")
for combination in combinations:
    print(combination)

# Calculate permutations
permutations = get_permutations(list_1)
print("\nPermutations:")
for permutation in permutations:
    print(permutation)
