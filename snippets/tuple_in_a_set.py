myset = set()

# add one tuple
myset.add((1, 2))
print(myset)  # {(1, 2)}

# add another tuple in different order
myset.add((2, 1))
print(myset)  # {(1, 2), (2, 1)} -> 被視為不同

# 所以 tuple 是有順序之分的

print((1, 2) == (2, 1))  # False
