class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        pairs = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in pairs: # if it is close one
                if not stack or stack[-1] != pairs[c]: #not in stack or not match
                    return False
                stack.pop() # match, then remove
            else: # open one
                stack.append(c)
        return True if not stack else False #"not stack"：the stack is empty