class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if self.isOpen(c):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if c == ')':
                    if top != '(':
                        return False
                elif c == '}':
                    if top != '{':
                        return False
                elif c == ']':
                    if top != '[':
                        return False
        
        if len(stack) != 0:
            return False
        return True
                

    def isOpen(self, c: str) -> bool:
        if (c == '(' or c == '[' or c == '{'):
            return True

        return False