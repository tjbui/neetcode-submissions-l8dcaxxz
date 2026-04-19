class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                added = stack.pop() + stack.pop()
                stack.append(added)
            elif token == "-":
                sub = stack.pop()
                curr = stack.pop()
                stack.append(curr - sub)
            elif token == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif token == "/":
                div = stack.pop()
                curr = stack.pop()
                stack.append(int(curr / div))
            else:
                stack.append(int(token))

        return stack.pop()
        

# ["10", "1", "2", "+", "3", "*", "4", "-", "*"]

# [((1 + 2) * 3) - 4] * 10

# 10
# stack

# 1
# 10
# stack

# 2
# 1
# 10
# stack

# + --> pop(), pop()
# added = 1 + 2

# 3
# 10
# stack

# 3
# 3
# 10
# stack

# * --> pop(), pop()