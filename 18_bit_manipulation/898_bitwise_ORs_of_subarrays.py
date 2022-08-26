'''
898. Bitwise ORs of Subarrays
https://leetcode.com/problems/bitwise-ors-of-subarrays/

Super Lazy Coder: https://youtu.be/dDlZD9pOzQI

#BitManipulation #DynamicProgramming
#Note (Notability)
'''


def subarrayBitwiseORs(arr):
    res = set()
    prev = set()

    for n in arr:
        curr = {n}
        res.add(n)

        for p in prev:
            curr.add(n | p)
            res.add(n | p)

        prev = curr

    return len(res)


assert subarrayBitwiseORs([0]) == 1
assert subarrayBitwiseORs([1, 1, 2]) == 3
assert subarrayBitwiseORs([1, 2, 4]) == 6

print('All tests have passed.')
