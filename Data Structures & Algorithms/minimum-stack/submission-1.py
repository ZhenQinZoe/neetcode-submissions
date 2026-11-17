class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] #we need this beacuse we need O(1) time for min

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        # the key is to update the min here, we need to check the min between val and the last min of min_stack, also we need to make sure that the min_stack is not empty, then we updat the min_stack
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()# we need to pop the cooradinate min stack too, so that all the element in stack is min

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]