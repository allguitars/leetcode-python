'''
The range keyword autimatically checks the left bound and 
right bound for you.
The loop will not run if the left bound is equal or 
greater than the right bound.
'''

# this will not run
for i in range(5, 5):
    print('hi')

# this will not run either
for i in range(6, 5):
    print('hi')

# this will run once
for i in range(4, 5):
    print('hi')
