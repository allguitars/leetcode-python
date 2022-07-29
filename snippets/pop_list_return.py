from hashlib import new


lst = [1, 2, 3, ]

item = lst.pop(0)

print(item)  # 1
print(lst)  # [2,3]

# pop the list again
lst.pop(1)
print(lst)  # [2]

new_lst = [10, 20, 30]
lst.append(new_lst.pop(0))  # 取最前面的 elem

print(lst)  # [2,10]
print(new_lst)  # [20,30]
