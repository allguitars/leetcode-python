a = [1, 2, 3, 4, 5]

print(id(a))

b = a
print(id(b))  # the same


def get_address(lst):
    print(id(lst))  # the same


get_address(a)


# copy() function returns a new copy of the original list


real_new = a.copy()
print(id(real_new))  # different
