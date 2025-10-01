class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Empty stack to keep track of push/pop operations
        stack = []
        # Pointer to keep track of the current element in the popped array
        i = 0
        
        for n in pushed:
            stack.append(n) # Push element in stack
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack