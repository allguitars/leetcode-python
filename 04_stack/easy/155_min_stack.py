# 155. Min Stack
# neetcode: https://youtu.be/qkLl7nAwDPo

# Time: O(1)
# Space: O(n) <- 額外需要一個 min stack

# min_stack 的 size 永遠跟 stack 一樣
# 其存放與 stack 對應的最小值，也就是在 stack 元素增加的任一時間點，其所存在的最小值。
# 例如：
# stack = [1, 2, -2, 5, -3]
# min_stack = [1, 1, -2, -2, -3]  <- 最上面的永遠存放目前 stack 中的最小值

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))  # pick a smaller number
        else:  # min stack is empty
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())  # -3
obj.pop()            # -3 is gone
print(obj.top())     # 0
print(obj.getMin())  # -2
